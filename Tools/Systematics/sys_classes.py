from decorrelation_dictionaries import decorrelations
import ROOT, math

################################################
def size_of_stat(h):
    """
    Measures the relative size of the statistical error on the histogram
    """

    nbins = h.GetNbinsX()

    error = 0
    
    for i in range(1, nbins+1):
        error += h.GetBinError(i)**2

    error = math.sqrt(error)

    return error/h.GetSumOfWeights()



################################################
def strip_stat_error(h):
    """
    Creates a new histogram without statistical error
    """

    nbins = h.GetNbinsX()
    xaxis = h.GetXaxis()
    xlo   = xaxis.GetBinLowEdge(1)
    xhi   = xaxis.GetBinUpEdge(nbins)

    new_name = '{0}_nostat'.format(h.GetName())
    
    new_h = ROOT.TH1F(new_name, new_name, nbins, xlo, xhi)

    for i in range(1, nbins+1):
        new_h.SetBinContent(i, h.GetBinContent(i))
        new_h.SetBinError(i, 0)

    return new_h



################################################
def smooth_variation(nominal, variation):
    """
    smooth one variation (up and down)
    """

    key_name = variation.GetName()
    
    variation.Divide(nominal)
    variation.Smooth(1)
    tmp = strip_stat_error(variation)

    variation.Reset()
    variation.ResetStats()
    variation.Add(nominal)
    variation.Multiply(tmp)

    variation.Write(key_name, ROOT.TObject.kWriteDelete)



################################################
def norm_variation(nominal,variation):
    """
    returns a factor for the normalization variation of a given shape systematic
    """

    nominal_norm   = nominal.GetSumOfWeights()
    variation_norm = variation.GetSumOfWeights()

    if nominal_norm > 0.0 and variation_norm > 0.0:
        variation.Scale(nominal_norm/variation_norm)
        variation.Write(variation.GetName(), ROOT.TObject.kWriteDelete)
        return variation_norm/nominal_norm
    else:
        return 1.0



################################################
def test_variation_significance(sumbkg, lo, hi):
    """
    test the significance of the variation bin by bin
    """

    variation_is_significant = False
    
    nbins = sumbkg.GetNbinsX()

    for i in range(1, nbins+1):
        if sumbkg.GetBinError(i) > 0.0:
            significance = abs(hi.GetBinContent(i) - lo.GetBinContent(i))/sumbkg.GetBinError(i)
            if significance > 0.1:
                variation_is_significant = True

    return variation_is_significant



################################################
def symmetrize_variations(nominal, lo, hi):
    """
    Symmetrize the variation in each bin
    """
    nbins = nominal.GetNbinsX()

    for i in range(1, nbins+1):
        nom_content = nominal.GetBinContent(i)
        nom_error   = nominal.GetBinError(i)

        hi_content  = hi.GetBinContent(i)
        hi_error    = hi.GetBinError(i)

        lo_content  = lo.GetBinContent(i)
        lo_error    = lo.GetBinError(i)

        hi_var = abs(nom_content - hi_content)
        lo_var = abs(nom_content - lo_content)

        if hi_var > lo_var:
            lo_content = 2*nom_content - hi_content
            lo_error   = 2*nom_error + hi_error

            lo.SetBinContent(i, lo_content)
            lo.SetBinError(i, lo_error)
        else:
            hi_content = 2*nom_content - lo_content
            hi_error   = 2*nom_error + lo_error

            hi.SetBinContent(i, hi_content)
            hi.SetBinError(i, hi_error)

    lo.Write(lo.GetName(), ROOT.TObject.kWriteDelete)
    hi.Write(hi.GetName(), ROOT.TObject.kWriteDelete)



################################################
def partial_symmetrize_variations(nominal, lo, hi):
    """
    Make sure no bin pulls the same way for the up/down variations
    """

    nbins = nominal.GetNbinsX()
    
    for i in range(1, nbins+1):
        nom_content = nominal.GetBinContent(i)
        hi_content  = hi.GetBinContent(i)
        lo_content  = lo.GetBinContent(i)

        hi_delta = hi_content - nom_content
        lo_delta = lo_content - nom_content

        if hi_delta*lo_delta > 0:
            if abs(hi_delta) > abs(lo_delta):
                lo.SetBinContent(i, nom_content)

            if abs(lo_delta) > abs(hi_delta):
                hi.SetBinContent(i, nom_content)

    lo.Write(lo.GetName(), ROOT.TObject.kWriteDelete)
    hi.Write(hi.GetName(), ROOT.TObject.kWriteDelete)




################################################
def partial_symmetrize_overall(lo, hi):
    """
    Make sure both lo and hi variations do not pull in the same direction
    """

    hi_delta = hi - 1.0
    lo_delta = lo - 1.0

    if hi_delta*lo_delta > 0:
        if abs(hi_delta) > abs(lo_delta):
            lo = 1.0
        else:
            hi = 1.0

    return lo, hi

    


    
################################################
def quad(variations):
    """
    Returns the quadrature combination of the list of variations provided
    """

    hi_total = 0
    lo_total = 0

    for var in variations:
        lo_total += abs(var[0] - 1.0)**2
        hi_total += abs(var[1] - 1.0)**2

    return 1.0-math.sqrt(lo_total), 1.0+math.sqrt(hi_total)


################################################
def max_variation(nominal, lo, hi):
    """
    Identify the maximum variation and return the value in percentage
    """
    nbins = nominal.GetNbinsX()

    max_variation = 0
    
    for i in range(1, nbins+1):
        nom_content = nominal.GetBinContent(i)
        hi_content  = hi.GetBinContent(i)
        lo_content  = lo.GetBinContent(i)

        if nom_content == 0: continue
        
        var_hi = abs(1.0 - hi_content/nom_content)
        var_lo = abs(1.0 - lo_content/nom_content)

        if var_hi > max_variation:
            max_variation = var_hi

        if var_lo > max_variation:
            max_variation = var_lo

    return max_variation*100


################################################
def max_var_over_error(h1, h2):
    """
    Compute the maximum variation over the bin error, 
    given that h1 has a larger total stat uncertainty,
    where h1 and h2 are the nominal and either lo or hi variation
    Return the value in a percentage
    """

    nbins = h1.GetNbinsX()

    maxvar_over_error = 0

    for i in range(1, nbins+1):
        h1_content = h1.GetBinContent(i)
        h2_content = h2.GetBinContent(i)

        if h1_content == 0: continue

        var = (abs(h1_content - h2_content))/h1.GetBinError(i)

        if var > maxvar_over_error:
            maxvar_over_error = var

    #return maxvar_over_error*100
    return maxvar_over_error




        

        

            



################################################
class SysSet:
    """
    A class to contain a complete set of systematics
    """
    
    ## ------------------------------------------- ##
    def __init__(self, name):
        """
        Constructor
        """

        self.name = name
        self.channels = []
        self.files = {}



    ## ------------------------------------------- ##
    def open_files(self, limit_histograms_file_name, categories): ## categories = ['wh', 'zh']
        """
        Open the files hosting the histograms
        """
        print 'Opening', limit_histograms_file_name, '...'
        ff = ROOT.TFile(limit_histograms_file_name, 'UPDATE')
        for category in categories:
            self.files[category] = ff



    ## ------------------------------------------- ##
    def add(self, limit_channel):
        """
        Add one limit channel
        """

        self.channels.append(limit_channel)



    ## ------------------------------------------- ##
    def get_shape(self, category, control_region, sample):
        """
        Return a list with all the shape systematics for one particular sample/category/control_region
        """

        for ch in self.channels:
            if ch.category == category and ch.control_region == control_region:
                for s in ch.samples:
                    if s.name == sample:
                        return s.shape



    ## ------------------------------------------- ##
    def get_shape_for_algo(self, categories, sample):
        """
        Returns shape systematics in a format appropriate for Algortihm.pyx
        """

        sys_list = []

        for ch in self.channels:
            if ch.category in categories:
                for s in ch.samples:
                    if s.name == sample:
                        for sys in s.shape:
                            already_in_it = False
                            for i in sys_list:
                                if i[0] == '%s_DOWN' % decorrelations.get(sys.name):
                                    already_in_it = True
                            if not already_in_it:
                                sys_list.append(('%s_DOWN' % decorrelations.get(sys.name), ch.category))
                                sys_list.append(('%s_UP' % decorrelations.get(sys.name), ch.category))

        return sys_list


    ## ------------------------------------------- ##
    def get_shape_for_plots(self, category, sample):
        """
        Returns a list of shape systematics for plots
        """

        sys_list = []

        for ch in self.channels:
            if ch.category == category:
                for s in ch.samples:
                    if s.name == sample:
                        for sys in s.shape:
                            if not sys.activated: continue
                            sys_name = decorrelations.get(sys.name)
                            if not sys_name in sys_list:
                                sys_list.append(sys_name)

        return sys_list


    ## ------------------------------------------- ##
    def get_overall(self, category, control_region, sample):
        """
        Return a list with all the shape systematics for one particular sample/category/control_region
        """

        for ch in self.channels:
            if ch.category == category and ch.control_region == control_region:
                for s in ch.samples:
                    if s.name == sample:
                        return s.overall


                    
    ## ------------------------------------------- ##
    def get_overall_for_plots(self, category, sample):

        sys_dict = {}
        
        for ch in self.channels:
            if ch.category == category:
                for s in ch.samples:
                    if s.name == sample:
                        for sys in s.overall:
                            if not sys.activated: continue
                            sys_name = sys.name
                            delta = abs(float(sys.hi) - float(sys.lo))
                            if (not sys_name in sys_dict.keys()):
                                sys_dict[sys_name] = (float(sys.lo), float(sys.hi))
                            else:
                                old_delta = abs(sys_dict[sys_name][1] - sys_dict[sys_name][0])
                                if delta > old_delta:
                                    sys_dict[sys_name] = (float(sys.lo), float(sys.hi))

        return sys_dict.values()
    


    ## ------------------------------------------- ##
    def print_all(self):
        """
        Print all the systematics
        """

        for ch in self.channels:

            print
            print '='*60
            print ch.category, ch.control_region
            print '-'*60
            
            for s in ch.samples:

                print '    Sample', s.name
                
                for ov in s.overall:
                    print '        {0:<12} {1:<36} {2:<9} {3:<9}'.format('OverallSys', 
                                                                         'n=%s' % ov.name, 
                                                                         'l=%s' % ov.lo,
                                                                         'h=%s' % ov.hi)

                
                for sh in s.shape:
                    print '        {0:<12} {1:<36} {2:<36} {3:<36}'.format('HistoSys', 
                                                                           'n=%s' % sh.name, 
                                                                           'l=%s' % sh.lo,
                                                                           'h=%s' % sh.hi)



    ## ------------------------------------------- ##
    def print_all_unique(self):
        """
        Print all the systematics
        """

        systs = []
        
        for ch in self.channels:
            
            for s in ch.samples:

                print '    Sample', s.name
                
                for ov in s.overall:
                    if not 'ov ' + ov.name in systs:
                        systs.append('ov ' + ov.name)

                
                for sh in s.shape:
                    if not 'sh ' + sh.name in systs:
                        systs.append('sh ' + sh.name)


                        
        print
        print 'Systematics figuring in the xmls:'
        print '='*60
        for sys in sorted(systs):
            print '    %s' % sys

                    


    ## ------------------------------------------- ##
    def print_shape(self):
        """
        Print shape systematics alone
        """

        shape_sys = {}
        
        for ch in self.channels:

            print
            print '='*60
            print ch.category, ch.control_region
            print '-'*60
            
            for s in ch.samples:

                if len(s.shape) == 0: continue
                
                print '    Sample', s.name
                
                for sh in s.shape:
                    print '        {0:<12} {1:<36} {2:<36} {3:<36}'.format('HistoSys', 
                                                                           'n=%s' % sh.name, 
                                                                           'l=%s' % sh.lo,
                                                                           'h=%s' % sh.hi)

                    if not sh.name in shape_sys.keys():
                        shape_sys[sh.name] = ['%s-%s-%s' % (s.name, ch.category, ch.control_region)]
                    else:
                        if not s.name in shape_sys[sh.name]:
                            shape_sys[sh.name].append('%s-%s-%s' % (s.name, ch.category, ch.control_region))

        keys = sorted(shape_sys.keys())

        print
        print
        
        for key in keys:
            print '-='*25
            print key
            print
            shape_sys[key].sort()
            for sample in shape_sys[key]:
                print '    %s' % sample



    ## ------------------------------------------- ##
    def reset(self):
        """
        Reset all systematics to activated
        """

        for ch in self.channels:
            for s in ch.samples:
                for ov in s.overall:
                    ov.activated = True
                for sh in s.shape:
                    sh.activated = True



    ## ------------------------------------------- ##
    def quadrature_combination(self):
        """
        Make a quadrature combination of the muon and electron efficiency systematics
        """

        print
        print '='*60
        print 'Quadrature combinations ...'

        for ch in self.channels:

            f = self.files[ch.category]
            f.cd()

            for s in ch.samples:

                sample_name = s.name
                if s.name == None:
                    sample_name = 'QCD'
                if 'AntitauEvents' in s.name: continue
                
                #nominal_name       = '{0}_{1}_{2}'.format(ch.category, ch.control_region, sample_name)
                nominal_name       = '{0}_{1}'.format(ch.category, sample_name)
                print '    ', nominal_name
                nominal            = f.Get(nominal_name)
                nominal_yield      = nominal.GetSumOfWeights()
                print '    ', nominal_name


                ### Combine the EL EFF systematics: EL_ID, EL_ISO, EL_TRIG
                ### Combine the EL SCALE systematics: EL_ZEE, EL_R12, EL_PS, EL_LOWPT
                ### Combine the MU EFF systematics: Mu_ID, MU_ISO, MU_TRIG

                electron_efficiencies = []
                electron_scales       = []
                muon_efficiencies     = []
                
                for sh in s.shape:

                    if ('ATLAS_EL_EFF' in sh.name):

                        sys_histogram_name = decorrelations.get(sh.name)
                    
                        hi_name = nominal_name + '_' + sys_histogram_name + '_UP'
                        hi = f.Get(hi_name)
                        hi_yield = hi.GetSumOfWeights()
                    
                        lo_name = nominal_name + '_' + sys_histogram_name + '_DOWN'
                        lo = f.Get(lo_name)
                        lo_yield = lo.GetSumOfWeights()

                        electron_efficiencies.append((lo_yield/nominal_yield, hi_yield/nominal_yield))
                        print '        {0:<36}: {1:<5.3f},     {2:<36}: {3:5.3f}'.format(hi_name, hi_yield/nominal_yield, lo_name, lo_yield/nominal_yield)

                        sh.activated = False
                        sh.cancelled = True

                    if ('ATLAS_EL_SCALE' in sh.name):

                        sys_histogram_name = decorrelations.get(sh.name)
                    
                        hi_name = nominal_name + '_' + sys_histogram_name + '_UP'
                        hi = f.Get(hi_name)
                        hi_yield = hi.GetSumOfWeights()
                    
                        lo_name = nominal_name + '_' + sys_histogram_name + '_DOWN'
                        lo = f.Get(lo_name)
                        lo_yield = lo.GetSumOfWeights()

                        electron_scales.append((lo_yield/nominal_yield, hi_yield/nominal_yield))
                        print '        {0:<36}: {1:<5.3f},     {2:<36}: {3:5.3f}'.format(hi_name, hi_yield/nominal_yield, lo_name, lo_yield/nominal_yield)

                        sh.activated = False
                        sh.cancelled = True

                    if ('ATLAS_MU_EFF' in sh.name):

                        sys_histogram_name = decorrelations.get(sh.name)
                    
                        hi_name = nominal_name + '_' + sys_histogram_name + '_UP'
                        hi = f.Get(hi_name)
                        hi_yield = hi.GetSumOfWeights()
                    
                        lo_name = nominal_name + '_' + sys_histogram_name + '_DOWN'
                        lo = f.Get(lo_name)
                        lo_yield = lo.GetSumOfWeights()

                        muon_efficiencies.append((lo_yield/nominal_yield, hi_yield/nominal_yield))
                        print '        {0:<36}: {1:<5.3f},     {2:<36}: {3:5.3f}'.format(hi_name, hi_yield/nominal_yield, lo_name, lo_yield/nominal_yield)

                        sh.activated = False
                        sh.cancelled = True

                el_lo, el_hi = quad(electron_efficiencies)
                els_lo, els_hi = quad(electron_scales)
                mu_lo, mu_hi = quad(muon_efficiencies)

                print '            ATLAS_EL_EFF   : lo=%.3f, hi=%.3f' % (el_lo, el_hi)
                print '            ATLAS_EL_SCALE : lo=%.3f, hi=%.3f' % (els_lo, els_hi)
                print '            ATLAS_MU_EFF   : lo=%.3f, hi=%.3f' % (mu_lo, mu_hi)

                s.add_overall('ATLAS_EL_SCALE', els_lo, els_hi)
                
                #if s.name == 'Ztt':
                    #s.add_overall('ATLAS_EL_EFF_Emb', el_lo, el_hi)
                    #s.add_overall('ATLAS_MU_EFF_Emb', mu_lo, mu_hi)
                #else:
                s.add_overall('ATLAS_EL_EFF', el_lo, el_hi)
                s.add_overall('ATLAS_MU_EFF', mu_lo, mu_hi)
                




    ## ------------------------------------------- ##
    def symmetrize(self):
        """
        symmetrize specific shape systematics
        """

        print
        print '='*60
        print 'Symmetrizing shape systematics ...'

        for ch in self.channels:

            f = self.files[ch.category]
            f.cd()

            for s in ch.samples:

                sample_name = s.name
                if s.name == None:
                    sample_name = 'QCD'
                
                nominal_name       = '{0}_{1}'.format(ch.category, sample_name)
                nominal            = f.Get(nominal_name)

                for sh in s.shape:

                    if not sh.name == 'ATLAS_JER_2012': continue

                    sys_histogram_name = decorrelations.get(sh.name)
                    
                    hi_name = nominal_name + '_' + sys_histogram_name + '_UP'
                    hi = f.Get(hi_name)
                    
                    lo_name = nominal_name + '_' + sys_histogram_name + '_DOWN'
                    lo = f.Get(lo_name)

                    print 'symmetrizing %s ...' % hi_name.replace('_UP', '')

                    symmetrize_variations(nominal, lo, hi)



    ## ------------------------------------------- ##
    def partial_symmetrize(self):
        """
        symmetrize specific shape systematics
        """

        print
        print '='*60
        print 'Partially symmetrizing shape systematics ...'

        for ch in self.channels:

            f = self.files[ch.category]
            f.cd()

            for s in ch.samples:

                sample_name = s.name
                if s.name == None:
                    sample_name = 'QCD'
                
                nominal_name       = '{0}_{1}_{2}'.format(ch.category, ch.control_region, sample_name)
                nominal            = f.Get(nominal_name)

                for sh in s.shape:

                    sys_histogram_name = decorrelations.get(sh.name)
                    
                    hi_name = nominal_name + '_' + sys_histogram_name + '_UP'
                    hi = f.Get(hi_name)
                    
                    lo_name = nominal_name + '_' + sys_histogram_name + '_DOWN'
                    lo = f.Get(lo_name)

                    print 'partially symmetrizing %s ...' % hi_name.replace('_UP', '')

                    partial_symmetrize_variations(nominal, lo, hi)



    ## ------------------------------------------- ##
    def norm_to_overall(self):
        """
        Check the effect on the normalization of the shape systematics and move over to overall
        systematics while adjusting the shape systematics normalization to that of the nominal
        """

        print
        print '='*60
        print 'Dealing with normalization of shape systematics ...'
        
        for ch in self.channels:

            f = self.files[ch.category]
            f.cd()

            samples_to_pop=[]
            
            for i, s in enumerate(ch.samples):

                sample_name = s.name
                if s.name == None:
                    sample_name = 'QCD'
                
                #nominal_name       = '{0}_{1}_{2}'.format(ch.category, ch.control_region, sample_name)
                nominal_name       = '{0}_{1}'.format(ch.category, sample_name)
                print '    ', nominal_name
                nominal            = f.Get(nominal_name)
                if not nominal:
                    samples_to_pop.append(i)
                    print '        ===> This sample will be removed, no valid histogram.'

                for sh in s.shape:

                    if sh.cancelled: continue

                    sys_histogram_name = decorrelations.get(sh.name)

                    hi_name = nominal_name + '_' + sys_histogram_name + '_UP'
                    hi = f.Get(hi_name)
                    
                    lo_name = nominal_name + '_' + sys_histogram_name + '_DOWN'
                    lo = f.Get(lo_name)

                    lo_norm = norm_variation(nominal, lo)
                    hi_norm = norm_variation(nominal, hi)
                    ov_weight = sh.weight


                    old_lo = -1
                    old_hi = -1
                    
                    ## Propagate to the normalization systematics
                    already_a_norm = False
                    for ov in s.overall:
                        if ov.name == sh.name:
                            old_lo = float(ov.lo)
                            old_hi = float(ov.hi)
                            ov.lo = lo_norm
                            ov.hi = hi_norm
                            ov.weight = ov_weight
                            already_a_norm = True
                            break

                    if not already_a_norm:
                       s.add_overall(sh.name, lo_norm, hi_norm, ov_weight)

                    if ch.onebin:
                        sh.activated = False

                    if old_lo > 0 and old_hi > 0:
                        print '         {0:<35} lo : {1:<5.3f} ({2:<5.3f})   hi : {3:<5.3f} ({4:<5.3f})'.format(sys_histogram_name, lo_norm, old_lo, hi_norm, old_hi)
                    else:
                        print '         {0:<35} lo : {1:<5.3f} (-----)   hi : {2:<5.3f} (-----)    {3:<5.3f}'.format(sys_histogram_name, lo_norm, hi_norm, ov.weight)

            ## Pop samples that don't figure in the workspace
            for i in reversed(samples_to_pop):
                ch.samples.pop(i)



    ## ------------------------------------------- ##
    def prune(self, criteria='Chi2', threshold=0.95):
        """
        deactivate shape systematics 
        """

        print
        print '='*60
        print 'Pruning shape systematics ...'

        for ch in self.channels:

            if ch.onebin: continue

            f = self.files[ch.category]
            f.cd()

            for s in ch.samples:

                sample_name = s.name
                
                nominal_name       = '{0}_{1}'.format(ch.category, sample_name)
                nominal            = f.Get(nominal_name)
                print '    ', nominal_name
                nominal_stat_error = size_of_stat(nominal)
                nominal_norm = nominal.GetSumOfWeights()

                for sh in s.shape:
                    
                    if sh.weight: continue

                    sys_histogram_name = decorrelations.get(sh.name)
                    
                    hi_name = nominal_name + '_' + sys_histogram_name + '_UP'
                    hi = f.Get(hi_name)
                    hi_stat_error = size_of_stat(hi)
                    hi_norm = hi.GetSumOfWeights()
                    hi.Scale(nominal_norm/hi_norm)
                    
                    lo_name = nominal_name + '_' + sys_histogram_name + '_DOWN'
                    lo = f.Get(lo_name)
                    lo_stat_error = size_of_stat(lo)
                    lo_norm = lo.GetSumOfWeights()
                    lo.Scale(nominal_norm/lo_norm)

                    test_hi = 1.0
                    test_lo = 1.0
                    

                    if criteria == 'Chi2':
                        ROOT.gErrorIgnoreLevel = ROOT.kWarning #This suppresses the Chi2Test info messages about having < 10 effective events...
                        if nominal_stat_error > hi_stat_error:
                            test_hi = nominal.Chi2Test(strip_stat_error(hi), 'WW')
                        else:
                            test_hi = hi.Chi2Test(strip_stat_error(nominal), 'WW')

                        if nominal_stat_error > lo_stat_error:
                            test_lo = nominal.Chi2Test(strip_stat_error(lo), 'WW')
                        else:
                            test_lo = lo.Chi2Test(strip_stat_error(nominal), 'WW')
                            

                    ## Restore normalizations
                    hi.Scale(hi_norm/nominal_norm)
                    lo.Scale(lo_norm/nominal_norm)

                    result = (test_hi < threshold or test_lo < threshold)
                    sh.activated = result
                    print '         {0:<35} lo : {1:<5.2f}   hi : {2:<5.2f}   keep : {3}'.format(sys_histogram_name, test_lo, test_hi, result)



    ## ------------------------------------------- ##
    def prune_shape_10(self, threshold = 0.1):
        """
        Prune shape systematics where max(bin variation)/bin_stat_error < 10%
        """

        print
        print '='*60
        print 'Pruning shapes with 10 percent bin test ...'

        for ch in self.channels:

            f = self.files[ch.category]
            f.cd()

            for s in ch.samples:
                
                sample_name = s.name

                nominal_name       = '{0}_{1}'.format(ch.category, sample_name)
                nominal            = f.Get(nominal_name)
                print '    ', nominal_name
                nominal_stat_error = size_of_stat(nominal)

                for sh in s.shape:

                    if not sh.activated: continue
                    if sh.cancelled: continue
                    if sh.weight: continue

                    sys_histogram_name = decorrelations.get(sh.name)

                    hi_name = nominal_name + '_' + sys_histogram_name + '_UP'
                    hi = f.Get(hi_name)
                    hi_stat_error = size_of_stat(hi)
                    #hi_norm = hi.GetSumOfWeights()

                    lo_name = nominal_name + '_' + sys_histogram_name + '_DOWN'
                    lo = f.Get(lo_name)
                    lo_stat_error = size_of_stat(lo)
                    #lo_norm = lo.GetSumOfWeights()

                    if nominal_stat_error > hi_stat_error:
                        diff_up = max_var_over_error(nominal, hi)
                    else:
                        diff_up = max_var_over_error(hi, nominal)
                        if hi_stat_error == 0:
                            if diff_up != 0:
                                sh.activated = True
                                break
                        
                    if nominal_stat_error > lo_stat_error:
                        diff_down = max_var_over_error(nominal, lo)
                    else:
                        diff_down = max_var_over_error(lo, nominal)
                        if lo_stat_error == 0:
                            if diff_down != 0:
                                sh.activated = True
                                break
                        

                    if max(diff_up, diff_down) > threshold:
                        sh.activated = True

                    else:
                        sh.activated = False

                    print '         {0:<35} diff_up : {1:<5.2f}   diff_down : {2:<5.2f}   keep : {3}'.format(sys_histogram_name, diff_up, diff_down, sh.activated)












    ## ------------------------------------------- ##
    def smooth(self):
        """
        Smooth shape systematics
        """

        print
        print '='*60
        print 'Smoothing the shape systematics ...'
        
        for ch in self.channels:

            if ch.onebin: continue
            
            f = self.files[ch.category]
            f.cd()

            for s in ch.samples:

                sample_name = s.name
                if s.name == None:
                    sample_name = 'QCD'
                
                nominal_name       = '{0}_{1}_{2}'.format(ch.category, ch.control_region, sample_name)
                nominal            = f.Get(nominal_name)

                print '    ', nominal_name

                for sh in s.shape:

                    sys_histogram_name = decorrelations.get(sh.name)

                    print '        smoothing {0} ...'.format(sys_histogram_name)
                    
                    hi_name = nominal_name + '_' + sys_histogram_name + '_UP'
                    hi = f.Get(hi_name)
                    
                    lo_name = nominal_name + '_' + sys_histogram_name + '_DOWN'
                    lo = f.Get(lo_name)

                    smooth_variation(nominal, lo)
                    smooth_variation(nominal, hi)



    ## ------------------------------------------- ##
    def prune_significance(self):
        """
        Prune according to the significance of the variations
        """

        print
        print '='*60
        print 'Pruning the remaining systematics according to significance of variation ...'
        
        for ch in self.channels:

            f = self.files[ch.category]
            f.cd()

            for s in ch.samples:

                sample_name = s.name
                if s.name == None:
                    sample_name = 'QCD'

                nominal_name      = '{0}_{1}_{2}'.format(ch.category, ch.control_region, sample_name)
                sumbkg_name       = '{0}_{1}_sumbkg'.format(ch.category, ch.control_region)
                sumbkg            = f.Get(sumbkg_name)

                print '    ', sumbkg_name.replace('sumbkg', sample_name)

                for sh in s.shape:

                    if not sh.activated: continue

                    sys_histogram_name = decorrelations.get(sh.name)
                    
                    hi_name = nominal_name + '_' + sys_histogram_name + '_UP'
                    hi = f.Get(hi_name)
                    
                    lo_name = nominal_name + '_' + sys_histogram_name + '_DOWN'
                    lo = f.Get(lo_name)

                    sh.activated = test_variation_significance(sumbkg, lo, hi)

                    print '        significance {0:<45} : keep: {1}'.format(hi_name.replace('_UP', ''), sh.activated)



    ## ------------------------------------------- ##
    def prune_05_percent(self):
        """
        Prune shape and overall systematics that don't make it above 0.5% variations
        """

        print
        print '='*60
        print 'Pruning the remaining systematics with the 0.5% threshold ...'
        
        for ch in self.channels:

            f = self.files[ch.category]
            f.cd()

            for s in ch.samples:

                sample_name = s.name
                
                nominal_name       = '{0}_{1}'.format(ch.category, sample_name)
                nominal            = f.Get(nominal_name)

                print '    ', nominal_name

                print '        == overalls =='
                for ov in s.overall:

                    if not ov.activated: continue
                    if ov.weight: continue
                    if ov.cancelled: continue

                    ov_name = ov.name

                    #print 'High diff is %.3f' % (100*abs(1.0-ov.hi))
                    #print 'Low diff is %.3f' % (100*abs(1.0-ov.lo))

                    if (100*abs(1.0-ov.hi) < 0.5) and (100*abs(1.0-ov.lo) < 0.5):
                        ov.activated = False

                    if math.isnan(ov.hi) or math.isnan(ov.lo):
                        ov.activated = False

                    ov.lo, ov.hi = partial_symmetrize_overall(ov.lo, ov.hi)

                    #print '        0.5% threshold {0:<45} : keep: {1}'.format(hi_name.replace('_UP', ''), ov.activated)
                    print '        0.5% threshold {0:<45} : keep: {1}'.format(ov_name.replace('_UP', ''), ov.activated)


                #                print '        == shapes =='
#                for sh in s.shape:
#
#                    if not sh.activated: continue
#                    if sh.weight: continue
#                    if sh.cancelled: continue
#
#                    sys_histogram_name = decorrelations.get(sh.name)
#
#                    hi_name = nominal_name + '_' + sys_histogram_name + '_UP'
#                    hi = f.Get(hi_name)
#                    
#                    lo_name = nominal_name + '_' + sys_histogram_name + '_DOWN'
#                    lo = f.Get(lo_name)
#
#                    if max_variation(nominal, lo, hi) < 0.5: #max variation returns a real percentage
#                        sh.activated = False
#
#                    print '        0.5% threshold {0:<45} : keep: {1}'.format(hi_name.replace('_UP', ''), sh.activated)
                        

                


        

#################################################
class LimitChannel:
    """
    A class to group the information relevant to a limit channel
    """

    ## ------------------------------------------- ##
    def __init__(self,
                 category,
                 control_region,
                 path=''):
        """
        Constructor
        """

        self.category = category
        self.control_region = control_region
        self.path = path
        self.onebin = False

        self.samples = []


    ## ------------------------------------------- ##
    def add(self, sample):
        """
        Add a sample
        """

        self.samples.append(sample)



#################################################
class Sys:
    """
    A class to house the data for a single systematic
    """

    ## ------------------------------------------- ##
    def __init__(self, name, lo, hi, weight=False):
        """
        Constructor
        """

        self.name      = name
        self.lo        = lo
        self.hi        = hi
        self.activated = True
        self.cancelled = False
        self.weight    = weight



#################################################
class Sample:
    """
    A class to house the systematics for a Sample
    """

    ## ------------------------------------------- ##
    def __init__(self, name):
        """
        Constructor
        """

        self.name = name
        
        self.overall = []
        self.shape   = []



    ## ------------------------------------------- ##
    def add_shape(self, name, weight=False):
        """
        Add a shape systematic
        """

        self.shape.append(Sys(name, '%s_DOWN' % name, '%s_UP' % name, weight))



    ## ------------------------------------------- ##
    def add_overall(self, name, lo, hi, weight=False):
        """
        Add an overall systematic
        """

        self.overall.append(Sys(name, lo, hi, weight))
