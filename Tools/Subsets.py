#from Subset import Subset
from Subset import *
import sys

######## OS ####
OS = Subset('OS')
OS.cut('evtsel_tau1_charge*evtsel_tau2_charge', '==', -1)
################################################

##### SSS ###### FOR WH
SSS = Subset('SSS')
SSS.cut('evtsel_tau1_charge', '==', 'evtsel_tau2_charge')
SSS.cut('evtsel_tau1_charge', '==', 'evtsel_vlep1_charge')
################################################

### SSSS_ZH ########
SSSS_ZH = Subset('SSSS_ZH')
SSSS_ZH.cut('evtsel_tau1_charge', '==', 'evtsel_tau2_charge')
SSSS_ZH.cut('evtsel_vlep1_charge', '==', 'evtsel_vlep2_charge')
##########################################

#### OSS (lep opposite to 2 SS taus) #####
OSS = Subset('OSS')
OSS.cut('evtsel_tau1_charge', '==', 'evtsel_tau2_charge')
OSS.cut('evtsel_tau1_charge*evtsel_vlep1_charge', '==', -1)
################################################

##### SS Taus for ZH #######
SS = Subset('SS')
SS.cut('evtsel_tau1_charge','==', 'evtsel_tau2_charge')
#######################

######## True taus backgrounds ###########
truetaus = Subset('truetau')
truetaus.cut('evtsel_tau1_matched', '==', 1)
truetaus.cut('evtsel_tau2_matched', '==', 1)
##############################

######## 1 Fake tau background #1 #########
onefaketau = Subset('onefake')
onefaketau.cut('evtsel_tau1_matched', '==', 0)
onefaketau.cut('evtsel_tau2_matched','==', 1)
###############################
######## 1 Fake tau background #2 ############
onefaketau2 = Subset('onefake2')
onefaketau2.cut('evtsel_tau1_matched', '==', 1)
onefaketau2.cut('evtsel_tau2_matched', '==', 0)
###############################

######## 2 Fake tau background #########
twofaketau = Subset('twofake')
twofaketau.cut('evtsel_tau1_matched', '==', 0)
twofaketau.cut('evtsel_tau2_matched', '==', 0)
##############################

####### Not anti-tau events ######
istau = Subset('istau')
istau.cut('evtsel_is_tau')
##########################

##### Not anti-object events #####
isreal = Subset('isreal')
isreal.cut('evtsel_is_real')
#####################


######## Anti-tau events #1 ########
antitau = Subset('antitau')
#antitau.cut('!evtsel_is_tau')
antitau.cut('!evtsel_is_real')
antitau.cut('evtsel_nAntiElectrons_Selected', '==', 0)
antitau.cut('evtsel_nAntiMuons_Selected', '==', 0)
antitau.cut('evtsel_nAntiTaus_Selected','==', 2)
antitau.cut('evtsel_tau1_is_AntiTau','==',1)
antitau.cut('evtsel_tau2_is_AntiTau', '==', 1)
#################################
####### Anti-tau events #2 #########
antitau2 = Subset('antitau2')
#antitau2.cut('!evtsel_is_tau')
antitau2.cut('!evtsel_is_real')
antitau2.cut('evtsel_nAntiElectrons_Selected', '==', 0)
antitau2.cut('evtsel_nAntiMuons_Selected', '==', 0)
antitau2.cut('evtsel_nAntiTaus_Selected','==',1)
antitau2.cut('evtsel_tau1_is_AntiTau', '==',1)
antitau2.cut('evtsel_tau2_is_AntiTau', '==', 0)
#################################
######## Anti-tau events #3 ########
antitau3 = Subset('antitau3')
#antitau3.cut('!evtsel_is_tau')
antitau3.cut('!evtsel_is_real')
antitau3.cut('evtsel_nAntiElectrons_Selected', '==', 0)
antitau3.cut('evtsel_nAntiMuons_Selected', '==', 0)
antitau3.cut('evtsel_nAntiTaus_Selected', '==', 1)
antitau3.cut('evtsel_tau1_is_AntiTau', '==', 0)
antitau3.cut('evtsel_tau2_is_AntiTau','==', 1)
##############################



###### ZH (signal region)--Z->muons #######
zh = Subset('zh_mumu')
#zh.cut('evtsel_is_tau')
zh.cut('evtsel_is_ZHhadhad')
zh.cut('((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_lep1_flavour==13)')
#zh.cut('(evtsel_EF_e24vhi_medium1 && evtsel_lep1_flavour==11) || (evtsel_EF_e60_medium1 && evtsel_lep1_flavour==11)')
zh.cut('evtsel_vlep1_flavour','==', 13)
zh.cut('evtsel_vlep2_flavour','==', 13)
zh.cut('evtsel_nMediumTaus', '==', 2)
zh.cut('evtsel_nLeptons', '==', 2)
zh.cut('evtsel_tau1_charge*evtsel_tau2_charge', '==', -1)
zh.cut('evtsel_vlep1_charge*evtsel_vlep2_charge', '==', -1)
zh.cut('evtsel_vlep1_flavour==evtsel_vlep2_flavour')
#zh.cut('evtsel_H_m_MMC', '>', 0)
#zh.cut('evtsel_H_m_MMC', '<', 20000)
#zh.cut('evtsel_vlep1_etcone20/evtsel_vlep1_pt', '<', 0.06)
#zh.cut('evtsel_vlep1_ptcone40/evtsel_vlep1_pt', '<', 0.06)
#zh.cut('evtsel_vlep2_etcone20/evtsel_vlep2_pt', '<', 0.06)
#zh.cut('evtsel_vlep2_ptcone40/evtsel_vlep2_pt', '<', 0.06)
#zh.cut('evtsel_Zll_mass', '<', 120000)
#zh.cut('evtsel_Zll_mass', '>', 60000)
zh.cut('evtsel_sum_tau_pt', '>', 70000)
#zh.cut('evtsel_passes_bjet_veto')
#################################################

###### ZH (signal region)--Z->electrons #######
zhe = Subset('zh_ee')
#zh.cut('evtsel_is_tau')
zhe.cut('evtsel_is_ZHhadhad')
#zh.cut('((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_lep1_flavour==13)')
zhe.cut('(evtsel_EF_e24vhi_medium1 && evtsel_lep1_flavour==11) || (evtsel_EF_e60_medium1 && evtsel_lep1_flavour==11)')
zhe.cut('evtsel_vlep1_flavour','==', 11)
zhe.cut('evtsel_vlep2_flavour','==', 11)
zhe.cut('evtsel_nMediumTaus', '==', 2)
zhe.cut('evtsel_nLeptons', '==', 2)
zhe.cut('evtsel_tau1_charge*evtsel_tau2_charge', '==', -1)
zhe.cut('evtsel_vlep1_charge*evtsel_vlep2_charge', '==', -1)
zhe.cut('evtsel_vlep1_flavour==evtsel_vlep2_flavour')
#zhe.cut('evtsel_H_m_MMC', '>', 0)
#zhe.cut('evtsel_H_m_MMC', '<', 20000)
#zhe.cut('evtsel_vlep1_etcone20/evtsel_vlep1_pt', '<', 0.06)
#zhe.cut('evtsel_vlep1_ptcone40/evtsel_vlep1_pt', '<', 0.06)
#zhe.cut('evtsel_vlep2_etcone20/evtsel_vlep2_pt', '<', 0.06)
#zhe.cut('evtsel_vlep2_ptcone40/evtsel_vlep2_pt', '<', 0.06)
#zhe.cut('evtsel_Zll_mass', '<', 120000)
#zhe.cut('evtsel_Zll_mass', '>', 60000)
zhe.cut('evtsel_sum_tau_pt', '>', 70000)
#zhe.cut('evtsel_passes_bjet_veto')
#################################################


#### WH (signal region) ########
wh = Subset('wh_sig')
wh.cut('evtsel_is_tau')
wh.cut('evtsel_is_WHhadhad')
wh.cut('((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_lep1_flavour==13) || (evtsel_EF_e24vhi_medium1 && evtsel_lep1_flavour==11) || (evtsel_EF_e60_medium1 && evtsel_lep1_flavour==11) || (evtsel_EF_tau29Ti_medium1_tau20Ti_medium1)')
wh.cut('evtsel_nMediumTaus', '==', 2)
wh.cut('evtsel_nLeptons', '==', 1)
wh.cut('evtsel_vlep1_etcone20/evtsel_vlep1_pt', '<', 0.06)
wh.cut('evtsel_vlep1_ptcone40/evtsel_vlep1_pt', '<', 0.06)
wh.cut('evtsel_sum_tau_pt', '>', 70000)
wh.cut('evtsel_transmass_lep1MET', '>', 20000)
wh.cut('evtsel_passes_bjet_veto')
################


##### Observing WH but with only one tau fake, region 1 #####
whtest = Subset('whtest')
whtest.cut('evtsel_is_tau')
whtest.cut('evtsel_is_WHhadhad')
whtest.cut('((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_lep1_flavour==13) || (evtsel_EF_e24vhi_medium1 && evtsel_lep1_flavour==11) || (evtsel_EF_e60_medium1 && evtsel_lep1_flavour==11) || (evtsel_EF_tau29Ti_medium1_tau20Ti_medium1)')
whtest.cut('evtsel_nMediumTaus', '==', 2)
whtest.cut('evtsel_vlep1_etcone20/evtsel_vlep1_pt', '<', 0.06)
whtest.cut('evtsel_vlep1_ptcone40/evtsel_vlep1_pt', '<', 0.06)
whtest.cut('evtsel_sum_tau_pt', '>', 70000)
whtest.cut('evtsel_transmass_lep1MET', '>', 20000)
whtest.cut('evtsel_tau1_charge', '==', 'evtsel_tau2_charge')
whtest.cut('evtsel_passes_bjet_veto')
whtest.cut('evtsel_tau1_matched', '==', 0)
whtest.cut('evtsel_tau2_matched', '==', 1)
whtest.cut('evtsel_tau1_charge', '==', 'evtsel_vlep1_charge')
##################################################

###### Observing WH but with only one tau fake, region 2 ########
whtest2 = Subset('whtest2')
whtest2.cut('evtsel_is_tau')
whtest2.cut('evtsel_is_WHhadhad')
whtest2.cut('((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_lep1_flavour==13) || (evtsel_EF_e24vhi_medium1 && evtsel_lep1_flavour==11) || (evtsel_EF_e60_medium1 && evtsel_lep1_flavour==11) || (evtsel_EF_tau29Ti_medium1_tau20Ti_medium1)')
whtest2.cut('evtsel_nMediumTaus', '==', 2)
whtest2.cut('evtsel_vlep1_etcone20/evtsel_vlep1_pt', '<', 0.06)
whtest2.cut('evtsel_vlep1_ptcone40/evtsel_vlep1_pt', '<', 0.06)
whtest2.cut('evtsel_sum_tau_pt', '>', 70000)
whtest2.cut('evtsel_transmass_lep1MET', '>', 20000)
whtest2.cut('evtsel_tau1_charge', '==', 'evtsel_tau2_charge')
whtest2.cut('evtsel_passes_bjet_veto')
whtest2.cut('evtsel_tau1_matched', '==', 1)
whtest2.cut('evtsel_tau2_matched', '==', 0)
whtest2.cut('evtsel_tau2_charge', '==', 'evtsel_vlep1_charge')
##################################################



###### QCD-enriched data CR #######
qcd = Subset('qcd_cr')
qcd.cut('evtsel_is_WHhadhad')
qcd.cut('evtsel_MET', '<', 15000)
qcd.cut('evtsel_transmass_lep1MET', '<', 30000)
#qcd.cut('evtsel_vlep1_etcone20/evtsel_vlep1_pt', '>', 0.06)
qcd.cut('evtsel_vlep1_ptcone40/evtsel_vlep1_pt', '>', 0.06)

##################################################





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
#z_cr.cut('evtsel_vlep1_flavour','==',13)
#z_cr.cut('evtsel_vlep2_flavour','==',13)
z_cr.cut('TMath::Sqrt(2*evtsel_MET*evtsel_lep1_pt*(1-TMath::Cos(TVector2::Phi_mpi_pi((evtsel_MET_phi-evtsel_lep1_phi)))))', '<', 60000)
#z_cr.cut('evtsel_Zll_mass', '<', 120000)
#z_cr.cut('evtsel_Zll_mass', '>', 60000)
z_cr.cut('evtsel_vlep1_etcone20/evtsel_vlep1_pt', '<', 0.06)
z_cr.cut('evtsel_vlep1_ptcone40/evtsel_vlep1_pt', '<', 0.06)
#z_cr.cut('(((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_lep1_flavour==13) || (evtsel_EF_e24vhi_medium1 && evtsel_lep1_flavour==11) || (evtsel_EF_e60_medium1 && evtsel_lep1_flavour==11)')
z_cr.cut('((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_lep1_flavour==13)')
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
