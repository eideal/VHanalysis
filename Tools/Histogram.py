import ROOT
import math, os, array, types
import palette, style

##################################################
## Helper functions and classes

class Component:

    ## -------------------------------------------- ##
    def __init__(self, name):
        """
        Constructor
        """

        self.name       = name
        self.parent_name= None
        self.color      = None
        self.style      = None
        self.stack      = None
        self.index      = None
        self.label      = None
        self.binning    = None
        self.shapesys   = None
        self.overallsys = None

        self.nbins    = None
        self.nominal  = None
        self.sys_up   = None
        self.sys_down = None

        self.event_yield = 0.0
        self.product = 1.0

        self.density = False

        self.positioning = style.normal_positioning

        
    ## -------------------------------------------- ##
    def apply_style(self, h):
        """
        Apply style to the nominal histogram
        """
        
        h.SetLineColor(self.color)
        h.SetMarkerColor(self.color)
        h.SetFillColor(self.color)
        self.style.apply(h)

        ## Axes
        xaxis = h.GetXaxis()
        xaxis.SetLabelSize(self.positioning.x_label_size)
        xaxis.SetTitleSize(self.positioning.x_title_size)
        xaxis.SetTitleOffset(self.positioning.x_title_offset)
        xaxis.SetTitle(self.label)

        yaxis = h.GetYaxis()
        yaxis.SetLabelSize(self.positioning.y_label_size)
        yaxis.SetTitleSize(self.positioning.y_title_size)
        yaxis.SetTitleOffset(self.positioning.y_title_offset)
        yaxis.SetTitle('yields')
        if self.density:
            yaxis.SetTitle('yields / bin width')
        yaxis.SetNdivisions(508)
        
        

    ## -------------------------------------------- ##
    def initialize(self):
        """
        Prepare the internal TH1Fs to be filled
        """

        ## Calculate number of bins
        self.hi    = self.binning[-1]
        self.lo    = self.binning[0]

        ## Calculate the maximum bin width
        max_bin_width = 0
        for b in range(1,len(self.binning)):
            bin_width = self.binning[b] - self.binning[b-1]
            if bin_width > max_bin_width:
                max_bin_width = bin_width

        ## Calculate extra bins to leave 30% of the space on the x-axis for the legend
        self.legend_max = self.hi + (self.hi-self.lo)*0.76
        self.plot_binning = self.binning + [self.hi+i*max_bin_width for i in range(1, int((self.legend_max-self.hi)/max_bin_width))]
        self.nbins = len(self.plot_binning) - 1

        ## Instantiate the nominal histogram
        self.nominal = ROOT.TH1F('%s.%s' % (self.name, self.parent_name),
                                 self.name,
                                 self.nbins,
                                 array.array('d', self.plot_binning))
        self.nominal.Sumw2()

        ## Instantiate the shape systematics histograms
        self.sys_up   = {}
        self.sys_down = {}
        for sys in self.shapesys:
            ## Histograms for upward variation
            self.sys_up[sys] = ROOT.TH1F('%s.%s_%s_up' % (self.name, self.parent_name, sys),
                                         '%s.%s_%s_up' % (self.name, self.parent_name, sys),
                                         self.nbins,
                                         array.array('d', self.plot_binning))
            self.sys_up[sys].Sumw2()

            ## Histogram for downward variation
            self.sys_down[sys] = ROOT.TH1F('%s.%s_%s_down' % (self.name, self.parent_name, sys),
                                           '%s.%s_%s_down' % (self.name, self.parent_name, sys),
                                           self.nbins,
                                           array.array('d', self.plot_binning))
            self.sys_down[sys].Sumw2()


    ## -------------------------------------------- ##
    def initialize_filled(self):
        """
        Prepare already filled TH1Fs
        """

        ## Retrieve binning
        self.nbins = self.nominal.GetNbinsX()
        self.binning    = []
        for i in range(1, self.nbins+2):
            self.binning.append(self.nominal.GetBinLowEdge(i))

        self.plot_binning = self.binning

        self.hi    = self.binning[-1]
        self.lo    = self.binning[0]

        self.shapesys = []

        self.event_yield = self.nominal.GetSumOfWeights()


    ## -------------------------------------------- ##
    def fill(self, value, weight=1.0, sys='', sys_direction='UP'):
        """
        Give an event to the Component
        Specify sys for filling a systematics histogram instead of the nominal
        """

        if sys:
            if sys_direction == 'UP':
                self.sys_up[sys].Fill(value, weight)
            elif sys_direction == 'DOWN':
                self.sys_down[sys].Fill(value, weight)
        else:
            self.nominal.Fill(value, weight)
            self.event_yield += weight/self.product
            

    ## -------------------------------------------- ##
    def add_systematic_errors(self):
        """
        Add the systematic uncertainty to the statistical uncertainty
        Should be called for completely filled histograms only
        Note that the error calculation is done in relative terms
        """
        
        ## Figure out the overall systematic error contribution
        overall_error = 0
        for sys in self.overallsys:
            low  = abs(1.0 - sys[0])
            high = abs(1.0 - sys[1])
            ## Symmetrize the error
            overall_error += (low**2 + high**2)/2
        

        ## Loop over bins:
        for i in range(1, self.nbins+1):
            bin_nominal    = self.nominal.GetBinContent(i)
            if bin_nominal == 0: continue
            
            bin_stat_error = (self.nominal.GetBinError(i)/bin_nominal)**2
            
            ## Get the shape systematic for this bin
            bin_shape_error = 0
            for sys in self.sys_up.keys():
                low  = abs(bin_nominal - self.sys_down[sys].GetBinContent(i))/bin_nominal
                high = abs(bin_nominal - self.sys_up[sys].GetBinContent(i))/bin_nominal
                ## Symmetrize the error
                bin_shape_error += (low**2 + high**2)/2

            ## Calculate total error
            bin_error = bin_nominal*math.sqrt(bin_stat_error + overall_error + bin_shape_error)

            ## Set the new error
            self.nominal.SetBinError(i, bin_error)



    ## -------------------------------------------- ##
    def set_density(self):
        """
        Especially useful for variable binnings,
        Divides the bin yield by the bin width
        """
        
        self.density = True

        for i in range(1, self.nbins+1):
            bin_nominal = self.nominal.GetBinContent(i)
            bin_error   = self.nominal.GetBinError(i)
            bin_width   = self.nominal.GetBinWidth(i)

            if bin_width == 0: continue

            self.nominal.SetBinContent(i, bin_nominal/bin_width)
            self.nominal.SetBinError(i, bin_error/bin_width)
            
        
        

##################################################
## Main class

class Histogram:

    ## -------------------------------------------- ##
    def __init__(self, name, testing, label, binning, lo=0, hi=1, factor = 1):
        """
        Constructor
        """

        self.name  = name
        self.testing = testing
        self.label = label
        self.factor = factor

        self.xlog = False
        self.ylog = False

        self.do_ratio = False

        self.show_yields = False

        self.density = False

        ## Convert integer number of bins to bin lists, take as is if a list is passed
        if isinstance(binning, types.ListType):
            self.binning = binning
        else:
            self.binning = [(lo + i*(hi-lo)/binning) for i in range(binning+1)]

        ## Internal count of the number of histograms
        self.n = -1

        ## List of components
        self.components = []

        ## List of text labels
        self.text_labels = []

        ## Select a positioning object
        self.positioning = style.normal_positioning
        

    ## -------------------------------------------- ##
    def add(self, name, color, sty, product=1.0, stack=True, shapesys=[], overallsys=[]):
        """
        Add an histogram
        """

        ## Increment the internal count
        self.n += 1
        
        new_component = Component(name)
        new_component.parent_name= self.name
        new_component.index      = self.n
        new_component.color      = ROOT.TColor.GetColor(color)
        new_component.style      = style.style1D[sty]
        new_component.stack      = stack
        new_component.label      = self.label
        new_component.binning    = self.binning
        new_component.shapesys   = shapesys
        new_component.overallsys = overallsys
        new_component.product    = product

        new_component.initialize()

        self.components.append(new_component)

        return self.n


    ## -------------------------------------------- ##
    def add_filled(self, th1f, name, color, sty, stack=True, sys_up={}, sys_down={}, overallsys=[]):
        """
        Add a histogram which has already been filled
        User is responsible to make binning match with other histograms
        shape systematics must be a dictionary of the shape variations
        """

        self.n += 1

        new_component = Component(name)
        new_component.index      = self.n
        new_component.nominal    = th1f
        new_component.color      = ROOT.TColor.GetColor(color)
        new_component.style      = style.style1D[sty]
        new_component.stack      = stack
        new_component.label      = self.label
        new_component.binning    = self.binning
        new_component.sys_up     = sys_up
        new_component.sys_down   = sys_down
        new_component.overallsys = overallsys

        new_component.initialize_filled()

        self.components.append(new_component)

        return self.n


    ## -------------------------------------------- ##
    def add_label(self, text, x=0.5, y=0.5):
        """
        Add a new label to the plot
        """

        self.text_labels.append((text, x, y))

        
    ## -------------------------------------------- ##
    def fill(self, index, value, weight=1.0, sys='', sys_direction='UP'):
        """
        Give an event to the Histogram
        Use index to specfiy which component to fill
        Specify sys for filling a systematics histogram instead of the nominal
        """

        self.components[index].fill(value, weight, sys, sys_direction)


    ## -------------------------------------------- ##
    def make_canvas(self):
        """
        Instantiate the Canvas
        """

        self.canvas = ROOT.TCanvas('%s_canvas' % self.name,
                                   '%s_canvas' % self.name,
                                   0, 0, 800, 600)
        self.canvas.SetLeftMargin(0.20)
        self.canvas.SetLogx(self.xlog)
        self.canvas.SetLogy(self.ylog)
        self.main_pad = self.canvas


    ## -------------------------------------------- ##
    def prepare_components(self):
        """
        Add systematic uncertainties
        """
        
        for component in self.components:
            component.add_systematic_errors()
            component.positioning = self.positioning
            if self.density:
                component.set_density()


    ## -------------------------------------------- ##
    def make_ratio(self, index):
        """
        Add the ratio plot, the stack is to be compared
        to component N. index
        """

        ## Communicate to the class that the ratio is activated
        self.do_ratio = True
        self.positioning = style.ratio_positioning
        self.numerator_index = index
        
        ## Override the default canvas
        self.canvas = ROOT.TCanvas('%s_canvas_ratio' % self.name,
                                   '%s_canvas_ratio' % self.name,
                                   0, 0, 800, 900)

        ## Divide the canvas
        self.canvas.Divide(1, 2, 0.0, 0.01, 0)

        ## Adjust the main pad
        self.main_pad = self.canvas.cd(1)
        self.main_pad.SetPad(0.0, 0.33, 1.0, 1.0)
        self.main_pad.GetFrame().SetBorderMode(0)
        self.main_pad.SetBorderSize(5)
        self.main_pad.SetTopMargin(0.05)
        self.main_pad.SetRightMargin(0.05)
        self.main_pad.SetLeftMargin(0.20)
        self.main_pad.SetBottomMargin(0.0)
        if self.xlog: 
            self.main_pad.SetLogx()
        if self.ylog: 
            self.main_pad.SetLogy()

        ## Adjust the ratio pad 
        self.ratio_pad = self.canvas.cd(2)
        self.ratio_pad.SetPad(0.0, 0.0, 1.0, 0.33)
        self.ratio_pad.GetFrame().SetBorderMode(0)
        self.ratio_pad.SetTopMargin(0.0)
        self.ratio_pad.SetRightMargin(0.05)
        self.ratio_pad.SetLeftMargin(0.20)
        self.ratio_pad.SetBottomMargin(0.4)
        if self.xlog:
            self.ratio_pad.SetLogx()


    ## -------------------------------------------- ##
    def make_legend(self):
        """
        Makes a legend
        """

        
        self.legend = ROOT.TLegend(0.65,
                                   self.positioning.legend_ymax - (self.n+1)*self.positioning.legend_spacing,
                                   self.positioning.legend_xmax,
                                   self.positioning.legend_ymax)

        #self.legend.SetNColumns(2)### EAI ADD
        #self.legend.SetColumnSeparation(0.1)
        self.legend.SetFillColor(0)
        self.legend.SetFillStyle(0)
        self.legend.SetBorderSize(0)
        self.legend.SetTextSize(0.03)##EAI from 0.03
        

        for component in self.components:
            ## Exclude empty histograms from the legend
            if component.event_yield == 0: continue
                
            if self.show_yields:
                if component.style.name == 'fill':
                    self.legend.AddEntry(component.nominal,
                                         '%s (%.1f)' % (component.name, component.event_yield),
                                         'F')
                elif component.style.name == 'line':
                    self.legend.AddEntry(component.nominal,
                                         '%s (%.1f)' % (component.name, component.event_yield),
                                         'L')
                else:
                    self.legend.AddEntry(component.nominal,
                                         '%s (%.1f)' % (component.name, component.event_yield),
                                         'LP')
            else:
                if component.style.name == 'fill':
                    self.legend.AddEntry(component.nominal,
                                         '',
                                         'F')
                elif component.style.name == 'line':
                    self.legend.AddEntry(component.nominal,
                                         '',
                                         'L')
                else:
                    self.legend.AddEntry(component.nominal,
                                         '',
                                         'LP')
        
        try:
            self.legend.AddEntry(self.error, '', 'F')
        except AttributeError:
            pass
                
        return


    ## -------------------------------------------- ##
    def draw_ratio(self):
        """
        Draws the ratio, to be called within the main draw method
        """

        numerator   = self.components[self.numerator_index]
        denominator = self.error

        ## Prepare ratio histogram
        self.ratio =  ROOT.TH1F('%s_ratio' % self.name,
                           '%s_ratio' % self.name,
                           numerator.nbins,
                           array.array('d', numerator.plot_binning))
        
        ## Figure out the ratio content and errors
        for i in range(1, numerator.nbins+1):
            num_content = numerator.nominal.GetBinContent(i)
            num_error   = numerator.nominal.GetBinError(i) #EMMA
            den_content = denominator.GetBinContent(i)
            den_error   = denominator.GetBinError(i) #EMMA
            
            ## Skip bins with empty denominator
            if den_content == 0:
                self.ratio.SetBinContent(i, -1)
                self.ratio.SetBinError(i, 0.0)
                continue
            
            ratio_content = num_content/den_content
            ratio_error   = math.sqrt((num_error/den_content)**2 + ((num_content*den_error)/(den_content**2))**2) #EMMA

            self.ratio.SetBinContent(i, ratio_content)
            self.ratio.SetBinError(i, ratio_error) # EMMA
            
        ## Apply style to ratio plot
        style.style1D['points'].apply(self.ratio)

        self.ratio_pad.cd()
        self.ratio.SetMinimum(0.01) 
        self.ratio.SetMaximum(1.99)
        self.ratio.Draw()
        
        ## Adjust ratio axes and range
        xaxis = self.ratio.GetXaxis()
        yaxis = self.ratio.GetYaxis()
        
        xaxis.SetTitle(self.label)
        xaxis.SetTitleOffset(1.0)
        xaxis.SetTitleSize(0.15)
        xaxis.SetLabelSize(0.12)
        xaxis.SetLabelOffset(0.015)
        xaxis.SetTickLength(0.055)
        
        yaxis.SetTitle('Data/Model')
        #yaxis.SetTitle('FS/AFII')
        yaxis.SetTitleOffset(0.5)
        yaxis.SetTitleSize(0.125)
        yaxis.SetLabelSize(0.12)
        yaxis.SetNdivisions(507)

        ## Show grid
        self.ratio_pad.SetGridy(2)
        
        ## Draw the ratio points
        self.ratio.Draw('SAME %s' % style.style1D['points'].draw_options)
        self.canvas.Update()
        self.canvas.cd()

        ## Cover the main pad 0
        box  = ROOT.TBox()
        box.SetFillColor(ROOT.kWhite)
        box.DrawBox(0.12, 0.32, 0.20, 0.37)

        ## Place a new 0
        latex = ROOT.TLatex()
        latex.SetNDC()
        latex.SetTextSize(0.045)
        latex.DrawLatex(0.17, 0.33, '0')


    ## -------------------------------------------- ##
    def draw(self):
        """
        Draw the entire thing,
        print to file
        """

        ## Prepare components
        self.prepare_components()

        ## Canvas
        
        if self.do_ratio:
            self.main_pad.cd()
        else:
            self.make_canvas()
            self.canvas.cd()
            
        ## Prepare the error histogram
        has_error = False
        
        for component in self.components:
            if component.stack:
                self.error = ROOT.TH1F('%s_error' % self.name,
                                       'stat. + sys.',
                                       component.nbins,
                                       array.array('d', component.plot_binning))
                has_error = True
                break

        ## First, draw the stack
        first = True
        first_component = None
        for i, component_i in enumerate(self.components):

            if component_i.stack:

                print '========================================='
                
                self.error.Add(component_i.nominal)

                print '-----------------------------------------'
                
                for j, component_j in enumerate(self.components):
                    if j>i and component_j.stack:
                        component_i.nominal.Add(component_j.nominal)

                component_i.apply_style(component_i.nominal)
                if first:
                    component_i.nominal.Draw('%s' % component_i.style.draw_options)
                    first_component = component_i
                    first = False
                else:
                    #               component_i.nominal.Draw('SAME %s' % component_i.style.draw_ratoptions)
                    component_i.nominal.Draw('SAME %s' % component_i.style.draw_options)

                    
        ## Then draw the error
        if has_error:
            style.style1D['error'].apply(self.error)
            self.error.SetFillColor(ROOT.TColor.GetColor(palette.darkred))
            self.error.Draw('SAME %s' % style.style1D['error'].draw_options) ###EMMA: EDITED OUT OF PLOTTING FOR NOW

        bin_max = -1
        maximum = -1
        
        ## Find the plot maximum (if there are any stacked histograms)
        if has_error:
            bin_max = self.error.GetMaximumBin()
            maximum = self.error.GetBinContent(bin_max) #+ self.error.GetBinError(bin_max)

        
        ## Then draw non-stacked histograms
        for component in self.components:
            if component.stack: continue

            bin_max = component.nominal.GetMaximumBin()
            this_maximum = component.nominal.GetBinContent(bin_max) #+ component.nominal.GetBinError(bin_max)
            if this_maximum > maximum:
                maximum = this_maximum

            component.apply_style(component.nominal)
                
            if first:
                component.nominal.Draw('%s' % component.style.draw_options)
                first_component = component
                first = False
            else:
                component.nominal.Draw('SAME %s' % component.style.draw_options)

                
        ## Set the plot y range
        if self.ylog:
            first_component.nominal.SetMaximum(1000*maximum)
            first_component.nominal.SetMinimum(0.9)
        else:
            first_component.nominal.SetMaximum(1.4*maximum)
        self.canvas.Update()

        
        ## Take care of the ratio business
        if self.do_ratio:
            self.draw_ratio()


        ## Make the legend
        self.make_legend()
        self.legend.Draw('SAME')

        
        ## Place labels
        latex = ROOT.TLatex()
        latex.SetNDC()
        latex.SetTextSize(self.positioning.plot_label_size(0.04))

        for lbl in self.text_labels:

            x, y = self.positioning.plot_label_offset(lbl[1], lbl[2])
            
            if lbl[0] == 'ATLAS':
                ROOT.ATLASLabel(x, y, self.positioning.plot_label_size(0.04), '', ROOT.kBlack)
                latex.DrawLatex(x+0.14, y, 'Internal')
            elif lbl[0][:4] == '#int':
                latex.SetTextSize(self.positioning.plot_label_size(0.032))
                latex.DrawLatex(x, y, '#int')
                latex.SetTextSize(self.positioning.plot_label_size(0.040))
                latex.DrawLatex(x+self.positioning.plot_label_size(0.02), y, lbl[0][4:])
            else:
                latex.DrawLatex(x, y, lbl[0])


        ## Redraw the axis
        self.main_pad.RedrawAxis()
                
        
        ## Print to file
        self.canvas.Print('%s%s.png' % (self.name, self.testing))
