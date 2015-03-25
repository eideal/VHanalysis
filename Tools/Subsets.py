#from Subset import Subset
from Subset import *
import sys


#######################

######## True taus backgrounds ###########
truetaus = Subset('truetau')
truetaus.cut('evtsel_tau1_matched', '==', 1)
truetaus.cut('evtsel_tau2_matched', '==', 1)
##############################

##### True taus backgrounds (for WHlephad) ####
truetaus2 = Subset('truetaus2')
truetaus2.cut('evtsel_tau1_matched', '==', 1)

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


####### TESTING 18 June 2014 -- because getting an underestimation in the model #####
noantitau = Subset('noantitau')
noantitau.cut('evtsel_nAntiTaus', '==', 0)


yesantitau = Subset('yesantitau')
yesantitau.cut('evtsel_nAntiTaus_Selected', '>', 0)
###########

##### Not anti-object events #####
isreal = Subset('isreal')
isreal.cut('evtsel_is_real')
#####################

#### MC CORRECTION TO FAKE TAUS#####
MCcorr = Subset('MCcorr')
MCcorr.cut('!evtsel_is_real')
#MCcorr.cut('(evtsel_tau1_matched && evtsel_tau1_is_AntiTau) || (evtsel_tau2_matched && evtsel_tau2_is_AntiTau) || (evtsel_vlep1_is_prompt && evtsel_vlep1_is_Anti)')
MCcorr.cut('((evtsel_tau1_matched && evtsel_tau1_is_AntiTau) || (evtsel_tau2_matched && evtsel_tau2_is_AntiTau))')
MCcorr.cut('evtsel_nAntiElectrons_Selected', '==', 0)
MCcorr.cut('evtsel_nAntiMuons_Selected', '==', 0)

###ALL fakes##
allfakes = Subset('allfakes')
allfakes.cut('!evtsel_is_real')
#allfakes.cut('evtsel_nAntiTaus_Selected', '>', 0)

##### Anti-tau events ONLY ###
antitau = Subset('antitau_test')
antitau.cut('!evtsel_is_real')
#antitau.cut('evtsel_nAntiTaus_Selected','>',0)
antitau.cut('evtsel_nAntiElectrons_Selected', '==', 0)
antitau.cut('evtsel_nAntiMuons_Selected', '==', 0)

#### TRUTH REQ IF CONSIDERING ALL OBJECT FAKES #####
truthObj = Subset('truthObj')
truthObj.cut('evtsel_tau1_matched', '==', 1)
truthObj.cut('evtsel_tau2_matched', '==', 1)
truthObj.cut('evtsel_vlep1_is_prompt', '==', 1)
#truthObj.cut('evtsel_vlep2_is_prompt', '==', 1)
#####

#### Some subsets made to study pT Higgs dependence after making selection cuts
ZHcat = Subset('ZHcat')
ZHcat.cut('evtsel_is_ZHhadhad')
#ZHcat.cut('evtsel_is_ZHlephad')

ZHtrig = Subset('ZHtrig')
ZHtrig.cut('evtsel_is_ZHhadhad')
ZHtrig.cut('((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_lep1_flavour==13)')
#ZHtrig.cut('(evtsel_EF_e24vhi_medium1 && evtsel_lep1_flavour==11) || (evtsel_EF_e60_medium1 && evtsel_lep1_flavour==11)')


ZHflav = Subset('ZHflav')
ZHflav.cut('evtsel_is_ZHhadhad')
#ZHflav.cut('((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_lep1_flavour==13)')
#ZHflav.cut('evtsel_vlep1_flavour','==', 13)
#ZHflav.cut('evtsel_vlep2_flavour','==', 13)
ZHflav.cut('(evtsel_EF_e24vhi_medium1 && evtsel_lep1_flavour==11) || (evtsel_EF_e60_medium1 && evtsel_lep1_flavour==11)')
ZHflav.cut('evtsel_vlep1_flavour','==', 11)
ZHflav.cut('evtsel_vlep2_flavour','==', 11)

ZHcharge = Subset('ZHcharge')
ZHcharge.cut('evtsel_is_ZHhadhad')
ZHcharge.cut('((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_lep1_flavour==13)')
ZHcharge.cut('evtsel_vlep1_flavour','==', 13)
ZHcharge.cut('evtsel_vlep2_flavour','==', 13)
#ZHcharge.cut('(evtsel_EF_e24vhi_medium1 && evtsel_lep1_flavour==11) || (evtsel_EF_e60_medium1 && evtsel_lep1_flavour==11)')
#ZHcharge.cut('evtsel_vlep1_flavour','==', 11)
#ZHcharge.cut('evtsel_vlep2_flavour','==', 11)
ZHcharge.cut('evtsel_tau1_charge*evtsel_tau2_charge', '==', -1)
ZHcharge.cut('evtsel_vlep1_charge*evtsel_vlep2_charge', '==', -1)

ZHall = Subset('ZHall')
ZHall.cut('evtsel_is_ZHhadhad')
#ZHall.cut('evtsel_is_ZHlephad')
#ZHall.cut('((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_lep1_flavour==13)')
#ZHall.cut('evtsel_vlep1_flavour','==', 13)
#ZHall.cut('evtsel_vlep2_flavour','==', 13)
ZHall.cut('(evtsel_EF_e24vhi_medium1 && evtsel_lep1_flavour==11) || (evtsel_EF_e60_medium1 && evtsel_lep1_flavour==11)')
ZHall.cut('evtsel_vlep1_flavour','==', 11)
ZHall.cut('evtsel_vlep2_flavour','==', 11)
#ZHall.cut('(evtsel_EF_e24vhi_medium1 && evtsel_lep1_flavour==11) || (evtsel_EF_e60_medium1 && evtsel_lep1_flavour==11) || (evtsel_EF_mu24i_tight && evtsel_lep1_flavour==13) || (evtsel_EF_mu36_tight && evtsel_lep1_flavour==13) || (evtsel_EF_mu18_tight_mu8_EFFS && evtsel_lep1_flavour==13) || (evtsel_EF_2mu13 && evtsel_lep1_flavour==13) || (evtsel_EF_e24vh_medium1_e7_medium1 && evtsel_lep1_flavour==11) || (evtsel_EF_2e12Tvh_loose1 && evtsel_lep1_flavour==11)')
#ZHall.cut('evtsel_MET', '>', 20000)
#ZHall.cut('evtsel_tau1_et', '>', 25000)
#ZHall.cut('evtsel_passes_bjet_veto')
#ZHall.cut('evtsel_vlep1_flavour','==', 'evtsel_vlep2_flavour')
ZHall.cut('evtsel_vlep1_charge*evtsel_vlep2_charge', '==', -1)
ZHall.cut('evtsel_H_m_MMC', '>', 0)
#ZHall.cut('evtsel_hlep1_etcone20/evtsel_hlep1_pt', '<=', 0.08)
#ZHall.cut('evtsel_hlep1_ptcone40/evtsel_hlep1_pt', '<=', 0.08)
ZHall.cut('evtsel_tau1_charge*evtsel_tau2_charge', '==', -1)
#ZHall.cut('evtsel_vlep1_etcone20/evtsel_vlep1_pt', '<=', 0.08)
#ZHall.cut('evtsel_vlep1_ptcone40/evtsel_vlep1_pt', '<=', 0.08)
#ZHall.cut('evtsel_vlep2_etcone20/evtsel_vlep2_pt', '<=', 0.08)
#ZHall.cut('evtsel_vlep2_ptcone40/evtsel_vlep2_pt', '<=', 0.08)
ZHall.cut('evtsel_Zll_m', '<', 120000)
ZHall.cut('evtsel_Zll_m', '>', 60000)
#ZHall.cut('evtsel_sum_tau_pt', '>', 70000)


WHcat = Subset('WHcat')
WHcat.cut('evtsel_is_WHlephad')

WHzmassveto = Subset('WHzmassveto')
WHzmassveto.cut('evtsel_is_WHlephad')
WHzmassveto.cut('(evtsel_EF_e24vhi_medium1 && evtsel_lep1_flavour==11) || (evtsel_EF_e60_medium1 && evtsel_lep1_flavour==11) || (evtsel_EF_mu24i_tight && evtsel_lep1_flavour==13) || (evtsel_EF_mu36_tight && evtsel_lep1_flavour==13) || (evtsel_EF_mu18_tight_mu8_EFFS && evtsel_lep1_flavour==13) || (evtsel_EF_2mu13 && evtsel_lep1_flavour==13) || (evtsel_EF_e24vh_medium1_e7_medium1 && evtsel_lep1_flavour==11) || (evtsel_EF_2e12Tvh_loose1 && evtsel_lep1_flavour==11)')
WHzmassveto.cut('evtsel_vlep1_flavour', '==', 13)
WHzmassveto.cut('evtsel_hlep1_flavour', '==', 13)
WHzmassveto.cut('evtsel_vlep1_charge', '==', 'evtsel_hlep1_charge')
WHzmassveto.cut('evtsel_passes_Z_mass_veto')
                    
WHpresel = Subset('WHpresel')
WHpresel.cut('evtsel_is_WHlephad')
WHpresel.cut('(evtsel_EF_e24vhi_medium1 && evtsel_lep1_flavour==11) || (evtsel_EF_e60_medium1 && evtsel_lep1_flavour==11) || (evtsel_EF_mu24i_tight && evtsel_lep1_flavour==13) || (evtsel_EF_mu36_tight && evtsel_lep1_flavour==13) || (evtsel_EF_mu18_tight_mu8_EFFS && evtsel_lep1_flavour==13) || (evtsel_EF_2mu13 && evtsel_lep1_flavour==13) || (evtsel_EF_e24vh_medium1_e7_medium1 && evtsel_lep1_flavour==11) || (evtsel_EF_2e12Tvh_loose1 && evtsel_lep1_flavour==11)')
WHpresel.cut('((evtsel_vlep1_flavour == 13 && evtsel_hlep1_flavour == 11) || (evtsel_vlep1_flavour == 11 && evtsel_hlep1_flavour == 13))')
WHpresel.cut('evtsel_vlep1_charge', '==', 'evtsel_hlep1_charge')
                
WHall = Subset('WHall')
WHall.cut('evtsel_is_WHlephad')
WHall.cut('(evtsel_EF_e24vhi_medium1 && evtsel_lep1_flavour==11) || (evtsel_EF_e60_medium1 && evtsel_lep1_flavour==11) || (evtsel_EF_mu24i_tight && evtsel_lep1_flavour==13) || (evtsel_EF_mu36_tight && evtsel_lep1_flavour==13) || (evtsel_EF_mu18_tight_mu8_EFFS && evtsel_lep1_flavour==13) || (evtsel_EF_2mu13 && evtsel_lep1_flavour==13) || (evtsel_EF_e24vh_medium1_e7_medium1 && evtsel_lep1_flavour==11) || (evtsel_EF_2e12Tvh_loose1 && evtsel_lep1_flavour==11)')
#WHall.cut('evtsel_vlep1_flavour', '==', 13)
#WHall.cut('evtsel_hlep1_flavour', '==', 13)
WHall.cut('((evtsel_vlep1_flavour == 13 && evtsel_hlep1_flavour == 11) || (evtsel_vlep1_flavour == 11 && evtsel_hlep1_flavour == 13))')
WHall.cut('evtsel_vlep1_charge', '==', 'evtsel_hlep1_charge')
#WHall.cut('evtsel_sum_lep_pt', '>', 80000)
#WHall.cut('evtsel_MET', '>', 20000)
#WHall.cut('evtsel_passes_bjet_veto')
#WHall.cut('evtsel_hlep1_etcone20/evtsel_hlep1_pt', '<=', 0.08)
#WHall.cut('evtsel_hlep1_ptcone40/evtsel_hlep1_pt', '<=', 0.08)
#WHall.cut('evtsel_vlep1_etcone20/evtsel_vlep1_pt', '<=', 0.08)
#WHall.cut('evtsel_vlep1_ptcone40/evtsel_vlep1_pt', '<=', 0.08)
#WHall.cut('evtsel_passes_Z_mass_veto')
#WHall.cut('evtsel_tau1_et', '>', 25000)
###
########### END of subsets made to study Higgs pT dependence in VH channels


###### ZH (signal region) combined Zmm + Zee #######
zh = Subset('zh')
zh.cut('evtsel_is_ZHhadhad')
zh.cut('((evtsel_EF_mu24i_tight && evtsel_vlep1_tight) || (evtsel_EF_mu36_tight && evtsel_vlep1_tight) || (evtsel_EF_e24vhi_medium1 && evtsel_vlep1_medium) || (evtsel_EF_e60_medium1 && evtsel_vlep1_medium) )')
#zh.cut('( (evtsel_EF_mu24i_tight) || (evtsel_EF_mu36_tight) || (evtsel_EF_e24vhi_medium1) || (evtsel_EF_e60_medium1) )')
#zh.cut('(evtsel_EF_mu24i_tight && evtsel_vlep1_tight)')
#zh.cut('(evtsel_EF_e24vhi_medium1 && evtsel_vlep1_medium)')
#zh.cut('(evtsel_EF_e60_medium1 && evtsel_vlep1_medium)')
zh.cut('evtsel_nMediumTaus', '==', 2)
zh.cut('evtsel_nLeptons', '==', 2)
zh.cut('evtsel_H_m_MMC', '>', 0)
zh.cut('evtsel_tau1_charge*evtsel_tau2_charge', '==', -1)
zh.cut('evtsel_vlep1_charge*evtsel_vlep2_charge', '==', -1)
zh.cut('evtsel_vlep1_flavour==evtsel_vlep2_flavour')
zh.cut('evtsel_hasBDTLowCut')
#zh.cut('evtsel_vlep2_pt','>', 35000)
#zh.cut('evtsel_Zll_m', '<', 120000)
#zh.cut('evtsel_Zll_m', '>', 60000)
#zh.cut('((evtsel_Zll_m > 120000) || (evtsel_Zll_m < 60000))')
#zh.cut('((evtsel_H_m_MMC > 160000) || (evtsel_H_m_MMC < 80000))')
#zh.cut('evtsel_sum_tau_pt', '>', 88000)
#zh.cut('evtsel_passes_bjet_veto')
#################################################

###### ZH (signal region) combined Zmm + Zee #######
ZHlephad = Subset('ZHlephad')
ZHlephad.cut('evtsel_is_ZHlephad')
#ZHlephad.cut('(((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_lep1_flavour==13) || (evtsel_EF_e24vhi_medium1 && evtsel_lep1_flavour==11) || (evtsel_EF_e60_medium1 && evtsel_lep1_flavour==11))')
ZHlephad.cut('( (evtsel_EF_mu24i_tight) || (evtsel_EF_mu36_tight) || (evtsel_EF_e24vhi_medium1) || (evtsel_EF_e60_medium1) )')
ZHlephad.cut('evtsel_H_m_MMC', '>', 0)
ZHlephad.cut('evtsel_vlep1_charge*evtsel_vlep2_charge', '==', -1)
ZHlephad.cut('evtsel_vlep1_flavour==evtsel_vlep2_flavour')
#ZHlephad.cut('evtsel_hlep1_charge*evtsel_tau1_charge', '>', 0)
#ZHlephad.cut('((evtsel_H_m_MMC > 160000) || (evtsel_H_m_MMC < 80000))')
#zh.cut('evtsel_Zll_m', '<', 120000)
#zh.cut('evtsel_Zll_m', '>', 60000)
#zh.cut('((evtsel_Zll_m > 120000) || (evtsel_Zll_m < 60000))')
#zh.cut('((evtsel_H_m_MMC > 160000) || (evtsel_H_m_MMC < 80000))')
#zh.cut('evtsel_sum_tau_pt', '>', 70000)
#zh.cut('!evtsel_passes_bjet_veto')
#################################################

###### ZH (signal region)--Z->electrons #######
zhe = Subset('zh_ee')
zhe.cut('evtsel_is_ZHhadhad')
zhe.cut('(evtsel_EF_e24vhi_medium1 && evtsel_vlep1_medium) || (evtsel_EF_e60_medium1 && evtsel_vlep1_medium)')
zhe.cut('evtsel_vlep1_flavour','==', 11)
zhe.cut('evtsel_vlep2_flavour','==', 11)
zhe.cut('evtsel_nMediumTaus', '==', 2)
zhe.cut('evtsel_nLeptons', '==', 2)
zhe.cut('evtsel_tau1_charge*evtsel_tau2_charge', '==', -1)
zhe.cut('evtsel_vlep1_charge*evtsel_vlep2_charge', '==', -1)
zhe.cut('evtsel_H_m_MMC', '>', 0)
zhe.cut('evtsel_hasBDTLowCut')
#zhe.cut('evtsel_Zll_m', '<', 120000)
#zhe.cut('evtsel_Zll_m', '>', 60000)
#zhe.cut('evtsel_sum_tau_pt', '>', 88000)
#zhe.cut('evtsel_passes_bjet_veto')
#################################################

###### ZH (signal region)--Z->muons #######
zhm = Subset('zh_m')
zhm.cut('evtsel_is_ZHhadhad')
zhm.cut('((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_vlep1_tight)')
zhm.cut('evtsel_vlep1_flavour','==', 13)
zhm.cut('evtsel_vlep2_flavour','==', 13)
zhm.cut('evtsel_nMediumTaus', '==', 2)
zhm.cut('evtsel_nLeptons', '==', 2)
zhm.cut('evtsel_tau1_charge*evtsel_tau2_charge', '==', -1)
zhm.cut('evtsel_vlep1_charge*evtsel_vlep2_charge', '==', -1)
zhm.cut('evtsel_H_m_MMC', '>', 0)
zhm.cut('evtsel_hasBDTLowCut')
#zhm.cut('evtsel_Zll_m', '<', 120000)
#zhm.cut('evtsel_Zll_m', '>', 60000)
#zhm.cut('evtsel_sum_tau_pt', '>', 88000)
#zhm.cut('evtsel_passes_bjet_veto')
#################################################

##### ZH SR + SS taus region ############
zhss = Subset('zhss')
zhss.cut('evtsel_is_ZHhadhad')
zhss.cut('( (evtsel_EF_mu24i_tight && evtsel_vlep1_tight) || (evtsel_EF_mu36_tight && evtsel_vlep1_tight) || (evtsel_EF_e24vhi_medium1 && evtsel_vlep1_medium) || (evtsel_EF_e60_medium1 && evtsel_vlep1_medium) )')
#zhss.cut('(((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_vlep1_tight) || (evtsel_EF_e24vhi_medium1 && evtsel_vlep1_medium) || (evtsel_EF_e60_medium1 && evtsel_vlep1_medium))')
zhss.cut('evtsel_nMediumTaus', '==', 2)
zhss.cut('evtsel_nLeptons', '==', 2)
zhss.cut('evtsel_H_m_MMC', '>', 0)
zhss.cut('evtsel_tau1_charge*evtsel_tau2_charge', '==', 1)
zhss.cut('evtsel_vlep1_charge*evtsel_vlep2_charge', '==', -1)
zhss.cut('evtsel_vlep1_flavour==evtsel_vlep2_flavour')
zhss.cut('evtsel_hasBDTLowCut')
#zhss.cut('evtsel_Zll_m', '<', 120000)
#zhss.cut('evtsel_Zll_m', '>', 60000)
#zhss.cut('evtsel_sum_tau_pt', '>', 70000)
################

######### ZH MMC sideband CR #####
mmcCR = Subset('mmcCR')
mmcCR.cut('evtsel_is_ZHhadhad')
mmcCR.cut('( (evtsel_EF_mu24i_tight && evtsel_vlep1_tight) || (evtsel_EF_mu36_tight && evtsel_vlep1_tight) || (evtsel_EF_e24vhi_medium1 && evtsel_vlep1_medium) || (evtsel_EF_e60_medium1 && evtsel_vlep1_medium) )')
mmcCR.cut('evtsel_nMediumTaus', '==', 2)
mmcCR.cut('evtsel_nLeptons', '==', 2)
mmcCR.cut('evtsel_H_m_MMC', '>', 0)
mmcCR.cut('evtsel_tau1_charge*evtsel_tau2_charge', '==', -1)
mmcCR.cut('evtsel_vlep1_charge*evtsel_vlep2_charge', '==', -1)
mmcCR.cut('evtsel_vlep1_flavour==evtsel_vlep2_flavour')
#mmcCR.cut('evtsel_Zll_m', '<', 120000)
#mmcCR.cut('evtsel_Zll_m', '>', 60000)
mmcCR.cut('((evtsel_H_m_MMC > 160000) || (evtsel_H_m_MMC < 80000))')
mmcCR.cut('evtsel_hasBDTLowCut')
#######

###### ZH SR ######
zh1 = Subset('zh1')
zh1.cut('evtsel_is_ZHhadhad')
zh1.cut('(((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_lep1_flavour==13 && evtsel_vlep1_tight) || (evtsel_EF_e24vhi_medium1 && evtsel_lep1_flavour==11 && evtsel_vlep1_medium) || (evtsel_EF_e60_medium1 && evtsel_lep1_flavour==11 && evtsel_vlep1_medium))')
zh1.cut('evtsel_nMediumTaus', '==', 2)
zh1.cut('evtsel_nLeptons', '==', 2)
zh1.cut('evtsel_H_m_MMC', '>', 0)
zh1.cut('evtsel_tau1_charge*evtsel_tau2_charge', '==', 1)
zh1.cut('evtsel_vlep1_charge*evtsel_vlep2_charge', '==', -1)
zh1.cut('evtsel_vlep1_flavour==evtsel_vlep2_flavour')
zh1.cut('evtsel_Zll_m', '<', 120000)
zh1.cut('evtsel_Zll_m', '>', 60000)
zh1.cut('evtsel_sum_tau_pt', '>', 70000)
##############

##### ZH 2#####
zh2 = Subset('zh2')
zh2.cut('evtsel_is_ZHhadhad')
zh2.cut('(((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_lep1_flavour==13 && evtsel_vlep1_tight) || (evtsel_EF_e24vhi_medium1 && evtsel_lep1_flavour==11 && evtsel_vlep1_medium) || (evtsel_EF_e60_medium1 && evtsel_lep1_flavour==11 && evtsel_vlep1_medium))')
zh2.cut('evtsel_nMediumTaus', '==', 2)
zh2.cut('evtsel_nLeptons', '==', 2)
zh2.cut('evtsel_H_m_MMC', '>', 0)
zh2.cut('evtsel_tau1_charge*evtsel_tau2_charge', '==', 1)
zh2.cut('evtsel_vlep1_charge*evtsel_vlep2_charge', '==', -1)
zh2.cut('evtsel_vlep1_flavour==evtsel_vlep2_flavour')
zh2.cut('evtsel_Zll_m', '<', 120000)
zh2.cut('evtsel_Zll_m', '>', 60000)

########

####### ZH 3 #####
zh3 = Subset('zh3')
zh3.cut('evtsel_is_ZHhadhad')
zh3.cut('(((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_lep1_flavour==13 && evtsel_vlep1_tight) || (evtsel_EF_e24vhi_medium1 && evtsel_lep1_flavour==11 && evtsel_vlep1_medium) || (evtsel_EF_e60_medium1 && evtsel_lep1_flavour==11 && evtsel_vlep1_medium))')
zh3.cut('evtsel_nMediumTaus', '==', 2)
zh3.cut('evtsel_nLeptons', '==', 2)
zh3.cut('evtsel_H_m_MMC', '>', 0)
zh3.cut('evtsel_vlep1_flavour==evtsel_vlep2_flavour')
zh3.cut('evtsel_tau1_charge*evtsel_tau2_charge', '==', 1)
zh3.cut('evtsel_vlep1_charge*evtsel_vlep2_charge', '==', -1)
#######

####### ZH 4 #####
zh4 = Subset('zh4')
zh4.cut('evtsel_is_ZHhadhad')
zh4.cut('(((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_lep1_flavour==13 && evtsel_vlep1_tight) || (evtsel_EF_e24vhi_medium1 && evtsel_lep1_flavour==11 && evtsel_vlep1_medium) || (evtsel_EF_e60_medium1 && evtsel_lep1_flavour==11 && evtsel_vlep1_medium))')
zh4.cut('evtsel_nMediumTaus', '==', 2)
zh4.cut('evtsel_nLeptons', '==', 2)
zh4.cut('evtsel_H_m_MMC', '>', 0)
zh4.cut('evtsel_vlep1_flavour==evtsel_vlep2_flavour')
zh4.cut('evtsel_tau1_charge*evtsel_tau2_charge', '==', 1)
#####





##### ZH SS taus CR ######
zh_sstaus = Subset('zh_sstaus')
zh_sstaus.cut('evtsel_is_ZHhadhad')


#### ttbar dilepton filter####
dilep = Subset('dilep')
dilep.cut('evtsel_dilepton_ttbar','==',0)
###############

#################################### WH HADHAD
#################################### WH HADHAD
#################################### WH HADHAD
#### WH (signal region) ########
wh = Subset('wh')
wh.cut('evtsel_is_WHhadhad')
#wh.cut('(((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_vlep1_flavour==13 && evtsel_vlep1_tight) || (evtsel_EF_e24vhi_medium1 && evtsel_vlep1_flavour==11 && evtsel_vlep1_medium) || (evtsel_EF_e60_medium1 && evtsel_vlep1_flavour==11 && evtsel_vlep1_medium))')
wh.cut('( (evtsel_EF_mu24i_tight) || (evtsel_EF_mu36_tight) || (evtsel_EF_e24vhi_medium1) || (evtsel_EF_e60_medium1) )')
#wh.cut('((evtsel_EF_mu24i_tight) || (evtsel_EF_mu36_tight))')
#wh.cut('evtsel_vlep1_medium')
#wh.cut('((evtsel_EF_e24vhi_medium1) || (evtsel_EF_e60_medium1))')
wh.cut('evtsel_vlep1_tight')
#wh.cut('( (evtsel_EF_e24vhi_medium1) || (evtsel_EF_e60_medium1))')
wh.cut('evtsel_nMediumTaus', '==', 2)
wh.cut('evtsel_nLeptons', '==', 1)
wh.cut('evtsel_passes_isolation', '==', 1)
#wh.cut('evtsel_MET','>',20000)
#wh.cut('evtsel_tau1_passes_muveto','==', 1)
#wh.cut('evtsel_tau2_passes_muveto','==', 1)
wh.cut('evtsel_tau1_charge*evtsel_tau2_charge', '==', -1)
#wh.cut('evtsel_sum_tau_pt', '>', 100000)
#wh.cut('evtsel_transmass_vlep1MET', '>', 20000)
wh.cut('evtsel_passes_bjet_veto')
wh.cut('evtsel_hasBDTLowCut')
#wh.cut('TMath::Sqrt(TMath::Power((evtsel_tau1_eta-evtsel_tau2_eta),2)+TMath::Power(TVector2::Phi_mpi_pi((evtsel_tau1_phi-evtsel_tau2_phi)),2))', '>', 0.8)
#wh.cut('TMath::Sqrt(TMath::Power((evtsel_tau1_eta-evtsel_tau2_eta),2)+TMath::Power(TVector2::Phi_mpi_pi((evtsel_tau1_phi-evtsel_tau2_phi)),2))', '<', 2.8) #3.5
#wh.cut('evtsel_tau2_et', '>', 30000)
################


#### WH (signal region) ########
whlh = Subset('whlh_sig')
whlh.cut('evtsel_is_WHlephad')
whlh.cut('(( (evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight)) || (evtsel_EF_e24vhi_medium1) || (evtsel_EF_e60_medium1) || (evtsel_EF_2e12Tvh_loose1) || (evtsel_EF_mu18_tight_mu8_EFFS) || (evtsel_EF_e24vh_medium1_e7_medium1) || (evtsel_EF_e12Tvh_medium1_mu6_topo_medium) || (evtsel_EF_2mu13))')
#whlh.cut('( (evtsel_EF_mu24i_tight) || (evtsel_EF_mu36_tight) || (evtsel_EF_mu18_tight_mu8_EFFS) || (evtsel_EF_2mu13) )')
#whlh.cut('( (evtsel_EF_e24vhi_medium1) || (evtsel_EF_e60_medium1) || (evtsel_EF_2e12Tvh_loose1) ||  (evtsel_EF_e24vh_medium1_e7_medium1) )')
#whlh.cut('evtsel_nMediumTaus', '==', 2)
#whlh.cut('evtsel_nLeptons', '==', 1)
#whlh.cut('evtsel_tau1_passes_muveto','==', 1)
#whlh.cut('evtsel_tau2_passes_muveto','==', 1)
#whlh.cut('evtsel_hlep1_etcone20/(evtsel_hlep1_pt*0.001)', '<', 0.08)
#whlh.cut('evtsel_hlep1_ptcone40/(evtsel_hlep1_pt*0.001)', '<', 0.08)
#wh.cut('((evtsel_M2T > 120) || (evtsel_M2T < 60))')
#whlh.cut('evtsel_hlep1_charge*evtsel_tau1_charge', '==', -1)
#whlh.cut('evtsel_vlep1_charge==evtsel_hlep1_charge')
#whlh.cut('evtsel_tau1_et', '>',25000)
#whlh.cut('evtsel_passes_charges', '==', 1)
#wh.cut('evtsel_passes_isolation', '==', 1)
#wh.cut('evtsel_sum_tau_pt', '>', 70000)
#wh.cut('evtsel_transmass_vlep1MET', '>', 20000)
#whlh.cut('evtsel_passes_bjet_veto')
################


###### QCD-enriched data CR #######
qcd = Subset('qcd_cr')
qcd.cut('evtsel_is_WHhadhad')
qcd.cut('(((evtsel_EF_mu24i_tight || evtsel_EF_mu36_tight) && evtsel_vlep1_flavour==13 && evtsel_vlep1_tight) || (evtsel_EF_e24vhi_medium1 && evtsel_vlep1_flavour==11 && evtsel_vlep1_medium) || (evtsel_EF_e60_medium1 && evtsel_vlep1_flavour==11 && evtsel_vlep1_medium))')
qcd.cut('evtsel_vlep1_etcone20/(evtsel_vlep1_pt*0.001)', '<', 0.06)
qcd.cut('evtsel_vlep1_ptcone40/(evtsel_vlep1_pt*0.001)', '<', 0.06)
#qcd.cut('evtsel_transmass_vlep1MET', '<', 40000)
qcd.cut('evtsel_tau1_charge', '==', 'evtsel_tau2_charge')
qcd.cut('evtsel_vlep1_charge', '==', 'evtsel_tau1_charge')
qcd.cut('evtsel_passes_bjet_veto')
##################################################

###### ttbar CR ########
tt_cr = Subset('ttbar_cr')
tt_cr.cut('evtsel_is_WHhadhad')
tt_cr.cut('( (evtsel_EF_mu24i_tight) || (evtsel_EF_mu36_tight) || (evtsel_EF_e24vhi_medium1) || (evtsel_EF_e60_medium1) )')
tt_cr.cut('evtsel_vlep1_tight')
tt_cr.cut('evtsel_nLeptons', '==', 1)
tt_cr.cut('evtsel_nMediumTaus', '==', 2)
#tt_cr.cut('evtsel_vlep1_etcone20/(evtsel_vlep1_pt*0.001)', '<', 0.08)
#tt_cr.cut('evtsel_vlep1_ptcone40/(evtsel_vlep1_pt*0.001)', '<', 0.08)
tt_cr.cut('evtsel_passes_isolation')
tt_cr.cut('!evtsel_passes_bjet_veto')
tt_cr.cut('evtsel_hasBDTLowCut')
#tt_cr.cut('evtsel_jets_num', '>=', 2)
#tt_cr.cut('evtsel_MET', '>', 30000)
#tt_cr.cut('evtsel_transmass_lep1MET', '>', 50000)
##################################################

###### Z+Jets CR #######
z_cr = Subset('zjets_cr')
z_cr.cut('evtsel_is_WHhadhad')
z_cr.cut('( (evtsel_EF_mu24i_tight) || (evtsel_EF_mu36_tight) || (evtsel_EF_e24vhi_medium1) || (evtsel_EF_e60_medium1) )')
z_cr.cut('evtsel_vlep1_tight')
z_cr.cut('evtsel_passes_isolation', '==', 1)
z_cr.cut('evtsel_nLeptons', '==', 1)
z_cr.cut('evtsel_nMediumTaus', '==', 2)
z_cr.cut('evtsel_passes_bjet_veto')
z_cr.cut('evtsel_transmass_vlep1MET', '<', 40000)
z_cr.cut('evtsel_M2T', '<', 60)
z_cr.cut('evtsel_hasBDTLowCut')
##################################################

###### W+Jets CR #######
w_cr = Subset('wjets_cr')
w_cr.cut('evtsel_is_WHhadhad')
#w_cr.cut('TMath::Sqrt(2*evtsel_MET*evtsel_vlep1_pt*(1-TMath::Cos(TVector2::Phi_mpi_pi((evtsel_MET_phi-evtsel_vlep1_phi)))))', '>', 60000)
w_cr.cut('( (evtsel_EF_mu24i_tight) || (evtsel_EF_mu36_tight) || (evtsel_EF_e24vhi_medium1) || (evtsel_EF_e60_medium1) )')
w_cr.cut('evtsel_vlep1_tight')
w_cr.cut('evtsel_nLeptons', '==', 1)
w_cr.cut('evtsel_nMediumTaus', '==', 2)
w_cr.cut('evtsel_passes_isolation', '==', 1)
w_cr.cut('evtsel_passes_bjet_veto')
w_cr.cut('evtsel_transmass_vlep1MET', '>', 60000)
w_cr.cut('evtsel_tau1_charge*evtsel_tau2_charge', '==', 1)
w_cr.cut('evtsel_hasBDTLowCut')
#################################################

###### M2T sideband CR ###########
m2t = Subset('m2t')
m2t.cut('evtsel_is_WHhadhad')
m2t.cut('( (evtsel_EF_mu24i_tight) || (evtsel_EF_mu36_tight) || (evtsel_EF_e24vhi_medium1) || (evtsel_EF_e60_medium1) )')
m2t.cut('evtsel_vlep1_tight')
m2t.cut('evtsel_nMediumTaus', '==', 2)
m2t.cut('evtsel_nLeptons', '==', 1)
m2t.cut('evtsel_passes_isolation', '==', 1)
m2t.cut('((evtsel_M2T > 120) || (evtsel_M2T < 60))')
m2t.cut('evtsel_passes_bjet_veto')
m2t.cut('evtsel_hasBDTLowCut')
##################################################

##### SS taus CR #####################
sstaus = Subset('sstaus')
sstaus.cut('evtsel_is_WHhadhad')
sstaus.cut('( (evtsel_EF_mu24i_tight) || (evtsel_EF_mu36_tight) || (evtsel_EF_e24vhi_medium1) || (evtsel_EF_e60_medium1) )')
sstaus.cut('evtsel_vlep1_tight')
sstaus.cut('evtsel_nMediumTaus', '==', 2)
sstaus.cut('evtsel_nLeptons', '==', 1)
sstaus.cut('evtsel_passes_isolation')
sstaus.cut('evtsel_tau1_charge*evtsel_tau2_charge', '==', 1)
sstaus.cut('evtsel_passes_bjet_veto')
sstaus.cut('evtsel_hasBDTLowCut')
#######################



######### EXTRAS EXTRAS EXTRAS EXTRAS #################
# ######## Anti-tau events #1 ########
# antitau = Subset('antitau')
# #antitau.cut('!evtsel_is_tau')
# antitau.cut('!evtsel_is_real')
# antitau.cut('evtsel_nAntiElectrons_Selected', '==', 0)
# antitau.cut('evtsel_nAntiMuons_Selected', '==', 0)
# antitau.cut('evtsel_nAntiTaus_Selected','==', 2)
# antitau.cut('evtsel_tau1_is_AntiTau','==',1)
# antitau.cut('evtsel_tau2_is_AntiTau', '==', 1)
# #################################
# ####### Anti-tau events #2 #########
# antitau2 = Subset('antitau2')
# #antitau2.cut('!evtsel_is_tau')
# antitau2.cut('!evtsel_is_real')
# antitau2.cut('evtsel_nAntiElectrons_Selected', '==', 0)
# antitau2.cut('evtsel_nAntiMuons_Selected', '==', 0)
# antitau2.cut('evtsel_nAntiTaus_Selected','==',1)
# antitau2.cut('evtsel_tau1_is_AntiTau', '==',1)
# antitau2.cut('evtsel_tau2_is_AntiTau', '==', 0)
# #################################
# ######## Anti-tau events #3 ########
# antitau3 = Subset('antitau3')
# #antitau3.cut('!evtsel_is_tau')
# antitau3.cut('!evtsel_is_real')
# antitau3.cut('evtsel_nAntiElectrons_Selected', '==', 0)
# antitau3.cut('evtsel_nAntiMuons_Selected', '==', 0)
# antitau3.cut('evtsel_nAntiTaus_Selected', '==', 1)
# antitau3.cut('evtsel_tau1_is_AntiTau', '==', 0)
# antitau3.cut('evtsel_tau2_is_AntiTau','==', 1)
# ##############################

#####Observing WH but with only one tau fake, region 1 #####
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
