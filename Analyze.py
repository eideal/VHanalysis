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
if not root_functions.Contains('ATLASLabel'):
    ROOT.gROOT.LoadMacro('AtlasStyle.C')
    ROOT.gROOT.LoadMacro('AtlasLabels.C')
    ROOT.SetAtlasStyle()

RQCD_studies = False
Make_workspace = True

RQCD_supergroups = [#for RQCD plots
#Data_RQCD,
#AllMC_RQCD
]

Plots_supergroups = [
Data,
AntitauEvents,
WZ_zerofakes,
tt_zerofakes,
ZZ_zerofakes,
#QCD,
# WH125,
ZH125,
    ]

Limit_supergroups = [
Data,
AntitauEvents,
ZH100,ZH105,ZH110,ZH115,ZH120,ZH125,ZH130,ZH135,ZH140,ZH145,ZH150,
WH100,WH105,WH110,WH115,WH120,WH125,WH130,WH135,WH140,WH145,WH150,
VBFH100,VBFH105,VBFH110,VBFH115,VBFH120,VBFH125,VBFH130,VBFH135,VBFH140,VBFH145,VBFH150,
ggH100,ggH105,ggH110,ggH115,ggH120,ggH125,ggH130,ggH135,ggH140,ggH145,ggH150,
tt_zerofakes,
ZZ_zerofakes,
WZ_zerofakes
]

list_of_systematics = [
	('','','tau',True), #this is the nominal fitting histogram
	
	('ATLAS_MU_MS','DOWN','SystematicsDOWN/MuSys',True), 
	('ATLAS_EL_ZEE','DOWN','SystematicsDOWN/ElES_Zee',True),
	('ATLAS_EL_R12','DOWN','SystematicsDOWN/ElES_R12',True),
	('ATLAS_EL_PS','DOWN','SystematicsDOWN/ElES_PS',True),  
	('ATLAS_EL_LOWPT','DOWN','SystematicsDOWN/ElES_LowPt',True),
	('ATLAS_EL_RES','DOWN','SystematicsDOWN/ElEnResSys',True),
	('ATLAS_JER_2012','DOWN','SystematicsDOWN/JER',True),
	('ATLAS_JES_2012_Statistical1','DOWN','SystematicsDOWN/JES_Statistical1',True),
	('ATLAS_JES_2012_Modelling1','DOWN','SystematicsDOWN/JES_Modelling1',True),
	('ATLAS_JES_2012_Detector1','DOWN','SystematicsDOWN/JES_Detector1',True), 
	('ATLAS_JES_2012_EtaModelling','DOWN','SystematicsDOWN/JES_EtaModelling',True), 
	('ATLAS_JES_2012_Eta_StatMethod','DOWN','SystematicsDOWN/JES_EtaMethod',True), 
	('ATLAS_JES_2012_PileRho_TAU','DOWN','SystematicsDOWN/JES_PURho',True), 
	('ATLAS_JES_NPV','DOWN','SystematicsDOWN/JES_PUNPV',True), 
	('ATLAS_JES_Mu','DOWN','SystematicsDOWN/JES_PUMu',True), 
	('ATLAS_JES_FlavComp_TAU','DOWN','SystematicsDOWN/JES_FlavComp',True), 
	('ATLAS_JES_FlavResp','DOWN','SystematicsDOWN/JES_FlavResp',True), 
	('ATLAS_JES_Flavb','DOWN','SystematicsDOWN/JES_BJet',True), 
	('ATLAS_JVF_2012','DOWN','SystematicsDOWN/JVF',True), 
	('ATLAS_TES_TRUE_2012','DOWN','SystematicsDOWN/TES',True), 
	('ATLAS_MET_RESOSOFT','DOWN','SystematicsDOWN/METResSys',True),
	('ATLAS_MET_SCALESOFT','DOWN','SystematicsDOWN/METScaleSys',True),
	('ATLAS_MU_MS','UP','SystematicsUP/MuSys',True), 
	('ATLAS_EL_ZEE','UP','SystematicsUP/ElES_Zee',True), 
	('ATLAS_EL_R12','UP','SystematicsUP/ElES_R12',True), 
	('ATLAS_EL_PS','UP','SystematicsUP/ElES_PS',True),
	('ATLAS_EL_LOWPT','UP','SystematicsUP/ElES_LowPt',True),
	('ATLAS_EL_RES','UP','SystematicsUP/ElEnResSys',True),
	('ATLAS_JER_2012','UP','SystematicsUP/JER',True),
	('ATLAS_JES_2012_Statistical1','UP','SystematicsUP/JES_Statistical1',True),
	('ATLAS_JES_2012_Modelling1','UP','SystematicsUP/JES_Modelling1',True),
	('ATLAS_JES_2012_Detector1','UP','SystematicsUP/JES_Detector1',True), 
	('ATLAS_JES_2012_EtaModelling','UP','SystematicsUP/JES_EtaModelling',True), 
	('ATLAS_JES_2012_Eta_StatMethod','UP','SystematicsUP/JES_EtaMethod',True), 
	('ATLAS_JES_2012_PileRho_TAU','UP','SystematicsUP/JES_PURho',True), 
	('ATLAS_JES_NPV','UP','SystematicsUP/JES_PUNPV',True), 
	('ATLAS_JES_Mu','UP','SystematicsUP/JES_PUMu',True), 
	('ATLAS_JES_FlavComp_TAU','UP','SystematicsUP/JES_FlavComp',True), 
	('ATLAS_JES_FlavResp','UP','SystematicsUP/JES_FlavResp',True), 
	('ATLAS_JES_Flavb','UP','SystematicsUP/JES_BJet',True), 
	('ATLAS_JVF_2012','UP','SystematicsUP/JVF',True), 
	('ATLAS_TES_TRUE_2012','UP','SystematicsUP/TES',True), 
	('ATLAS_MET_RESOSOFT','UP','SystematicsUP/METResSys',True), 
	('ATLAS_MET_SCALESOFT','UP','SystematicsUP/METScaleSys',True),
#('ATLAS_BTag_BEFF','DOWN','evtsel_bjet_sys_b_down',False), 
#	('ATLAS_BTag_BEFF','UP','evtsel_bjet_sys_b_up',False), 
#	('ATLAS_BTag_CEFF','DOWN','evtsel_bjet_sys_c_down',False), 
#	('ATLAS_BTag_CEFF','UP','evtsel_bjet_sys_c_up',False), 
#	('ATLAS_BTag_LEFF','DOWN','evtsel_bjet_sys_m_down',False),
#	('ATLAS_BTag_LEFF','UP','evtsel_bjet_sys_m_up',False), 
	('ATLAS_PU_RESCALE_2012','DOWN','evtsel_sys_PU_rescaling_dn',False), 
	('ATLAS_PU_RESCALE_2012','UP','evtsel_sys_PU_rescaling_up',False), 
	('ATLAS_EL_ID','DOWN','evtsel_sys_sf_el_id_down',False),
	('ATLAS_EL_ID','UP','evtsel_sys_sf_el_id_up',False),
	('ATLAS_EL_ISO','DOWN','evtsel_sys_sf_el_iso_down',False),
	('ATLAS_EL_ISO','UP','evtsel_sys_sf_el_iso_up',False),
	('ATLAS_EL_TRIG','DOWN','evtsel_sys_sf_el_trig_down',False),
	('ATLAS_EL_TRIG','UP','evtsel_sys_sf_el_trig_up',False),
######('','DOWN','evtsel_sys_sf_electron_FF_down',False),
######(,'UP','evtsel_sys_sf_electron_FF_UP',False),
	('ATLAS_MU_ID','DOWN','evtsel_sys_sf_mu_id_down',False), 
	('ATLAS_MU_ID','UP','evtsel_sys_sf_mu_id_up',False), 
	('ATLAS_MU_ISO','DOWN','evtsel_sys_sf_mu_iso_down',False), 
	('ATLAS_MU_ISO','UP','evtsel_sys_sf_mu_iso_up',False), 
	('ATLAS_MU_TRIG','DOWN','evtsel_sys_sf_mu_trig_down',False), 
	('ATLAS_MU_TRIG','UP','evtsel_sys_sf_mu_trig_up',False), 
#######	('DOWN','evtsel_sys_sf_muon_FF_down',False),
######	(,'UP','evtsel_sys_sf_muon_FF_up',False),
######	('DOWN','evtsel_sys_sf_tau_FF_down',False),
######	(,'UP','evtsel_sys_sf_tau_FF_up',False),
	('ATLAS_TAU_EFAKE_2012','DOWN','evtsel_sys_sf_tau_el_down',False),
	('ATLAS_TAU_EFAKE_2012','UP','evtsel_sys_sf_tau_el_up',False), 
	('ATLAS_TAU_ID_2012','DOWN','evtsel_sys_sf_tau_id_down',False), 
	('ATLAS_TAU_ID_2012','UP','evtsel_sys_sf_tau_id_up',False), 
	('ATLAS_TAU_ID_STAT_2012','DOWN','evtsel_sys_sf_tau_id_stat_down',False), ### WHAT IS THIS?
	('ATLAS_TAU_ID_STAT_2012','UP','evtsel_sys_sf_tau_id_stat_up',False), ## WHAT IS THIS?
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
# [ZHe, 0.0, []]
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
                    
        QCD_histo = ROOT.TH1F('QCD_%s' % region[0].name, '', entry.nbins, entry.binlow, entry.binhigh)
        region[2].append(QCD_histo)

        #Loop over systematics (this also includes the nominal histogram)
        for sys in list_of_systematics:
            sys_name = sys[0] ##ATLAS official name
            sys_var = sys[1] ## <up,down>
            sys_path = sys[2] ## branch or tree path
            sys_is_tree = sys[3] ##bool if branch or if tree
			
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
					
					#Instantiate TChain: depending on the type of systematic
                    if sys_is_tree:
                        chain = ROOT.TChain(sys_path)
                    else:
                        chain = ROOT.TChain('tau')

                    for sample in group.samples:
                        #print '    ', sample.path
                        chain.Add(sample.path)

                    if sys_is_tree:
                        cut1 = 'evtsel_weight*0.02'
                        if supergroup.name == 'AntitauEvents':
                            cut1 = 'evtsel_weight_FF'
                        if supergroup.name == 'Data':
                            cut1 = 'evtsel_weight'
                    else:
                        cut1 = 'evtsel_weight*0.02*%s' % sys_path
                        if supergroup.name == 'AntitauEvents':
                            cut1 = 'evtsel_weight_FF'
                        if supergroup.name == 'Data':
                            cut1 = 'evtsel_weight'

                        #if supergroup.name == 'QCD':
						#    region[0] = region[0] + QCD_CR

                
                    cut2 = cut1 + '*' + (region[0] + supergroup.subset + group.subset).string() 

                    if (entry.variable == 'evtsel_dR'):
                        chain.Draw('TMath::Sqrt(TMath::Power((evtsel_tau1_eta-evtsel_tau2_eta),2)+TMath::Power(TVector2::Phi_mpi_pi((evtsel_tau1_phi-evtsel_tau2_phi)),2))>>%s' % th1f_name,cut2)
                        group_yield = th1f.GetSumOfWeights()
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
                    h.add(region[0].name, region[0].name + '_' + sys_name + '_' + sys_var + '_' + supergroup.name, th1f_total)
					
            
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
