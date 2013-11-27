#from Subset import Subset
from Subset import *
import sys

####### WH OS (signal region) #######
wh_os = Subset('wh_sig')
wh_os.cut('evtsel_is_tau')
wh_os.cut('evtsel_is_WHhadhad')
wh_os.cut('((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_lep1_flavour==13) || (evtsel_EF_e24vhi_medium1 && evtsel_lep1_flavour==11) || (evtsel_EF_e60_medium1 && evtsel_lep1_flavour==11) || (evtsel_EF_tau29Ti_medium1_tau20Ti_medium1)')
wh_os.cut('evtsel_tau1_charge*evtsel_tau2_charge', '==', -1)
#wh_os.cut('evtsel_nMediumTaus', '==', 2)
#wh_os.cut('evtsel_nLeptons', '==', 1)
#wh_os.cut('evtsel_vlep1_etcone20/evtsel_vlep1_pt', '<', 0.06)
#wh_os.cut('evtsel_vlep1_ptcone40/evtsel_vlep1_pt', '<', 0.06)
#wh_os.cut('evtsel_sum_tau_pt', '>', 70000)
#wh_os.cut('evtsel_transmass_lep1MET', '>', 20000)
#wh_os.cut('evtsel_passes_bjet_veto')
#################################################


####### WH SSS region ########
wh_sss = Subset('wh_ss')
wh_sss.cut('evtsel_is_tau')
wh_sss.cut('evtsel_is_WHhadhad')
wh_sss.cut('((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_lep1_flavour==13) || (evtsel_EF_e24vhi_medium1 && evtsel_lep1_flavour==11) || (evtsel_EF_e60_medium1 && evtsel_lep1_flavour==11) || (evtsel_EF_tau29Ti_medium1_tau20Ti_medium1)')
wh_sss.cut('evtsel_tau1_charge', '==', 'evtsel_tau2_charge')
wh_sss.cut('evtsel_tau1_charge', '==', 'evtsel_vlep1_charge')
#wh_sss.cut('evtsel_nMediumTaus', '==', 2)
#wh_sss.cut('evtsel_nLeptons', '==', 1)
#wh_sss.cut('evtsel_vlep1_etcone20/evtsel_vlep1_pt', '<', 0.06)
#wh_sss.cut('evtsel_vlep1_ptcone40/evtsel_vlep1_pt', '<', 0.06)
#wh_sss.cut('evtsel_sum_tau_pt', '>', 70000)
#wh_sss.cut('evtsel_transmass_lep1MET', '>', 20000)
#wh_sss.cut('evtsel_passes_bjet_veto')
##################################################


###### QCD-enriched data CR #######
qcd = Subset('qcd_cr')
#qcd.cut('evtsel_is_tau')
#qcd.cut('evtsel_is_WHhadhad')
#qcd.cut('((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_lep1_flavour==13) || (evtsel_EF_e24vhi_medium1 && evtsel_lep1_flavour==11) || (evtsel_EF_e60_medium1 && evtsel_lep1_flavour==11) || (evtsel_EF_tau29Ti_medium1_tau20Ti_medium1)')
qcd.cut('evtsel_MET', '<', 15000)
qcd.cut('evtsel_transmass_lep1MET', '<', 30000)
#qcd.cut('evtsel_vlep1_etcone20/evtsel_vlep1_pt', '>', 0.06)
#qcd.cut('evtsel_vlep1_ptcone40/evtsel_vlep1_pt', '>', 0.06)

##################################################


###### ZH OS (signal region) #######
zh_os = Subset('zh_sig')
zh_os.cut('evtsel_is_tau')
zh_os.cut('evtsel_is_ZHhadhad')
zh_os.cut('(((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_lep1_flavour==13) || (evtsel_EF_e24vhi_medium1 && evtsel_lep1_flavour==11) || (evtsel_EF_e60_medium1 && evtsel_lep1_flavour==11))')
zh_os.cut('evtsel_nMediumTaus', '==', 2)
zh_os.cut('evtsel_tau1_charge*evtsel_tau2_charge', '==', -1)
zh_os.cut('evtsel_nLeptons', '==', 2)
zh_os.cut('evtsel_vlep1_charge*evtsel_vlep2_charge', '==', -1)
zh_os.cut('evtsel_vlep1_flavour==evtsel_vlep2_flavour')
zh_os.cut('evtsel_vlep1_etcone20/evtsel_vlep1_pt', '<', 0.06)
zh_os.cut('evtsel_vlep1_ptcone40/evtsel_vlep1_pt', '<', 0.06)
zh_os.cut('evtsel_vlep2_etcone20/evtsel_vlep2_pt', '<', 0.06)
zh_os.cut('evtsel_vlep2_ptcone40/evtsel_vlep2_pt', '<', 0.06)
zh_os.cut('evtsel_Zll_mass', '<', 120000)
zh_os.cut('evtsel_Zll_mass', '>', 60000)
zh_os.cut('evtsel_sum_tau_pt', '>', 70000)
zh_os.cut('evtsel_passes_bjet_veto')
#################################################


###### ttbar CR ########
tt_cr = Subset('ttbar_cr')
tt_cr.cut('evtsel_is_tau')
tt_cr.cut('evtsel_jets_num', '>=', 2)
tt_cr.cut('evtsel_MET', '>', 30000)
tt_cr.cut('evtsel_transmass_lep1MET', '>', 50000)
tt_cr.cut('evtsel_nLeptons', '>', 0)
tt_cr.cut('((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_lep1_flavour==13) || (evtsel_EF_e24vhi_medium1 && evtsel_lep1_flavour==11) || (evtsel_EF_e60_medium1 && evtsel_lep1_flavour==11)')
tt_cr.cut('evtsel_vlep1_etcone20/evtsel_vlep1_pt', '<', 0.06)
tt_cr.cut('evtsel_vlep1_ptcone40/evtsel_vlep1_pt', '<', 0.06)
tt_cr.cut('!(evtsel_passes_bjet_veto)')
##################################################


###### Z+Jets CR #######
z_cr = Subset('zjets_cr')
z_cr.cut('evtsel_is_tau')
z_cr.cut('evtsel_nLeptons', '==', 2)
z_cr.cut('evtsel_passes_bjet_veto')
z_cr.cut('TMath::Sqrt(2*evtsel_MET*evtsel_lep1_pt*(1-TMath::Cos(TVector2::Phi_mpi_pi((evtsel_MET_phi-evtsel_lep1_phi)))))', '<', 60000)
z_cr.cut('evtsel_Zll_mass', '<', 120000)
z_cr.cut('evtsel_Zll_mass', '>', 60000)
z_cr.cut('evtsel_vlep1_etcone20/evtsel_vlep1_pt', '<', 0.06)
z_cr.cut('evtsel_vlep1_ptcone40/evtsel_vlep1_pt', '<', 0.06)
z_cr.cut('(((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_lep1_flavour==13) || (evtsel_EF_e24vhi_medium1 && evtsel_lep1_flavour==11) || (evtsel_EF_e60_medium1 && evtsel_lep1_flavour==11)')
##################################################


###### W+Jets CR #######
w_cr = Subset('wjets_cr')
w_cr.cut('evtsel_is_tau')
w_cr.cut('TMath::Sqrt(2*evtsel_MET*evtsel_lep1_pt*(1-TMath::Cos(TVector2::Phi_mpi_pi((evtsel_MET_phi-evtsel_lep1_phi)))))', '>', 60000)
w_cr.cut('evtsel_nLeptons', '==', 1)
w_cr.cut('evtsel_passes_bjet_veto')
w_cr.cut('evtsel_vlep1_etcone20/evtsel_vlep1_pt', '<', 0.06)
w_cr.cut('evtsel_vlep1_ptcone40/evtsel_vlep1_pt', '<', 0.06)
w_cr.cut('(((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_lep1_flavour==13) || (evtsel_EF_e24vhi_medium1 && evtsel_lep1_flavour==11) || (evtsel_EF_e60_medium1 && evtsel_lep1_flavour==11)')
#################################################


