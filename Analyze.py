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
    #                 ttbar_allh,
    #ttbar_dilep,
    #ttbar_lepfil,
    #Top,
    #SingleTop,
    #ZZ,
    #WW,
    #WZ,
    #DYZ,
    #AllBG,
    #WH]
    ZH]


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

        #####
        ####ACCEPTANCE CHALLENGE: WH125 HADHAD
        #####
        """
        cut1 = 'evtsel_weight*0.02'
        cut2 = cut1 + '*(evtsel_is_WHhadhad)'
        cut3 = cut2.strip(')') + ' && (evtsel_nLooseTaus==2))'
        cut4 = cut3.strip('))') + ') && (((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_lep1_flavour==13 && evtsel_lep1_pt>25000) || (evtsel_EF_e24vhi_medium1 && evtsel_lep1_flavour==11 && evtsel_lep1_pt>25000) || (evtsel_EF_e60_medium1 && evtsel_lep1_flavour==11 && (evtsel_lep1_pt*cosh(evtsel_lep1_eta))>60000) || (evtsel_EF_tau29Ti_medium1_tau20Ti_medium1 && evtsel_tau1_et>40000 && evtsel_tau2_et>25000)))'
        cut5 = cut4.strip(')))') + ')) && (evtsel_nMediumTaus==2))'
        cut6 = cut5.strip('2))') + '2) && (evtsel_tau1_charge*evtsel_tau2_charge==-1))'
        cut7 = cut6.strip('-1))') + '-1) && (evtsel_vlep1_etcone20/evtsel_vlep1_pt<0.06 && evtsel_vlep1_ptcone40/evtsel_vlep1_pt<0.06))'
        cut8 = cut7.strip('6))') + '6) && (evtsel_sum_tau_pt>70))'
        cut9 = cut8.strip('70))') + '70) && (evtsel_transmass_lep1MET>20))'
        ####cut10---rewrite cuts again because need to apply the evtsel_bjet_weight
        cut10 = 'evtsel_weight*0.02*evtsel_bjet_weight*(evtsel_is_WHhadhad && (evtsel_nLooseTaus==2) && (((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_lep1_flavour==13 && evtsel_lep1_pt>25000) || (evtsel_EF_e24vhi_medium1 && evtsel_lep1_flavour==11 && evtsel_lep1_pt>25000) || (evtsel_EF_e60_medium1 && evtsel_lep1_flavour==11 && (evtsel_lep1_pt*cosh(evtsel_lep1_eta))>60000) || (evtsel_EF_tau29Ti_medium1_tau20Ti_medium1 && evtsel_tau1_et>40000 && evtsel_tau2_et>25000)) && (evtsel_nMediumTaus==2) && (evtsel_tau1_charge*evtsel_tau2_charge==-1) && (evtsel_vlep1_etcone20/evtsel_vlep1_pt<0.06 && evtsel_vlep1_ptcone40/evtsel_vlep1_pt<0.06) && (evtsel_sum_tau_pt>70) && (evtsel_transmass_lep1MET>20) && evtsel_passes_bjet_veto)'


        chain.Draw('%s*%f>>%s' % (entry.variable, entry.factor, th1f_name), cut1)
        print 'Weighted Nentries to start is %.3f' % th1f.GetSumOfWeights()
        chain.Draw('%s*%f>>%s' % (entry.variable, entry.factor, th1f_name), cut2)
        print 'Weighted Nentries after WHhh flag is %.3f' % th1f.GetSumOfWeights()
        chain.Draw('%s*%f>>%s' % (entry.variable, entry.factor, th1f_name), cut3)
        print 'Weighted Nentries after 2 Loose Taus is %.3f' % th1f.GetSumOfWeights()
        chain.Draw('%s*%f>>%s' % (entry.variable, entry.factor, th1f_name), cut4)
        print 'Weighted Nentries after Triggers is %.3f' % th1f.GetSumOfWeights()
        chain.Draw('%s*%f>>%s' % (entry.variable, entry.factor, th1f_name), cut5)
        print 'Weighted Nentries after 2 Medium Taus is %.3f' % th1f.GetSumOfWeights()
        chain.Draw('%s*%f>>%s' % (entry.variable, entry.factor, th1f_name), cut6)
        print 'Weighted Nentries after tau OS charge cut %.3f' % th1f.GetSumOfWeights()
        chain.Draw('%s*%f>>%s' % (entry.variable, entry.factor, th1f_name), cut7)
        print 'Weighted Nentries after leading lep isolation %.3f' % th1f.GetSumOfWeights()
        chain.Draw('%s*%f>>%s' % (entry.variable, entry.factor, th1f_name), cut8)
        print 'Weighted Nentries after sum taupt is %.3f' % th1f.GetSumOfWeights()
        chain.Draw('%s*%f>>%s' % (entry.variable, entry.factor, th1f_name), cut9)
        print 'Weighted Nentries after transmass lep1MET is %.3f' % th1f.GetSumOfWeights()
        chain.Draw('%s*%f>>%s' % (entry.variable, entry.factor, th1f_name), cut10)
        print 'Weighted Nentries after b-jet veto is %.3f' % th1f.GetSumOfWeights()
"""
        #####
        ##ACCEPTANCE CHALLENGE: ZH125 HADHAD
        #####

        chain.Draw('%s*%f>>%s' % (entry.variable, entry.factor, th1f_name), 'evtsel_weight*0.02')
        print 'Weighted Nentries to start is %.3f' % th1f.GetSumOfWeights()
        
        chain.Draw('%s*%f>>%s' % (entry.variable, entry.factor, th1f_name), 'evtsel_weight*0.02*((((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_vlep1_flavour==13 && evtsel_vlep1_pt>25000) || (evtsel_EF_e24vhi_medium1 && evtsel_lep1_flavour==11 && evtsel_lep1_pt>25000) || (evtsel_EF_e60_medium1 && evtsel_lep1_flavour==11 && (evtsel_lep1_pt*cosh(evtsel_lep1_eta))>60000)))')
        print 'Weighted Nentries with Trigger+ptcut is %.3f' % th1f.GetSumOfWeights()

        chain.Draw('%s*%f>>%s' % (entry.variable, entry.factor, th1f_name), 'evtsel_weight*0.02*((((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_vlep1_flavour==13 && evtsel_vlep1_pt>25000) || (evtsel_EF_e24vhi_medium1 && evtsel_vlep1_flavour==11 && evtsel_vlep1_pt>25000) || (evtsel_EF_e60_medium1 && evtsel_vlep1_flavour==11 && (evtsel_vlep1_pt*cosh(evtsel_vlep1_eta))>60000)) && evtsel_nLooseTaus==1)')
        print 'Weighted Nentries with 2 Loose Taus is %.3f' % th1f.GetSumOfWeights()
        
        chain.Draw('%s*%f>>%s' % (entry.variable, entry.factor, th1f_name), 'evtsel_weight*0.02*((((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_vlep1_flavour==13 && evtsel_vlep1_pt>25000) || (evtsel_EF_e24vhi_medium1 && evtsel_vlep1_flavour==11 && evtsel_vlep1_pt>25000) || (evtsel_EF_e60_medium1 && evtsel_vlep1_flavour==11 && (evtsel_vlep1_pt*cosh(evtsel_vlep1_eta))>60000)) && (evtsel_nLooseTaus==2) && (evtsel_tau2_is_medium==1))')
        print 'Weighted Nentries with leading tau BDTL(done) and sublead BDTM is %.3f' % th1f.GetSumOfWeights()

        chain.Draw('%s*%f>>%s' % (entry.variable, entry.factor, th1f_name), 'evtsel_weight*0.02*((((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_vlep1_flavour==13 && evtsel_vlep1_pt>25000) || (evtsel_EF_e24vhi_medium1 && evtsel_vlep1_flavour==11 && evtsel_vlep1_pt>25000) || (evtsel_EF_e60_medium1 && evtsel_vlep1_flavour==11 && (evtsel_vlep1_pt*cosh(evtsel_vlep1_eta))>60000)) && (evtsel_nLooseTaus==2) && (evtsel_tau2_is_medium==1) && (evtsel_tau1_charge*evtsel_tau2_charge==-1))')
        print 'Weighted Nentries with OS taus is %.3f' % th1f.GetSumOfWeights()
        
        chain.Draw('%s*%f>>%s' % (entry.variable, entry.factor, th1f_name), 'evtsel_weight*0.02*((((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_vlep1_flavour==13 && evtsel_vlep1_pt>25000) || (evtsel_EF_e24vhi_medium1 && evtsel_vlep1_flavour==11 && evtsel_vlep1_pt>25000) || (evtsel_EF_e60_medium1 && evtsel_vlep1_flavour==11 && (evtsel_vlep1_pt*cosh(evtsel_vlep1_eta))>60000)) && (evtsel_nLooseTaus==2) && (evtsel_tau2_is_medium==1) && (evtsel_tau1_charge*evtsel_tau2_charge==-1) && (evtsel_nLeptons==2))')
        print 'Weighted Nentries with 2 Leptons is %.3f' % th1f.GetSumOfWeights()
     
        chain.Draw('%s*%f>>%s' % (entry.variable, entry.factor, th1f_name), 'evtsel_weight*0.02*((((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_vlep1_flavour==13 && evtsel_vlep1_pt>25000) || (evtsel_EF_e24vhi_medium1 && evtsel_vlep1_flavour==11 && evtsel_vlep1_pt>25000) || (evtsel_EF_e60_medium1 && evtsel_vlep1_flavour==11 && (evtsel_vlep1_pt*cosh(evtsel_vlep1_eta))>60000)) && (evtsel_nLooseTaus==2) && (evtsel_tau2_is_medium==1) && (evtsel_tau1_charge*evtsel_tau2_charge==-1) && (evtsel_nLeptons==2) && (evtsel_vlep1_charge*evtsel_vlep2_charge == -1))')
        print 'Weighted Nentries with OS leptons is %.3f' % th1f.GetSumOfWeights()
    
        chain.Draw('%s*%f>>%s' % (entry.variable, entry.factor, th1f_name), 'evtsel_weight*0.02*((((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_vlep1_flavour==13 && evtsel_vlep1_pt>25000) || (evtsel_EF_e24vhi_medium1 && evtsel_vlep1_flavour==11 && evtsel_vlep1_pt>25000) || (evtsel_EF_e60_medium1 && evtsel_vlep1_flavour==11 && (evtsel_vlep1_pt*cosh(evtsel_vlep1_eta))>60000)) && (evtsel_nLooseTaus==2) && (evtsel_tau2_is_medium==1) && (evtsel_tau1_charge*evtsel_tau2_charge==-1) && (evtsel_nLeptons==2) && (evtsel_vlep1_charge*evtsel_vlep2_charge==-1) && (evtsel_vlep1_flavour == evtsel_vlep2_flavour))')
        print 'Weighted Nentries with SF leptons is %.3f' % th1f.GetSumOfWeights()
        
        chain.Draw('%s*%f>>%s' % (entry.variable, entry.factor, th1f_name), 'evtsel_weight*0.02*((((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_vlep1_flavour==13 && evtsel_vlep1_pt>25000) || (evtsel_EF_e24vhi_medium1 && evtsel_vlep1_flavour==11 && evtsel_vlep1_pt>25000) || (evtsel_EF_e60_medium1 && evtsel_vlep1_flavour==11 && (evtsel_vlep1_pt*cosh(evtsel_vlep1_eta))>60000)) && (evtsel_nLooseTaus==2) && (evtsel_tau2_is_medium==1) && (evtsel_tau1_charge*evtsel_tau2_charge==-1) && (evtsel_nLeptons==2) && (evtsel_vlep1_charge*evtsel_vlep2_charge == -1) && (evtsel_vlep1_flavour == evtsel_vlep2_flavour) && (evtsel_vlep1_etcone20/evtsel_vlep1_pt<0.06 && evtsel_vlep1_ptcone40/evtsel_vlep1_pt<0.06) && (evtsel_vlep2_etcone20/evtsel_vlep2_pt<0.06 && evtsel_vlep2_ptcone40/evtsel_vlep2_pt<0.06))')
        print 'Weighted Nentries with lep isolation is %.3f' % th1f.GetSumOfWeights()

        chain.Draw('%s*%f>>%s' % (entry.variable, entry.factor, th1f_name), 'evtsel_weight*0.02*((((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_vlep1_flavour==13 && evtsel_vlep1_pt>25000) || (evtsel_EF_e24vhi_medium1 && evtsel_vlep1_flavour==11 && evtsel_vlep1_pt>25000) || (evtsel_EF_e60_medium1 && evtsel_vlep1_flavour==11 && (evtsel_vlep1_pt*cosh(evtsel_vlep1_eta))>60000)) && (evtsel_nLooseTaus==2) && (evtsel_tau2_is_medium==1) && (evtsel_tau1_charge*evtsel_tau2_charge==-1) && (evtsel_nLeptons==2) && (evtsel_vlep1_charge*evtsel_vlep2_charge == -1) && (evtsel_vlep1_flavour == evtsel_vlep2_flavour) && (evtsel_vlep1_etcone20/evtsel_vlep1_pt<0.06 && evtsel_vlep1_ptcone40/evtsel_vlep1_pt<0.06) && (evtsel_vlep2_etcone20/evtsel_vlep2_pt<0.06 && evtsel_vlep2_ptcone40/evtsel_vlep2_pt<0.06) && (evtsel_sum_tau_pt >70))')
        print 'Weighted Nentries with sumtaupt>70GeV is %.3f' % th1f.GetSumOfWeights()

        chain.Draw('%s*%f>>%s' % (entry.variable, entry.factor, th1f_name), 'evtsel_weight*0.02*evtsel_bjet_weight*((((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_vlep1_flavour==13 && evtsel_vlep1_pt>25000) || (evtsel_EF_e24vhi_medium1 && evtsel_vlep1_flavour==11 && evtsel_vlep1_pt>25000) || (evtsel_EF_e60_medium1 && evtsel_vlep1_flavour==11 && (evtsel_vlep1_pt*cosh(evtsel_vlep1_eta))>60000)) && (evtsel_nLooseTaus==2) && (evtsel_tau2_is_medium==1) && (evtsel_tau1_charge*evtsel_tau2_charge==-1) && (evtsel_nLeptons==2) && (evtsel_vlep1_charge*evtsel_vlep2_charge == -1) && (evtsel_vlep1_flavour == evtsel_vlep2_flavour) && (evtsel_vlep1_etcone20/evtsel_vlep1_pt<0.06 && evtsel_vlep1_ptcone40/evtsel_vlep1_pt<0.06) && (evtsel_vlep2_etcone20/evtsel_vlep2_pt<0.06 && evtsel_vlep2_ptcone40/evtsel_vlep2_pt<0.06) && (evtsel_sum_tau_pt>70) && (evtsel_passes_bjet_veto))')
        print 'Weighted Nentries passing bjet veto is %.3f' % th1f.GetSumOfWeights()
        #print 'Number of entries %d' % th1f.GetEntries()

        
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
	
	#entry.histogram.draw()
