from Tools.Groups import *
from Tools.Histogram import Histogram
import ROOT

list_of_groups = [WJets,
                  WZ,
                  WW,
                  ZZ,
                  ZJets,
                  #ttbar_allh,
                  #ttbar_dilep,
                  #ttbar_lepfil,
                  Top,
                  WH,
                  SingleTop]


## Instantiate Histogram(s)
nbins =100
bins_low = 0
bins_high = 100

h_tau1_pt = Histogram('h_tau1_pt', '#tau_{1} p_{T} ', nbins, bins_low, bins_high)

## Loop over groups
for group in list_of_groups:

    print group.name

    ## Instantiate TChain
    chain = ROOT.TChain('tau')

    ## Loop over the samples in the group and load in TChain
    for sample in group.samples:
        print '    ', sample.path
        chain.Add(sample.path)

    ## TChain Draw into a TH1F
    hist = ROOT.TH1F('tau1pt_%s' % group.name, 'tau1pt', nbins, bins_low, bins_high)
    chain.Draw('evtsel_tau1_pt>>tau1pt_%s' % group.name)
    ## Add TH1F to Histogram
    h_tau1_pt.add_filled(hist,
                         group.name,
                         group.plotting.color,
                         group.plotting.style,
                         group.plotting.stack)

## Histogram.draw() 

h_tau1_pt.draw()    
