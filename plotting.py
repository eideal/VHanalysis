from plotinfo_container import plotinfo_container
from Tools import palette
import math

plots = plotinfo_container()

#plots.Add('evtsel_weight_FF', '_totalTEST', 45, -0.04, 0.15, palette.green, 'fill', 'OldFakes', 'evtsel_weight_FF', 1, False, False)
#plots.Add('newFF', '_totalTEST', 45, -0.04, 0.15, palette.blue, 'line', 'NewFakes','newFF', 1, False, False)

#plots.Add('evtsel_nAntiTaus', '_totalTEST', 15,0, 15, palette.green, 'fill', 'nothing', 'evtsel_nAntiTaus', 1, False, False)
#plots.Add('evtsel_trueHiggs_pt', '', 15, 0, 300, palette.green, 'fill', 'nothing', 'pT Higgs', 1, False, False) 

plots.Add('evtsel_tau1_et', '', 6,50,150, palette.green, 'fill', 'nothing', 'E_{T}^{#tau_{1}} [GeV]', 0.001, False, False)
#plots.Add('evtsel_tau1_et', '', 5,40,130, palette.green, 'fill', 'nothing', 'E_{T}^{#tau_{1}} [GeV]', 0.001, False, False)
#plots.Add('evtsel_Zll_m', '', 20,0, 250, palette.green, 'fill', 'nothing', 'M_{ll} [GeV]', 0.001, False, False)
#plots.Add('evtsel_dR','', 20, 0, 8, palette.green, 'fill', 'nothing', '#DeltaR(#tau_{1},#tau_{2})', 1, False, False)
#plots.Add('evtsel_V_pt','_totalTEST', 20, 0, 200, palette.green, 'fill','nothing', 'V_pt', 0.001, False, False)
plots.Add('evtsel_sum_tau_pt', '', 5, 80, 230, palette.green, 'fill', 'nothing', 'E_{T}^{#tau_{1}} + E_{T}^{#tau_{2}} [GeV]', 0.001, False, False)
#plots.Add('evtsel_sum_tau_pt', '', 6, 100, 220, palette.green, 'fill', 'nothing', 'E_{T}^{#tau_{1}} + E_{T}^{#tau_{2}} [GeV]', 0.001, False, False)
#plots.Add('evtsel_jets_num', '_totalTEST', 10, 0, 10, 'evtsel_jets_num', 1, False)


#plots.Add('evtsel_sum_lep_pt', '_totalTEST', 10, 50, 400, 'sum_lep_pt', 0.001, False, False)
#plots.Add('evtsel_transmass_vlep1MET', '_totalTEST', 20, 0, 200, palette.green, 'fill', 'nothing', 'm_{T}(vlep_{1}, MET) [GeV]', 0.001, False, False)
#plots.Add('evtsel_transmass_tau1MET', '_totalTEST', 15, 0, 300, palette.green, 'fill', 'nothing', 'transmass_tau1MET', 0.001, False, False)
#plots.Add('evtsel_transmass_tau2MET', '_totalTEST', 15, 0, 300, palette.green, 'fill', 'nothing', 'transmass_tau2MET', 0.001, False, False)
plots.Add('evtsel_MET','', 8, 0, 150, palette.green, 'fill','nothing', 'MET [GeV]', 0.001, False, False)
#plots.Add('evtsel_caloiso', '_WHhhcat', 30, -0.5, 1, palette.green, 'fill', 'nothing', 'calo_iso', 1, False, False)
#plots.Add('evtsel_trackiso', '_WHhhcat', 30, -0.5, 1, palette.green, 'fill', 'nothing', 'track_iso', 1, False, False)
#plots.Add('evtsel_MET_sig','_totalTEST', 20, 0, 400, palette.green, 'fill','nothing', 'MET_sig', 1, False, False)
#plots.Add('evtsel_V_pt_vis','_totalTEST', 20, 0, 200, palette.green, 'fill','nothing', 'V_pt_vis', 0.001, False, False)
#plots.Add('evtsel_H_m_vis', '_totalTEST', 7,25,200, palette.green, 'fill', 'nothing', 'H_m_vis', 0.001, False, True)
#plots.Add('evtsel_nLeptons', '', 2,0,3, palette.green, 'fill', 'nothing', 'Background Composition',1,False, False)
#plots.Add('evtsel_nLeptons', '', 2,1,3, palette.green, 'fill', 'nothing', 'Background Composition',1,False, False)
#plots.Add('evtsel_MET_phi', '_total', 15, -math.pi, 2*math.pi, palette.green, 'fill', 'nothing', 'MET_phi', 1, False, False)

#plots.Add('evtsel_H_m_MMC', '', 10,0,350, palette.green, 'fill', 'nothing', 'm_{MMC} [GeV]', 0.001, False, False)
#plots.Add('evtsel_H_m_MMC', '', 5,25,225, palette.green, 'fill', 'nothing', 'm_{MMC} [GeV]', 0.001, False, False)
#plots.Add('evtsel_H_m_MMC', '_totalTEST', 5,25,225, palette.green, 'fill', 'nothing', 'm_{MMC}', 0.001, False, True)
#plots.Add('evtsel_H_m_MMC', '_totalTEST', 1,25,225, palette.green, 'fill', 'nothing', 'm_{MMC}', 0.001, False, True)
plots.Add('evtsel_M2T', '_totalTEST', 8, 25, 200, palette.green, 'fill', 'nothing', 'M_{2T} [GeV]', 1, False, True)
#plots.Add('evtsel_M2T', '_totalTEST', 8, 25, 210, palette.green, 'fill', 'nothing', 'M_{2T} [GeV]', 1, False, False)
#plots.Add('evtsel_M2T', '', 15, 20, 220, palette.green, 'fill', 'nothing', 'M_{2T} [GeV]', 1, False, False)
#plots.Add('evtsel_vlep1_pt', '',5,20,150, palette.green, 'fill', 'nothing', 'p_{T}^{l_{1}} [GeV]', 0.001, False, False)
#plots.Add('evtsel_dPhi', '_totalTEST', 15, -math.pi , 2*math.pi, palette.green, 'fill', 'nothing', 'dPhi(tau1,tau2)', 1, False, False)

#plots.Add('evtsel_hlep1_pt', '_totalTEST',20,0,200, palette.green, 'fill', 'nothing', 'hlep1_pt', 0.001, False, False)
#plots.Add('evtsel_vlep2_pt', '',10,20,150, palette.green, 'fill', 'nothing', 'p_{T}^{l_{2}}', 0.001, False, False)
#plots.Add('evtsel_tau2_et', '', 5, 20, 100, palette.green, 'fill', 'nothing', 'E_{T}^{#tau_{2}} [GeV]', 0.001, False, False)
#plots.Add('evtsel_dEta', '_totalTEST', 10, 0, 5, palette.green, 'fill', 'nothing', 'dEta(tau1,tau2)', 1, False, False)
#plots.Add('evtsel_tau1_phi', '_totalTEST', 15, -math.pi, 2*math.pi, palette.green, 'fill', 'nothing', 'tau1_phi', 1, False, False)
#plots.Add('evtsel_tau1_eta', '_totalTEST', 20,-5,5, palette.green, 'fill', 'nothing', 'tau1_eta', 1, False, False)

#plots.Add('evtsel_MET_OSMC','_OSMC', 30, 0, 300, 'evtsel_MET', 0.001, False)
#plots.Add('evtsel_MET_SSSMC', '_SSSMC', 30,0,300, 'evtsel_MET', 0.001, False)
#plots.Add('evtsel_MET_SSSdata', '_SSSdata', 30,0,300, 'evtsel_MET', 0.001, False)

#plots.Add('evtsel_jets_num', '_WHhh',10,0,10, 'evtsel_jets_num', 1, False)
#plots.Add('evtsel_jets_num_PreOverlap', '_WHhh', 1,0, 20, 'evtsel_jets_num_PreOverlap', 1, False)

#plots.Add('evtsel_tau1_weight_medium', '_WHhh',10, 0,2, 'evtsel_tau1_weight_medium', 1, False)
#plots.Add('evtsel_MET1', '_LH', 50,0,100, 'MET[GeV]', 0.001, False)
#plots.Add('evtsel_MET_phi','_WHhh', 15, -4, 8, 'evtsel_MET_phi', 1, False)

#plots.Add('evtsel_tau1_et_failL', '', 30,0,300, 'evtsel_tau1_et_failL', 0.001, False)
#plots.Add('evtsel_tau1_et_passL', '', 30,0,300, 'evtsel_tau1_et_passL', 0.001, False)

#plots.Add('evtsel_vlep1_truth_type','_WHhh', 40, -20,20 , 'evtsel_vlep1_truth_type', 1, False)
#plots.Add('evtsel_hlep1_truth_type','_WHhh', 40, -20,20 , 'evtsel_hlep1_truth_type', 1, False)
#plots.Add('evtsel_vlep2_truth_type','_WHhh', 40, -20,20 , 'evtsel_vlep2_truth_type', 1, False)
#plots.Add('evtsel_tau1_truth_type','_WHhh', 40, 0,40 , 'evtsel_tau1_truth_type', 1, False)
#plots.Add('evtsel_tau2_truth_type','_WHhh', 5, 20,25 , 'evtsel_tau2_truth_type', 1, False)

#plots.Add('evtsel_lep3_pt', '', 20,0,50, 'evtsel_lep3_pt', 0.001, False)
#plots.Add('evtsel_lep2_pt', '_WHhh', 38,0,76, 'evtsel_lep2_pt', 0.001, False)
#plots.Add('evtsel_nLeptons', '_WHhh', 1,0,10, 'evtsel_nLeptons',1,False, False)
#plots.Add('evtsel_weight', 'WHhh125', 20, -10, 10, 'evtsel_weight', 1, False)
#plots.Add('evtsel_lep2_flavour', '', 32, -16, 16, 'evtsel_lep2_flavour', 1, False)
#plots.Add('evtsel_vlep1_z0', '_WHhh', 15,10, 100, 'evtsel_vlep1_z0', 1, False)
#plots.Add('evtsel_V_m_vis', '_WHhh', 30,0, 300, 'evtsel_V_m_vis', 0.001, False)
#plots.Add('evtsel_V_pt_vis', '_WHhh', 30,0, 300, 'evtsel_V_pt_vis', 0.001, False)

#plots.Add('evtsel_vlep2_z0', '_WHhh', 15,-20, 20, 'evtsel_vlep2_z0', 1, False)
#plots.Add('evtsel_hlep1_z0', 'WHhh', 50,-250, 250, 'evtsel_hlep1_z0', 1, False)

#plots.Add('evtsel_hlep1_pt', '_WHhh', 20,0,110, 'evtsel_hlep1_pt', 0.001, False)
#plots.Add('evtsel_dphi', '_WHhh', 25, -4, 8, 'evtsel_dphi', 1, False)
#plots.Add('evtsel_deta', '_WHhh', 25, -5, 10, 'evtsel_deta', 1, False)

# plots.Add('evtsel_vlep1_eta', '_WHhh', 15,-3.5,6, 'evtsel_vlep1_eta', 1, False)
# plots.Add('evtsel_vlep1_phi', '_WHhh', 15,-4,8, 'evtsel_vlep1_phi', 1, False)
#plots.Add('evtsel_vlep2_pt', '_WHhh', 38,0,76, 'evtsel_vlep2_pt', 0.001, False)
#plots.Add('evtsel_lep1_phi', 'WHhh', 30,-4,8, 'evtsel_lep1_phi', 1, False)
#plots.Add('evtsel_lep1_eta', 'WHhh', 30,-3.5,6, 'evtsel_lep1_eta', 1, False)
#plots.Add('evtsel_lep1_pt', '_WHhh', 30, 0, 300, 'evtsel_lep1_pt', 0.001, False)
#plots.Add('evtsel_nLooseTaus', 'WHhh', 5,0,5, 'evtsel_nLooseTaus', 1, False)
#plots.Add('evtsel_nMediumTaus', 'WHhh', 5,0,5, 'evtsel_nMediumTaus', 1, False)
# plots.Add('evtsel_tau1_JetBDTScore', '_WHhh', 15,0.4,1.2, 'evtsel_tau1_JetBDTScore', 1, False)

# plots.Add('evtsel_vlep1_etcone20', '', 50,0,200, 'evtsel_vlep1_etcone20', 0.001, False)
# plots.Add('evtsel_vlep1_ptcone40', '', 50,0,200, 'evtsel_vlep1_ptcone40', 0.001, False)
#plots.Add('evtsel_vlep1_pt','_', 100, 0, 400, 'vlep_{1} p_{T}', 0.001, True)


