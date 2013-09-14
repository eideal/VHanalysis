from plotinfo_container import plotinfo_container

plots = plotinfo_container()

#plots.Add('evtsel_MET','_HH', 15, 0, 100, 'MET[GeV]', 0.001, False)
plots.Add('evtsel_MET1', '_HH', 15,0,100, 'MET[GeV]', 0.001, False)
#plots.Add('evtsel_MET_phi','_HH', 15, -4, 8, 'evtsel_MET_phi', 1, False)
plots.Add('evtsel_tau1_et', '_HH', 20,20,80, 'evtsel_tau1_et', 0.001, False)

#plots.Add('evtsel_lep3_pt', '', 20,0,50, 'evtsel_lep3_pt', 0.001, False)
#plots.Add('evtsel_lep2_pt', 'WJetsmedID', 15,0,75, 'evtsel_lep2_pt', 0.001, False)
#plots.Add('evtsel_nLeptons', '_HH', 5,0,5, 'evtsel_nLeptons',1,False)
#plots.Add('evtsel_weight', 'ZH125', 20, -10, 10, 'evtsel_weight', 1, False)
#plots.Add('evtsel_lep2_flavour', '', 32, -16, 16, 'evtsel_lep2_flavour', 1, False)
#plots.Add('evtsel_vlep1_z0', 'WJetsmedID', 50,-150, 150, 'evtsel_vlep1_z0', 1, False)
#plots.Add('evtsel_vlep2_z0', 'WJetsmedID', 50,-150, 150, 'evtsel_vlep2_z0', 1, False)
#plots.Add('evtsel_hlep1_z0', 'WJetsmedID', 50,-250, 250, 'evtsel_hlep1_z0', 1, False)

#plots.Add('evtsel_hlep1_pt', '_HH', 20,0,110, 'evtsel_hlep1_pt', 0.001, False)
plots.Add('evtsel_vlep1_pt', '_HH', 20,0,110, 'evtsel_vlep1_pt', 0.001, False)
plots.Add('evtsel_vlep1_eta', '_HH', 20,-3.5,6, 'evtsel_vlep1_eta', 1, False)
plots.Add('evtsel_vlep1_phi', '_HH', 20,-4,8, 'evtsel_vlep1_phi', 1, False)
plots.Add('evtsel_H_m_vis', '_HH', 30,0,300, 'evtsel_H_m_vis', 1, False)

#plots.Add('evtsel_vlep2_pt', '_ZH125', 50,0,200, 'evtsel_vlep2_pt', 0.001, False)
#plots.Add('evtsel_lep1_phi', 'HH', 30,-4,8, 'evtsel_lep1_phi', 1, False)
#plots.Add('evtsel_lep1_eta', 'HH', 30,-3.5,6, 'evtsel_lep1_eta', 1, False)
#plots.Add('evtsel_lep1_pt', 'HH', 40, 0, 200, 'evtsel_lep1_pt', 0.001, False)
#plots.Add('evtsel_nLooseTaus', 'WJetsmedID', 5,0,5, 'evtsel_nLooseTaus', 1, False)
#plots.Add('evtsel_nMediumTaus', 'WJetsmedID', 5,0,5, 'evtsel_nMediumTaus', 1, False)

plots.Add('evtsel_tau1_phi', '_HH', 20,-4,8, 'evtsel_tau1_phi', 1, False)
plots.Add('evtsel_tau1_JetBDTScore', '_HH', 15,0.4,1, 'evtsel_tau1_JetBDTScore', 1, False)

# plots.Add('evtsel_vlep1_etcone20', '', 50,0,200, 'evtsel_vlep1_etcone20', 0.001, False)

plots.Add('evtsel_tau1_eta', '_HH', 15,-3.5,6, 'evtsel_tau1_eta', 1, False)

# plots.Add('evtsel_vlep1_ptcone40', '', 50,0,200, 'evtsel_vlep1_ptcone40', 0.001, False)
#plots.Add('evtsel_tau1_et','_BG+SIG', 60, 0, 900, '#tau_{1} p_{T}', 0.001, False)
#plots.Add('evtsel_vlep1_pt','_', 100, 0, 400, 'vlep_{1} p_{T}', 0.001, True)

        
