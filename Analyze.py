#from Tools import Subsets_with_a_super_long_name as ss
from Tools import Subsets
from Tools.Supergroups import *
#from Tools.Groups import *
from Tools.Histogram import Histogram
from plotting import plots #"from blank" where blank is the name of the python file blank.py and you can import anything that is defined with an equals sign. It can be a class or a variable
from Tools import palette
from Tools.histo_container import HistoContainer
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

RQCD_studies = False
Make_workspace = True

RQCD_supergroups = [#for RQCD plots
Data_RQCD,
AllMC_RQCD
]

Plots_supergroups = [
Data,
AntitauEvents,
#AntiTauEvents_2AntiTau,
#WeJets,
#WmJets,
#WtJets,
#tt,
WZ_zerofakes,
#WZ_onefake,
#WZ_twofakes,
tt_zerofakes,
#tt_onefake,
#tt_twofakes,
#SingleTop,
WmJets_zerofakes,
#WmJets_onefake,
#WmJets_twofakes,
ZttJets_zerofakes,
ZZ_zerofakes,
#ZZ_onefake,
#ZZ_twofakes,
#WW,
#WGamma,
#ZttJets_onefake,
#ZttJets_twofakes,
#ZeeJets,
#ZmmJets,
ZmmJets_zerofakes,
#ZmmJets_onefake,
#ZmmJets_twofakes,
#ZttJets,
#tt,
#ZZ,
#WZ,
#QCD,
# WH125,
ZH125,
    ]

Limit_supergroups = [
Data,
AntitauEvents,
ZH100,ZH105,ZH110,ZH115,ZH120,ZH125,ZH130,ZH135,ZH140,ZH145,ZH150,
WH100,WH105,WH110,WH115,WH125,WH130,WH135,WH140,WH145,WH150, ### WH120
VBFH100,VBFH105,VBFH110,VBFH115,VBFH120,VBFH125,VBFH130,VBFH135,VBFH140,VBFH145,VBFH150,
ggH100,ggH105,ggH110,ggH115,ggH120,ggH125,ggH130,ggH135,ggH140,ggH145,ggH150,
tt_zerofakes,
ZZ_zerofakes,
WZ_zerofakes
]

list_of_supergroups = Plots_supergroups

if Make_workspace:
    list_of_supergroups = Limit_supergroups
if RQCD_studies:
    list_of_supergroups = RQCD_supergroups

###Subsets definition
WH = Subsets.wh
ZH = Subsets.zh
ZHe = Subsets.zhe
ZHistau = Subsets.zh + Subsets.istau
TT = Subsets.tt_cr
WJets = Subsets.w_cr
ZJets = Subsets.z_cr

WH_SSS =  Subsets.wh + Subsets.SSS
WH_OSS = Subsets.wh + Subsets.OSS
QCD_SSS = Subsets.qcd + Subsets.SSS
QCD_SSS.name = 'SSS'
QCD_OS = Subsets.qcd + Subsets.OS
QCD_OS.name = 'OS'
WHstudy = Subsets.whtest * Subsets.whtest2  #Dec3-5 study


regions = [
    [ZH, 0.0, []],
    [ZHe, 0.0, []]
    ]
if RQCD_studies:
    regions = [
    [QCD_OS,  0.0, []],
    [QCD_SSS, 0.0, []],
    ]

h = HistoContainer('evtsel_H_m_MMC')
    
####Loop over regions
for region in regions:

    h.add_region(region[0].name)

    ###Loop over plots
    for entry in plots:
        #if entry.rootfile:
        #   h = HistoContainer(entry.variable)
            
        QCD_histo = ROOT.TH1F('QCD_%s' % region[0].name, '', entry.nbins, entry.binlow, entry.binhigh)
        region[2].append(QCD_histo)

        ##Loop over supergroups
        for supergroup in list_of_supergroups:
            print 'Plotting supergroup %s ...' % supergroup.name
            th1f_total_name = '%s_%s_sg' % (entry.variable, supergroup.name)
            th1f_total = ROOT.TH1F(th1f_total_name, supergroup.legendLabel, entry.nbins, entry.binlow, entry.binhigh)
            th1f_total.Sumw2()

            for group in supergroup.groups:
                print 'Plotting group %s ...' % group.name
                th1f_name = '%s_%s_g' % (entry.variable, group.name)
                th1f = ROOT.TH1F(th1f_name, supergroup.legendLabel, entry.nbins, entry.binlow, entry.binhigh)
                th1f.Sumw2()

                #Instantiate TChain
                chain = ROOT.TChain('tau')

                for sample in group.samples:
                    #print '    ', sample.path
                    chain.Add(sample.path)
 
                
                cut1 = 'evtsel_weight*0.02*evtsel_weight_tau_fakerate' #evtsel_bjet_weight
                if supergroup.name == 'AntitauEvents':
                    cut1 = 'evtsel_weight*evtsel_weight_FF'
                if supergroup.name == 'Data':
                    cut1 = 'evtsel_weight'
                #if supergroup.name == 'QCD':
                #    region[0] = region[0] + QCD_CR

                
                cut2 = cut1 + '*' + (region[0] + supergroup.subset + group.subset).string() 

                if (entry.variable == 'evtsel_dR'):
                    chain.Draw('TMath::Sqrt(TMath::Power((evtsel_tau1_eta-evtsel_tau2_eta),2)+TMath::Power(TVector2::Phi_mpi_pi((evtsel_tau1_phi-evtsel_tau2_phi)),2))>>%s' % th1f_name,cut2)
                else: 
                    chain.Draw('%s*%f>>%s' % (entry.variable, entry.factor, th1f_name), cut2)
                group_yield = th1f.GetSumOfWeights()
                #group_yield = th1f.GetEntries()

                ## R_QCD stuff
                region[1] += group_yield*group.factor*supergroup.factor
                #QCD_histo.Add(th1f, sign)
                QCD_histo.Add(th1f,group.factor*supergroup.factor)
                
                ##########print 'Weight Nentries passing cuts is %.3f' % (group_yield*group.factor*supergroup.factor)
                th1f_total.Add(th1f,group.factor*supergroup.factor)
               

            #Compute error on the supergroup
            supergroup_raw_yield = th1f_total.GetEntries()
            supergroup_raw_error = math.sqrt(supergroup_raw_yield)
            #print 'Number of raw supergroup entries is %d' % (supergroup_raw_yield)
            #print 'Raw error on the %s supergroup is %.3f' % (supergroup.name, supergroup_raw_error) 
            supergroup_weighted_yield = th1f_total.GetSumOfWeights()
            print 'Number of weighted %s supergroup entries is %.3f' % (supergroup.name,supergroup_weighted_yield)
            nbins = th1f_total.GetNbinsX()
            sum2errors = 0
            for i in range(1,nbins+1):
                sum2errors += th1f_total.GetBinError(i)**2
            th1f_error = math.sqrt(sum2errors)
            print 'Error on the %s supergroup is %.3f' % (supergroup.name,th1f_error)


     ## Add TH1F to Histogram
            entry.histogram.add_filled(th1f_total,
                                       supergroup.legendLabel,
                                       supergroup.color,
                                       supergroup.style,
                                       supergroup.stack)
            if entry.rootfile:
                h.add(region[0].name, region[0].name + '_' + supergroup.name, th1f_total)
            
    ## Histogram.draw()
    if not Make_workspace: 
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

if Make_workspace:
    h.save()
    h.make_workspace()


#############################################################
## R_QCD calculation
#############################################################

print '='*60
print 'R_QCD numbers'
print '-'*60

OS_number = 0
SSS_number = 0

for region in regions:
    if region[0].name == 'OS':
        OS_number = region[1]
    if region[0].name == 'SSS':
        SSS_number = region[1]
    print region[0].name, region[1]

R_QCD = 1.0
if SSS_number > 0:
    R_QCD = (OS_number/SSS_number)
    print 'R_QCD = %.3f' % R_QCD
    
for i, entry in enumerate(plots):
    QCD_comparison = Histogram('%s_QCD_comparison' % entry.variable, '', entry.axislabel, entry.nbins, entry.binlow, entry.binhigh, entry.factor)
    
    for region in regions:
        if region[0].name == 'OS':
            QCD_comparison.add_filled(region[2][i], 'QCD OS', palette.yellow, 'fill')
        if region[0].name == 'SSS':
            region[2][i].Scale(R_QCD)
            #QCD_comparison.add_filled(region[2][i], 'QCD SSS #times R_{QCD}=%.2f' % R_QCD, palette.black, 'line', False)
            QCD_comparison.add_filled(region[2][i], 'QCD SSS', palette.black, 'line', False)

    if R_QCD != 1.0:
        QCD_comparison.show_yields = True
        QCD_comparison.make_ratio(1)
        QCD_comparison.draw()
