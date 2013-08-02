from plotinfo_container import plotinfo_container

plots = plotinfo_container()

plots.Add('evtsel_MET', 100, 0, 1000, 'MET[GeV]', 0.001, True) 
plots.Add('evtsel_tau1_pt', 100, 0, 400, '#tau_{1} p_{T}', 0.001, True)

        
