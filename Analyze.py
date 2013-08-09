from Tools.Groups import *
from Tools.Histogram import Histogram
from plotting import plots # "from blank" where blank is the name of the python file blank.py and you can import anything that is defined with an equals sign. It can be a class or a variable
import ROOT

## Setting up the ATLAS style
root_functions = ROOT.gROOT.GetListOfFunctions()
#ROOT.gSystem.Load('MyClass_C.so')
#m = ROOT.MyClass()
if not root_functions.Contains('ATLASLabel'):
    ROOT.gROOT.LoadMacro('AtlasStyle.C')
    ROOT.gROOT.LoadMacro('AtlasLabels.C')
    ROOT.SetAtlasStyle()
    

    list_of_groups = [#WJets,
#ZJets,
                  #ttbar_allh,
                  #ttbar_dilep,
                  #ttbar_lepfil,
                  #Top,
                  #WH,
                  #SingleTop,
                  #ZZ,
                  #WW,
                  #WZ,
                  WH]


## Loop over groups
for group in list_of_groups:

    print 'Plotting %s ...' % group.name

    ## Instantiate TChain
    chain = ROOT.TChain('tau')

    ## Loop over the samples in the group and load in TChain
    for sample in group.samples:
        #print '    ', sample.path
        chain.Add(sample.path)
        
    for entry in plots:
        th1f_name = '%s_%s' % (entry.variable,	group.name)

        th1f = ROOT.TH1F(th1f_name, group.plotting.legendLabel, entry.nbins, entry.binlow, entry.binhigh)
        chain.Draw('%s*%f>>%s' % (entry.variable, entry.factor, th1f_name), 'evtsel_weight*0.02*(evtsel_is_WHlephad && (evtsel_is_mu || evtsel_is_el))')
        print 'Weighted number of entries after just SLT trigger for WHlh is %.3f' % th1f.GetSumOfWeights()

        #        chain.Draw('%s*%f>>%s' % (entry.variable, entry.factor, th1f_name), 'evtsel_weight*0.02*evtsel_bjet_weight*(evtsel_is_WHlephad && (evtsel_is_mu || evtsel_is_el) && evtsel_passes_MV1)')
        #print 'Number of entries %d' % th1f.GetEntries()
        #print 'Weighted number of entries after trigger+bjet veto is %.3f' % th1f.GetSumOfWeights()

        #chain.Draw('%s*%f>>%s' % (entry.variable, entry.factor, th1f_name), 'evtsel_weight*0.02*evtsel_bjet_weight*(evtsel_is_WHlephad && (evtsel_is_mu || evtsel_is_el) && evtsel_passes_MV1 && (evtsel_tau1_pt>50000))')
        #print 'Weighted number of entries after trigger+bjetveto+taupt is %.3f' % th1f.GetSumOfWeights()
        
        ## Add TH1F to Histogram
        entry.histogram.add_filled(th1f,
                                   group.name,
                                   group.plotting.color,
                                   group.plotting.style,
                                   group.plotting.stack)
    

## Histogram.draw() 
for entry in plots:
	entry.histogram.add_label('ATLAS', 0.23, 0.9)
	entry.histogram.add_label('#intL dt = 20.3fb^{-1}', 0.65, 0.89)
	entry.histogram.add_label('#sqrt{s} = 8 TeV', 0.67, 0.83)
    
	entry.histogram.ylog = entry.logplot
	
	
	entry.histogram.show_yields = True
	
	entry.histogram.draw()
