#from Tools import Subsets_with_a_super_long_name as ss
from Tools import Subsets
from Tools.Supergroups import *
#from Tools.Groups import *
from Tools.Histogram import Histogram
from plotting import plots #"from blank" where blank is the name of the python file blank.py and you can import anything that is defined with an equals sign. It can be a class or a variable
from Tools import palette
import ROOT
import math



## Setting up the ATLAS style
root_functions = ROOT.gROOT.GetListOfFunctions()
#ROOT.gSystem.Load('MyClass_C.so')
#m = ROOT.MyClass()
if not root_functions.Contains('ATLASLabel'):
    ROOT.gROOT.LoadMacro('AtlasStyle.C')
    ROOT.gROOT.LoadMacro('AtlasLabels.C')
    ROOT.SetAtlasStyle()
    

list_of_supergroups = [
    Data,
    WeJets,
    WmJets,
    WtJets,
    ZeeJets,
    ZmmJets,
    ZttJets,
    tt,
    SingleTop,
    ZZ,
    WW,
    WGamma,
    WZ,
#QCD
    #WH
    #ZH
    ]

###Subsets definition
WH = Subsets.wh_os
WHSSS = Subsets.wh_sss
ZH = Subsets.zh_os
TT = Subsets.tt_cr
WJets = Subsets.w_cr
ZJets = Subsets.z_cr
QCD_CR = Subsets.qcd
QCD_SSS = QCD_CR + WHSSS
QCD_OS  = QCD_CR + WH

master_subset = WH + QCD_CR

regions = [
    [QCD_OS,  0.0, []],
    [QCD_SSS, 0.0, []],
    # [WH,      0.0, []],
    # [TT,      0.0, []]
]

####Loop over regions
for region in regions:

    ###Loop over plots
    for entry in plots:

        QCD_histo = ROOT.TH1F('QCD_%s' % region[0].name, '', entry.nbins, entry.binlow, entry.binhigh)
        region[2].append(QCD_histo)

        ##Loop over supergroups
        for supergroup in list_of_supergroups:
            print 'Plotting %s ...' % supergroup.name
            th1f_total_name = '%s_%s_sg' % (entry.variable, supergroup.name)
            th1f_total = ROOT.TH1F(th1f_total_name, supergroup.legendLabel, entry.nbins, entry.binlow, entry.binhigh)
            th1f_total.Sumw2()

            for group in supergroup.groups:
                print 'Plotting %s ...' % group.name
                th1f_name = '%s_%s_g' % (entry.variable, group.name)
                th1f = ROOT.TH1F(th1f_name, supergroup.legendLabel, entry.nbins, entry.binlow, entry.binhigh)
                th1f.Sumw2()

                #Instantiate TChain
                chain = ROOT.TChain('tau')

                for sample in group.samples:
                    #print '    ', sample.path
                    chain.Add(sample.path)

                ## For R_QCD calculation
                sign = -1
                    
                cut1 = 'evtsel_weight*0.02'
                if group.classification == 'DATA':
                    cut1 = 'evtsel_weight'
                    sign = 1
                #if supergroup.name == 'QCD':
                #    region[0] = region[0] + QCD_CR

                cut2 = cut1 + '*' + (region[0] + supergroup.subset).string() 

                chain.Draw('%s*%f>>%s' % (entry.variable, entry.factor, th1f_name), cut2)
                group_yield = th1f.GetSumOfWeights()

                ## R_QCD stuff
                region[1] += group_yield * sign
                QCD_histo.Add(th1f, sign)
                
                print 'Weight Nentries passing cuts is %.3f' % group_yield
                th1f_total.Add(th1f,group.factor)
                #nbins = th1f.GetNbinsX()
                #sum2errors = 0
                #for i in range(1,nbins+1):
                #  sum2errors += th1f.GetBinError(i)**2
                #th1f_error = math.sqrt(sum2errors)
                #print 'Error on the supergroup'


    ## Add TH1F to Histogram
            entry.histogram.add_filled(th1f_total,
                                       supergroup.legendLabel,
                                       supergroup.color,
                                       supergroup.style,
                                       supergroup.stack)

    ## Histogram.draw() 
    for entry in plots:
        entry.histogram.suffix = '_' + region[0].name
        entry.histogram.add_label('ATLAS', 0.23, 0.9)
        entry.histogram.add_label('#intL dt = 20.0fb^{-1}', 0.65, 0.89)
        entry.histogram.add_label('#sqrt{s} = 8 TeV', 0.67, 0.83)

        entry.histogram.ylog = entry.logplot


        entry.histogram.show_yields = True
        entry.histogram.make_ratio(0)
        entry.histogram.draw()
        entry.histogram.reset()


#############################################################
## R_QCD stuff
#############################################################

print '='*60
print 'R_QCD numbers'
print '-'*60

OS_number = 0
SSS_number = 0

for region in regions:
    if region[0].name == 'qcd_cr_wh_sig':
        OS_number = region[1]
    if region[0].name == 'qcd_cr_wh_ss':
        SSS_number = region[1]
    print region[0].name, region[1]

R_QCD = 1.0
if SSS_number > 0:
    R_QCD = (OS_number/SSS_number)
    print 'R_QCD = %.3f' % R_QCD
    
for i, entry in enumerate(plots):
    QCD_comparison = Histogram('%s_QCD_comparison' % entry.variable, '', entry.axislabel, entry.nbins, entry.binlow, entry.binhigh, entry.factor)
    
    for region in regions:
        if region[0].name == 'qcd_cr_wh_sig':
            QCD_comparison.add_filled(region[2][i], 'QCD OS', palette.yellow, 'fill')
        if region[0].name == 'qcd_cr_wh_ss':
            region[2][i].Scale(R_QCD)
            QCD_comparison.add_filled(region[2][i], 'QCD SSS #times R_{QCD}=%.2f' % R_QCD, palette.black, 'line', False)

    if R_QCD != 1.0:
        QCD_comparison.show_yields = True
        QCD_comparison.make_ratio(1)
        QCD_comparison.draw()
