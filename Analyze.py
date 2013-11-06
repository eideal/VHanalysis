from Tools.Groups import *
from Tools.Histogram import Histogram
from plotting import plots # "from blank" where blank is the name of the python file blank.py and you can import anything that is defined with an equals sign. It can be a class or a variable
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
    

    list_of_groups = [
	Data,
    #WlepnuNp0,
    #WlepnuJets,
    #WlepnuJetsAFII,
    #Data,
    #WtaunuNp0,
    #WtaunuJets,
    #ZleplepNp0,
    #ZleplepJets,
    #Ztautau,
    #ZtautauJets,
    #WH,
    #ZH,
    #ZJets,
    #WJets,
    WeJets,
	SSSWeJets,
    WmJets,
	SSSWmJets,
    WtJets,
	SSSWtJets,
	ZeeJets,
	SSSZeeJets,
    ZmmJets,
	SSSZmmJets,
    ZttJets,
	SSSZttJets,
    #WJetsAFII,
    #ZJetsAFII,
    #WJetsMedID,
    tt,
	SSStt,
    SingleTop,
	SSSSingleTop,
    ZZ,
	SSSZZ,
    WW,
	SSSWW,
    WGamma,
	SSSWGamma,
    WZ,
	SSSWZ,
	DataSSS,
    #AllBG,
    #ggF,
    #ZH,
    #VBF,
    ]


## Loop over groups
for group in list_of_groups:

    print 'Plotting %s ...' % group.name

    ## Instantiate TChain
    chain = ROOT.TChain('tau')

    ## Loop over the samples in the group and load in TChain
    for sample in group.samples:
        #print '    ', sample.path
        chain.Add(sample.path)

    # th1f_name_tem1 = 'num'
    # th1f_name_tem2 = 'den'
    # th1f_num = ROOT.TH1F(th1f_name_tem1,group.plotting.legendLabel,30,0,300)
    # th1f_den = ROOT.TH1F(th1f_name_tem2,group.plotting.legendLabel,30,0,300)
	#th1f_name_tem1 = 'OSMC'
	#th1f_name_tem2 = 'SSSMC'
	#th1f_OSMC = ROOT.TH1F(th1f_name_tem1, group.plotting.legendLabel,30,0,300)
	#th1f_SSSMC = ROOT.TH1F(th1f_name_tem2, group.plotting.legendLabel,30,0,300)


    for entry in plots:
        th1f_name = '%s_%s' % (entry.variable,	group.name)
        th1f = ROOT.TH1F(th1f_name, group.plotting.legendLabel, entry.nbins, entry.binlow, entry.binhigh)
        th1f.Sumw2() 
        #th1f_den.Sumw2()

               
        ####
        ### ttbar CR
        ####
        """
        cut1 = 'evtsel_weight*0.02'
        if group.classification == 'DATA':
            cut1 = 'evtsel_weight'
        cut2 = cut1 + '*(evtsel_is_tau && evtsel_jets_num>=2 && evtsel_MET>30000 && TMath::Sqrt(2*evtsel_MET*evtsel_lep1_pt*(1-TMath::Cos(TVector2::Phi_mpi_pi((evtsel_MET_phi-evtsel_lep1_phi)))))>50000 && evtsel_nLeptons>0 && ( ((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_lep1_flavour==13 && evtsel_lep1_pt>25000) || (evtsel_EF_e24vhi_medium1 && evtsel_lep1_flavour==11 && evtsel_lep1_pt>25000) || (evtsel_EF_e60_medium1 && evtsel_lep1_flavour==11 && (evtsel_lep1_pt*cosh(evtsel_lep1_eta))>60000)) && evtsel_vlep1_etcone20/evtsel_vlep1_pt<0.06 && evtsel_vlep1_ptcone40/evtsel_vlep1_pt<0.06 && !(evtsel_passes_bjet_veto) )'
        """
        
        ####
        ### Z+Jets CR
        ####
        """
        cut1 = 'evtsel_weight*0.02'
        if group.classification == 'DATA':
            cut1 = 'evtsel_weight'
        cut2 = cut1 + '*(evtsel_is_tau && evtsel_nLeptons==2 && evtsel_passes_bjet_veto && TMath::Sqrt(2*evtsel_MET*evtsel_lep1_pt*(1-TMath::Cos(TVector2::Phi_mpi_pi((evtsel_MET_phi-evtsel_lep1_phi)))))<60000 && evtsel_Zll_mass<120000 && evtsel_Zll_mass>60000 && evtsel_vlep1_etcone20/evtsel_vlep1_pt<0.06 && evtsel_vlep1_ptcone40/evtsel_vlep1_pt<0.06 && ( ((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_lep1_flavour==13 && evtsel_lep1_pt>25000) || (evtsel_EF_e24vhi_medium1 && evtsel_lep1_flavour==11 && evtsel_lep1_pt>25000) || (evtsel_EF_e60_medium1 && evtsel_lep1_flavour==11 && (evtsel_lep1_pt*cosh(evtsel_lep1_eta))>60000)) )'
        """
        #####
        ### W+Jets CR 
        #####
        """
        cut1 = 'evtsel_weight*0.02'
        if group.classification == 'DATA':
            cut1 = 'evtsel_weight'
        cut2 = cut1 + '*(evtsel_is_tau && TMath::Sqrt(2*evtsel_MET*evtsel_lep1_pt*(1-TMath::Cos(TVector2::Phi_mpi_pi((evtsel_MET_phi-evtsel_lep1_phi)))))>60000 && evtsel_nLeptons==1 && evtsel_passes_bjet_veto && evtsel_vlep1_etcone20/evtsel_vlep1_pt<0.06 && evtsel_vlep1_ptcone40/evtsel_vlep1_pt<0.06 && ( ((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_lep1_flavour==13 && evtsel_lep1_pt>25000) || (evtsel_EF_e24vhi_medium1 && evtsel_lep1_flavour==11 && evtsel_lep1_pt>25000) || (evtsel_EF_e60_medium1 && evtsel_lep1_flavour==11 && (evtsel_lep1_pt*cosh(evtsel_lep1_eta))>60000))  )'
            #cut2 = cut1 + '*(!evtsel_is_tau && TMath::Sqrt(2*evtsel_MET*evtsel_lep1_pt*(1-TMath::Cos(TVector2::Phi_mpi_pi((evtsel_MET_phi-evtsel_lep1_phi)))))>60000 && evtsel_nLeptons==2)'
            #cut2 = cut1 + '*( !(evtsel_is_tau) && TMath::Sqrt(2*evtsel_MET*evtsel_lep1_pt*(1-TMath::Cos(TVector2::Phi_mpi_pi((evtsel_MET_phi-evtsel_lep1_phi)))))>60000 && evtsel_passes_bjet_veto && evtsel_vlep1_etcone20/evtsel_vlep1_pt<0.06 && evtsel_vlep1_ptcone40/evtsel_vlep1_pt<0.06 && evtsel_nLeptons==1 && ( ((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_lep1_flavour==13 && evtsel_lep1_pt>25000) || (evtsel_EF_e24vhi_medium1 && evtsel_lep1_flavour==11 && evtsel_lep1_pt>25000) || (evtsel_EF_e60_medium1 && evtsel_lep1_flavour==11 && (evtsel_lep1_pt*cosh(evtsel_lep1_eta))>60000)))' #SLT
            #cut3 = cut1 + '*(evtsel_is_tau && (!(evtsel_tau1_is_medium)) && TMath::Sqrt(2*evtsel_MET*evtsel_lep1_pt*(1-TMath::Cos(TVector2::Phi_mpi_pi((evtsel_MET_phi-evtsel_lep1_phi)))))>60000 && evtsel_passes_bjet_veto && evtsel_vlep1_etcone20/evtsel_vlep1_pt<0.06 && evtsel_vlep1_ptcone40/evtsel_vlep1_pt<0.06 && evtsel_nLeptons==1 && ( ((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_lep1_flavour==13 && evtsel_lep1_pt>25000) || (evtsel_EF_e24vhi_medium1 && evtsel_lep1_flavour==11 && evtsel_lep1_pt>25000) || (evtsel_EF_e60_medium1 && evtsel_lep1_flavour==11 && (evtsel_lep1_pt*cosh(evtsel_lep1_eta))>60000)))' #SLT
        

        if entry.variable == 'evtsel_tau1_et_failL':
            chain.Draw('%s*%f>>%s' % ('evtsel_tau1_et', entry.factor, th1f_name), cut2)
            chain.Draw('%s*%f>>%s' % ('evtsel_tau1_et', entry.factor, th1f_name_tem2), cut2)
            th1f.Scale(group.factor)
            print 'Weighted Nentries of taus failing BDTL is %.3f' % th1f.GetSumOfWeights()
        if entry.variable == 'evtsel_tau1_et_passL':
            chain.Draw('%s*%f>>%s' % ('evtsel_tau1_et', entry.factor, th1f_name), cut3)
            chain.Draw('%s*%f>>%s' % ('evtsel_tau1_et', entry.factor, th1f_name_tem1), cut3)
            th1f.Scale(group.factor)
            print 'Weighted Nentries of taus passing BDTL is %.3f' % th1f.GetSumOfWeights()

            
        
        if entry.variable == 'evtsel_dR':
            chain.Draw('TMath::Sqrt(TMath::Power((evtsel_tau1_eta-evtsel_tau2_eta),2) + TMath::Power(TVector2::Phi_mpi_pi((evtsel_tau1_phi-evtsel_tau2_phi)),2))>>%s' % th1f_name, cut2)
            th1f.Scale(group.factor)
            print 'Weighted Nentries after Triggers is %.3f' % th1f.GetSumOfWeights()
        if entry.variable == 'evtsel_transmass_lep1MET':
            chain.Draw('%s*%f>>%s' % ('TMath::Sqrt(2*evtsel_MET*evtsel_lep1_pt*(1-TMath::Cos(TVector2::Phi_mpi_pi((evtsel_MET_phi-evtsel_lep1_phi)))))', entry.factor, th1f_name), cut2)
            th1f.Scale(group.factor)
            nbins = th1f.GetNbinsX()
            sum2errors = 0
            for i in range(1,nbins+1):
                sum2errors += th1f.GetBinError(i)**2
            th1f_error = math.sqrt(sum2errors)
            print 'Weighted Nentries after Triggers is %.3f' % th1f.GetSumOfWeights()
            print 'th1f error is %.3f' % th1f_error
        else:
            chain.Draw('%s*%f>>%s' % (entry.variable, entry.factor, th1f_name), cut2)
            th1f.Scale(group.factor)
            nbins = th1f.GetNbinsX()
            sum2errors = 0
            for i in range(1,nbins+1):
                sum2errors += th1f.GetBinError(i)**2
            th1f_error = math.sqrt(sum2errors)
            print 'Weighted Nentries after Triggers is %.3f' % th1f.GetSumOfWeights()
            print 'th1f error is %.3f' % th1f_error
           """ 
	
	
            
        #####
        ####ACCEPTANCE CHALLENGE: WH125 HADHAD
        #####

        cut1 = 'evtsel_weight*0.02'
        if group.classification == 'DATA':
			cut1 = 'evtsel_weight'
        cut2 = cut1 + '*(evtsel_is_tau && evtsel_is_WHhadhad && evtsel_tau1_charge*evtsel_tau2_charge==-1)'
        cut2ex = cut1 + '*(evtsel_is_tau && evtsel_is_WHhadhad && evtsel_tau1_charge==evtsel_tau2_charge && evtsel_tau2_charge==evtsel_vlep1_charge)'
        #cut3 = cut2.strip(')') + '&& (((evtsel_EF_tau29Ti_medium1_tau20Ti_medium1))))'
        #cut3 = cut2.strip(')') + ' && ' + mutau_trigstring + '||' + etau_trigstring '||' + mumu_simtrigstring '||' + ee_simtrigstring '||' +mumu_difftrigstring '||' + ee_difftrigstring '||' + emu_trigstring '||' + singlemu_trigstring '||' + singlee_trigstring +')'
        #cut3 = cut2.strip(')') + ' && (((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_lep1_flavour==13 && evtsel_lep1_pt>26000) || (evtsel_EF_e24vhi_medium1 && evtsel_lep1_flavour==11 && evtsel_lep1_pt>26000) || (evtsel_EF_tau20_medium1_mu15 && evtsel_tau1_et>25000 && evtsel_lep1_flavour==13 && evtsel_lep1_pt>17000) || (evtsel_EF_tau20Ti_medium1_e18vh_medium1 && evtsel_lep1_pt>20000 && evtsel_tau1_et>25000)))' #LEPHAD TRIG
        #cut3 = cut2.strip(')') + ' && (((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_lep1_flavour==13 && evtsel_lep1_pt>25000) || (evtsel_EF_e24vhi_medium1 && evtsel_lep1_flavour==11 && evtsel_lep1_pt>25000) || (evtsel_EF_e60_medium1 && evtsel_lep1_flavour==11 && (evtsel_lep1_pt*cosh(evtsel_lep1_eta))>60000) || (evtsel_EF_tau29Ti_medium1_tau20Ti_medium1 && evtsel_tau1_et>40000 && evtsel_tau2_et>25000)))' #HADHAD TRIG
        cut3 = cut2.strip(')') + ' && (((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_lep1_flavour==13) || (evtsel_EF_e24vhi_medium1 && evtsel_lep1_flavour==11) || (evtsel_EF_e60_medium1 && evtsel_lep1_flavour==11) || (evtsel_EF_tau29Ti_medium1_tau20Ti_medium1)))' #HH NO PT THRESHOLDS
        cut3ex = cut2ex.strip(')') + ' && (((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_lep1_flavour==13) || (evtsel_EF_e24vhi_medium1 && evtsel_lep1_flavour==11) || (evtsel_EF_e60_medium1 && evtsel_lep1_flavour==11) || (evtsel_EF_tau29Ti_medium1_tau20Ti_medium1)))'
        #cut3 = cut2.strip(')') + ' && (evtsel_EF_e24vhi_medium1 && evtsel_lep1_flavour==11 && evtsel_lep1_pt>25000))'#CHECKS ON SINGLE TRIGGERS
        cut4 = cut3.strip(')))') + ')) && (evtsel_nLooseTaus==2))'
        cut5 = cut4.strip('2))') + '2) && (evtsel_nMediumTaus==2))'
        cut6 = cut5.strip('mTaus==2))') + 'umTaus==2) && (evtsel_tau1_charge*evtsel_tau2_charge==-1))'
        cut7 = cut6.strip('-1))') + '-1) && (evtsel_nLeptons==1))'
        cut8 = cut7.strip('==1))') + '==1) && (evtsel_vlep1_etcone20/evtsel_vlep1_pt<0.06 && evtsel_vlep1_ptcone40/evtsel_vlep1_pt<0.06))'
        cut9 = cut8.strip('6))') + '6) && (evtsel_sum_tau_pt>70000))'
        cut10 = cut9.strip('70000))') + '70000) && (evtsel_transmass_lep1MET>20000))'
        ####cut11---rewrite cuts again because need to apply the evtsel_bjet_weight
        cut11 = 'evtsel_weight*0.02*(evtsel_is_WHhadhad && evtsel_is_tau && (evtsel_nLooseTaus==2) && (((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_lep1_flavour==13 && evtsel_lep1_pt>25000) || (evtsel_EF_e24vhi_medium1 && evtsel_lep1_flavour==11 && evtsel_lep1_pt>25000) || (evtsel_EF_e60_medium1 && evtsel_lep1_flavour==11 && (evtsel_lep1_pt*cosh(evtsel_lep1_eta))>60000) || (evtsel_EF_tau29Ti_medium1_tau20Ti_medium1 && evtsel_tau1_et>40000 && evtsel_tau2_et>25000)) && (evtsel_nMediumTaus==2) && (evtsel_tau1_charge*evtsel_tau2_charge==-1) && (evtsel_nLeptons==1) && (evtsel_vlep1_etcone20/evtsel_vlep1_pt<0.06 && evtsel_vlep1_ptcone40/evtsel_vlep1_pt<0.06) && (evtsel_sum_tau_pt>70000) && (evtsel_transmass_lep1MET>20000) && evtsel_passes_bjet_veto)'
        #cut11 = 'evtsel_weight*0.02*(evtsel_is_WHhadhad && evtsel_is_tau && (evtsel_nLooseTaus==2) && (((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_lep1_flavour==13 && evtsel_lep1_pt>25000) || (evtsel_EF_e24vhi_medium1 && evtsel_lep1_flavour==11 && evtsel_lep1_pt>25000) || (evtsel_EF_e60_medium1 && evtsel_lep1_flavour==11 && (evtsel_lep1_pt*cosh(evtsel_lep1_eta))>60000) || (evtsel_EF_tau29Ti_medium1_tau20Ti_medium1 && evtsel_tau1_et>40000 && evtsel_tau2_et>25000)) && (evtsel_nMediumTaus==2) && (evtsel_tau1_charge*evtsel_tau2_charge==1) && (evtsel_nLeptons==1) && (evtsel_vlep1_etcone20/evtsel_vlep1_pt<0.06 && evtsel_vlep1_ptcone40/evtsel_vlep1_pt<0.06) && (evtsel_sum_tau_pt>70000) && (evtsel_transmass_lep1MET>20000) && evtsel_passes_bjet_veto)' #### SAME SIGN MC
        if group.classification == 'DATA':
            cut11 = 'evtsel_weight*(evtsel_is_WHhadhad && evtsel_is_tau && evtsel_tau1_matched==0 && evtsel_tau2_matched==0 && (evtsel_nLooseTaus==2) && (((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_lep1_flavour==13 && evtsel_lep1_pt>25000) || (evtsel_EF_e24vhi_medium1 && evtsel_lep1_flavour==11 && evtsel_lep1_pt>25000) || (evtsel_EF_e60_medium1 && evtsel_lep1_flavour==11 && (evtsel_lep1_pt*cosh(evtsel_lep1_eta))>60000) || (evtsel_EF_tau29Ti_medium1_tau20Ti_medium1 && evtsel_tau1_et>40000 && evtsel_tau2_et>25000)) && (evtsel_nMediumTaus==2) && (evtsel_tau1_charge*evtsel_tau2_charge==-1) && (evtsel_nLeptons==1) && (evtsel_vlep1_etcone20/evtsel_vlep1_pt<0.06 && evtsel_vlep1_ptcone40/evtsel_vlep1_pt<0.06) && (evtsel_sum_tau_pt>70000) && (evtsel_transmass_lep1MET>20000) && evtsel_passes_bjet_veto)'
            #cut11 = 'evtsel_weight*(evtsel_is_WHhadhad && evtsel_is_tau && (evtsel_nLooseTaus==2) && (((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_lep1_flavour==13 && evtsel_lep1_pt>25000) || (evtsel_EF_e24vhi_medium1 && evtsel_lep1_flavour==11 && evtsel_lep1_pt>25000) || (evtsel_EF_e60_medium1 && evtsel_lep1_flavour==11 && (evtsel_lep1_pt*cosh(evtsel_lep1_eta))>60000) || (evtsel_EF_tau29Ti_medium1_tau20Ti_medium1 && evtsel_tau1_et>40000 && evtsel_tau2_et>25000)) && (evtsel_nMediumTaus==2) && (evtsel_tau1_charge*evtsel_tau2_charge==1) && (evtsel_nLeptons==1) && (evtsel_vlep1_etcone20/evtsel_vlep1_pt<0.06 && evtsel_vlep1_ptcone40/evtsel_vlep1_pt<0.06) && (evtsel_sum_tau_pt>70000) && (evtsel_transmass_lep1MET>20000) && evtsel_passes_bjet_veto)'####SAME SIGN DATA

        if (group.name=='SSSWeJets' or group.name=='SSSWmJets' or group.name == 'SSSWtJets' or group.name =='SSSZeeJets' or group.name =='SSSZmmJets' or group.name =='SSSZttJets' or group.name =='SSStt' or group.name =='SSSSingleTop' or group.name =='SSSWW' or group.name =='SSSWZ' or group.name =='SSSZZ' or group.name =='SSSWGamma' or group.name=='DataSSS'):
            chain.Draw('%s*%f>>%s' % (entry.variable, entry.factor, th1f_name), cut3ex)
            th1f.Scale(group.factor)
            print 'Weight Nentries in SSS is %.3f' % th1f.GetSumOfWeights()
        if (group.name=='WeJets' or group.name=='WmJets' or group.name == 'WtJets' or group.name =='ZeeJets' or group.name =='ZmmJets' or group.name =='ZttJets' or group.name =='tt' or group.name =='SingleTop' or group.name =='WW' or group.name =='WZ' or group.name =='ZZ' or group.name =='WGamma' or group.name=='Data'):
            chain.Draw('%s*%f>>%s' % (entry.variable, entry.factor, th1f_name), cut3)
            th1f.Scale(group.factor)
            print 'Weight Nentries in OS is %.3f' % th1f.GetSumOfWeights()

        """
        if group.name != 'DataSSS':
            if entry.testing== '_OSMC':
                chain.Draw('evtsel_MET*%f>>%s' % (entry.factor, th1f_name), cut3)
				th1f.Scale(group.factor)
                print 'Weight Nentries in OS plot is %.3f' % th1f.GetSumOfWeights()
        if group.name=='DataSSS':
            if entry.testing=='_SSSdata':
                chain.Draw('%s*%f>>%s' % ('evtsel_MET', entry.factor, th1f_name), cut3ex)
                th1f.Scale(group.factor)
                print 'Weight Nentries in SSS data plot is %.3f' % th1f.GetSumOfWeights()
        if (group.name != 'DataSSS' and group.name != 'Data'):
            if entry.testing=='_SSSMC':
                chain.Draw('evtsel_MET*%f>>%s' % (entry.factor, th1f_name), cut3ex)
                th1f.Scale(group.factor)
                print 'Weight Nentries in SSS MC plot is %.3f' % th1f.GetSumOfWeights()
        


                #th1f.Scale(1.0/th1f.GetSumOfWeights()) ## TO SCALE HISTO TO UNITY
    
        if entry.variable == 'evtsel_MET1':
            chain.Draw('sqrt(pow(evtsel_met_etx, 2) + pow(evtsel_met_ety,2))>>%s' % th1f_name, cut3)
            th1f.Scale(group.factor)
            print 'Weighted Nentries after Triggers is %.3f' % th1f.GetSumOfWeights()
        elif entry.variable == 'evtsel_dphi':
            chain.Draw('TVector2::Phi_mpi_pi((evtsel_tau1_phi-evtsel_tau2_phi))>>%s' % th1f_name, cut3)
            th1f.Scale(group.factor)
            print 'Weighted Nentries after Triggers is %.3f' % th1f.GetSumOfWeights()
        elif entry.variable == 'evtsel_deta':
            chain.Draw('(evtsel_tau1_eta-evtsel_tau2_eta)>>%s' % th1f_name, cut3)
            th1f.Scale(group.factor)
            print 'Weighted Nentries after Triggers is %.3f' % th1f.GetSumOfWeights()
        elif entry.variable == 'evtsel_dR':
            chain.Draw('TMath::Sqrt(TMath::Power((evtsel_tau1_eta-evtsel_tau2_eta),2) + TMath::Power(TVector2::Phi_mpi_pi((evtsel_tau1_phi-evtsel_tau2_phi)),2))>>%s' % th1f_name, cut3)
            th1f.Scale(group.factor)
            nbins = th1f.GetNbinsX()
            sum2errors = 0
            for i in range(1,nbins+1):
                sum2errors += th1f.GetBinError(i)**2
            th1f_error = math.sqrt(sum2errors)
            print 'Weighted Nentries after Triggers is %.3f' % th1f.GetSumOfWeights()
            print 'th1f error is %.3f' % th1f_error
            print 'Weighted Nentries after Triggers is %.3f' % th1f.GetSumOfWeights()
        elif entry.variable == 'evtsel_transmass_lep1MET':
            chain.Draw('%s*%f>>%s' % ('TMath::Sqrt(2*evtsel_MET*evtsel_lep1_pt*(1-TMath::Cos(TVector2::Phi_mpi_pi((evtsel_MET_phi-evtsel_lep1_phi)))))', entry.factor, th1f_name), cut3)
            th1f.Scale(group.factor)
        else:
            chain.Draw('%s*%f>>%s' % (entry.variable, entry.factor, th1f_name), cut3)
            th1f.Scale(group.factor)
            nbins = th1f.GetNbinsX()
            sum2errors = 0
            for i in range(1,nbins+1):
                sum2errors += th1f.GetBinError(i)**2
            th1f_error = math.sqrt(sum2errors)
            print 'Weighted Nentries after Triggers is %.3f' % th1f.GetSumOfWeights()
            print 'th1f error is %.3f' % th1f_error
		"""

            
        #####
        ##ACCEPTANCE CHALLENGE: ZH125 HADHAD
        #####
        """
        cut1 = 'evtsel_weight*0.02'
        if group.classification == 'DATA':
            cut1 = 'evtsel_weight'
        #cut2 = cut1 + '*(evtsel_is_ZHhadhad && evtsel_is_tau)'
        #cut2 = cut1 + '*(evtsel_is_tau && evtsel_passes_isolation && evtsel_is_WHlephad)'
        cut2 = cut1 + '*(evtsel_is_tau && evtsel_is_ZHhadhad)'
        cut3 = cut2.strip(')') + '&& ((((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_lep1_flavour==13 && evtsel_lep1_pt>25000) || (evtsel_EF_e24vhi_medium1 && evtsel_lep1_flavour==11 && evtsel_lep1_pt>25000) || (evtsel_EF_e60_medium1 && evtsel_lep1_flavour==11 && (evtsel_lep1_pt*cosh(evtsel_lep1_eta))>60000))))'
        cut4 = cut3.strip('))))') + '))) && (evtsel_nLooseTaus==2))'
        cut5 = cut4.strip('2))') + '2) && (evtsel_tau2_is_medium==1))'
        cut6 = cut5.strip('1))') + '1) && (evtsel_tau1_charge*evtsel_tau2_charge==-1))'
        cut7 = cut6.strip('-1))') + '-1) && (evtsel_nLeptons==2))'
        cut8 = cut7.strip('ons==2))') + 'ons==2) && (evtsel_vlep1_etcone20/evtsel_vlep1_pt<0.06 && evtsel_vlep1_ptcone40/evtsel_vlep1_pt<0.06) && (evtsel_vlep2_etcone20/evtsel_vlep2_pt<0.06 && evtsel_vlep2_ptcone40/evtsel_vlep2_pt<0.06))'
        cut9 = cut8.strip('6))') + '6) && (evtsel_vlep1_charge*evtsel_vlep2_charge == -1))'
        cut10  = 'evtsel_weight*0.02*(evtsel_is_ZHhadhad*evtsel_is_tau*((((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_lep1_flavour==13 && evtsel_lep1_pt>25000) || (evtsel_EF_e24vhi_medium1 && evtsel_lep1_flavour==11 && evtsel_lep1_pt>25000) || (evtsel_EF_e60_medium1 && evtsel_lep1_flavour==11 && (evtsel_lep1_pt*cosh(evtsel_lep1_eta))>60000))) && (evtsel_nLooseTaus==2) && (evtsel_tau2_is_medium==1) && (evtsel_tau1_charge*evtsel_tau2_charge==-1) && (evtsel_nLeptons==2) && (evtsel_vlep1_etcone20/evtsel_vlep1_pt<0.06 && evtsel_vlep1_ptcone40/evtsel_vlep1_pt<0.06) && (evtsel_vlep2_etcone20/evtsel_vlep2_pt<0.06 && evtsel_vlep2_ptcone40/evtsel_vlep2_pt<0.06) && (evtsel_vlep1_charge*evtsel_vlep2_charge==-1) && (evtsel_vlep1_flavour == evtsel_vlep2_flavour))'
        cut11 = cut10.strip('our))') + 'our) && (evtsel_Zll_mass<120000) && (evtsel_Zll_mass>60000))'
        cut12 = cut11.strip('ss>60000))') + 'ss>60000) && (evtsel_sum_tau_pt >70000))'
        if group.classification=='DATA':
            cut13 = 'evtsel_weight*(evtsel_is_ZHhadhad*evtsel_is_tau*((((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_lep1_flavour==13 && evtsel_lep1_pt>25000) || (evtsel_EF_e24vhi_medium1 && evtsel_lep1_flavour==11 && evtsel_lep1_pt>25000) || (evtsel_EF_e60_medium1 && evtsel_lep1_flavour==11 && (evtsel_lep1_pt*cosh(evtsel_lep1_eta))>60000))) && (evtsel_nLooseTaus==2) && (evtsel_tau2_is_medium==1) && (evtsel_tau1_charge*evtsel_tau2_charge==-1) && (evtsel_nLeptons==2) && (evtsel_vlep1_charge*evtsel_vlep2_charge == -1) && (evtsel_vlep1_flavour == evtsel_vlep2_flavour) && (evtsel_vlep1_etcone20/evtsel_vlep1_pt<0.06 && evtsel_vlep1_ptcone40/evtsel_vlep1_pt<0.06) && (evtsel_vlep2_etcone20/evtsel_vlep2_pt<0.06 && evtsel_vlep2_ptcone40/evtsel_vlep2_pt<0.06) && (evtsel_Zll_mass<120000) && (evtsel_Zll_mass>60000) && (evtsel_sum_tau_pt>70000) && (evtsel_passes_bjet_veto))'
        else:            
            cut13 = 'evtsel_weight*0.02*(evtsel_is_ZHhadhad*evtsel_is_tau*((((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_lep1_flavour==13 && evtsel_lep1_pt>25000) || (evtsel_EF_e24vhi_medium1 && evtsel_lep1_flavour==11 && evtsel_lep1_pt>25000) || (evtsel_EF_e60_medium1 && evtsel_lep1_flavour==11 && (evtsel_lep1_pt*cosh(evtsel_lep1_eta))>60000))) && (evtsel_nLooseTaus==2) && (evtsel_tau2_is_medium==1) && (evtsel_tau1_charge*evtsel_tau2_charge==-1) && (evtsel_nLeptons==2) && (evtsel_vlep1_charge*evtsel_vlep2_charge == -1) && (evtsel_vlep1_flavour == evtsel_vlep2_flavour) && (evtsel_vlep1_etcone20/evtsel_vlep1_pt<0.06 && evtsel_vlep1_ptcone40/evtsel_vlep1_pt<0.06) && (evtsel_vlep2_etcone20/evtsel_vlep2_pt<0.06 && evtsel_vlep2_ptcone40/evtsel_vlep2_pt<0.06) && (evtsel_Zll_mass<120000) && (evtsel_Zll_mass>60000) && (evtsel_sum_tau_pt>70000) && (evtsel_passes_bjet_veto))'


        #chain.Draw('%s*%f>>%s' % (entry.variable, entry.factor, th1f_name), cut1)
        #print 'Weighted Nentries to start is %.3f' % th1f.GetSumOfWeights()
        #th1f.Scale(1.0/th1f.GetSumOfWeights())
        # chain.Draw('%s*%f>>%s' % (entry.variable, entry.factor, th1f_name), cut2)
        # print 'Weighted Nentries with ZHhh category flag is %.3f' % th1f.GetSumOfWeights()

        if entry.variable == 'evtsel_MET1':
            chain.Draw('sqrt(pow(evtsel_met_etx, 2) + pow(evtsel_met_ety,2))>>%s' % th1f_name, cut3)
            th1f.Scale(group.factor)
            print 'Weighted Nentries after Triggers is %.3f' % th1f.GetSumOfWeights()
        elif entry.variable == 'evtsel_dphi':
            chain.Draw('TVector2::Phi_mpi_pi((evtsel_tau1_phi-evtsel_tau2_phi))>>%s' % th1f_name, cut3)
            th1f.Scale(group.factor)
            print 'Weighted Nentries after Triggers is %.3f' % th1f.GetSumOfWeights()
        elif entry.variable == 'evtsel_deta':
            chain.Draw('(evtsel_tau1_eta-evtsel_tau2_eta)>>%s' % th1f_name, cut3)
            th1f.Scale(group.factor)
            print 'Weighted Nentries after Triggers is %.3f' % th1f.GetSumOfWeights()
        elif entry.variable == 'evtsel_dR':
            chain.Draw('TMath::Sqrt(TMath::Power((evtsel_tau1_eta-evtsel_tau2_eta),2) + TMath::Power(TVector2::Phi_mpi_pi((evtsel_tau1_phi-evtsel_tau2_phi)),2))>>%s' % th1f_name, cut3)
            th1f.Scale(group.factor)
            nbins = th1f.GetNbinsX()
            sum2errors = 0
            for i in range(1,nbins+1):
                sum2errors += th1f.GetBinError(i)**2
            th1f_error = math.sqrt(sum2errors)
            print 'Weighted Nentries after Triggers is %.3f' % th1f.GetSumOfWeights()
            print 'th1f error is %.3f' % th1f_error
            print 'Weighted Nentries after Triggers is %.3f' % th1f.GetSumOfWeights()
        elif entry.variable == 'evtsel_transmass_lep1MET':
            chain.Draw('%s*%f>>%s' % ('TMath::Sqrt(2*evtsel_MET*evtsel_lep1_pt*(1-TMath::Cos(TVector2::Phi_mpi_pi((evtsel_MET_phi-evtsel_lep1_phi)))))', entry.factor, th1f_name), cut3)
            th1f.Scale(group.factor)
        else:
            chain.Draw('%s*%f>>%s' % (entry.variable, entry.factor, th1f_name), cut3)
            th1f.Scale(group.factor)
            nbins = th1f.GetNbinsX()
            sum2errors = 0
            for i in range(1,nbins+1):
                sum2errors += th1f.GetBinError(i)**2
            th1f_error = math.sqrt(sum2errors)
            print 'Weighted Nentries after Triggers is %.3f' % th1f.GetSumOfWeights()
            print 'th1f error is %.3f' % th1f_error
		"""
       
       
        
## Add TH1F to Histogram
        entry.histogram.add_filled(th1f,
                                   group.plotting.legendLabel,
                                   group.plotting.color,
                                   group.plotting.style,
                                   group.plotting.stack)

        #if entry.variable == 'evtsel_MET_SSSdata':
		#	canvas = ROOT.TCanvas('histo_canvas','histo_canvas', 0,0,800,600)
		#	canvas.cd()
		#	finalhist1 = ROOT.TH1F.Add(th1f_OSMC, th1f_SSSMC, 1, -1)
		#	finalhist2 = ROOT.TH1F.Add(finalhist1, th1f, 1, 1)
		#	finalhist.Draw('')
		#	canvas.Print('finalhist2.png')
        # if entry.variable == 'evtsel_tau1_et_passL':
        #     #effhist = ROOT.TGraphAsymmErrors(th1f, th1f_den)
        #                 #effhist = ROOT.TGraphAsymmErrors(th1f_num,th1f_den)

        #                 #effhist = ROOT.TGraphAsymmErrors(th1f_num, th1f_den)
        #     canvas = ROOT.TCanvas('histo_canvas','histo_canvas',0,0,800,600)
        #     #canvas2 = ROOT.TCanvas('histo_canvas2','histo_canvas2',0,0,800,600)
        #     canvas.cd()
        #     #effhist = ROOT.TGraphAsymmErrors(th1f, th1f_den)
        #     #th1f.Draw()
        #     #canvas2.cd()
        #     #th1f_den.Draw()
        #     th1f.Divide(th1f_den)
        #     th1f.Draw('')
        #     #effhist.Draw('AP')
        #     canvas.Print('effhist.png')
        #     #canvas2.Print('effhist2.png')
            
            

## Histogram.draw() 
for entry in plots:
    entry.histogram.add_label('ATLAS', 0.23, 0.9)
    entry.histogram.add_label('#intL dt = 20.0fb^{-1}', 0.65, 0.89)
    entry.histogram.add_label('#sqrt{s} = 8 TeV', 0.67, 0.83)
    
    entry.histogram.ylog = entry.logplot

	
    entry.histogram.show_yields = True
    entry.histogram.make_ratio(0)
    entry.histogram.draw()

    
