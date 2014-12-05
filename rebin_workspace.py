import ROOT
from math import sqrt

plots_file = ROOT.TFile('workspaceAllMC_rebinned.root')

new_file = ROOT.TFile('rebinned_workspace.root', 'RECREATE')
new_file.cd()


def rebin(h, channel):

	if channel == 'wh':
		bins = [(25,60),(60,80),(80,90),(90,100),(100,110),(110,130),(130,160),(160,200)]
	elif channel == 'zh': 
		bins = [(25,80),(80,110),(110,130),(130,150),(150,225)]

	new_bin_content = []
	new_bin_error = []

	nbins = h.GetNbinsX() # 1000 bins
	xaxis = h.GetXaxis()

	for (start, end) in bins:
		full_content = 0
		full_error   = 0

		for i in range(1, nbins+1):
			bin_content = h.GetBinContent(i)
			bin_error   = h.GetBinError(i)
			bin_lo_edge = xaxis.GetBinLowEdge(i)
			bin_hi_edge = xaxis.GetBinUpEdge(i)
			
			if bin_lo_edge >= start and bin_hi_edge < end:
				full_content += bin_content
				full_error   += bin_error**2
		
		new_bin_content.append(full_content)
		new_bin_error.append(sqrt(full_error))

	return (new_bin_content, new_bin_error)
		


for keys in plots_file.GetListOfKeys():

	hist_name = keys.GetName()
	histogram_name = str(hist_name)

	if 'wh' in hist_name.lower() and not 'data' in hist_name.lower():
		#if 'AntitauEvents' in hist_name and 'TAU_FF' in hist_name:
			print 'Working on histogram', hist_name
			new_hist = ROOT.TH1F(histogram_name, histogram_name, 8, 0, 1)
			hist = plots_file.Get(hist_name)
			list_bin_content, list_bin_error = rebin(hist, 'wh')

			for i in range(1, 9):
				new_hist.SetBinContent(i, list_bin_content[i-1])
				new_hist.SetBinError(i, list_bin_error[i-1])

			new_hist.Write()


	elif 'zh' in hist_name.lower() and not 'data' in hist_name.lower():
		#if 'AntitauEvents' in hist_name and 'TAU_FF' in hist_name:
			print 'Working on histogram', hist_name
			new_hist = ROOT.TH1F(histogram_name,histogram_name, 5, 0, 1)
			hist = plots_file.Get(hist_name)
			list_bin_content, list_bin_error = rebin(hist, 'zh')

			for i in range(1, 6):
				new_hist.SetBinContent(i, list_bin_content[i-1])
				new_hist.SetBinError(i, list_bin_error[i-1])
	
			new_hist.Write()

	elif 'wh' in hist_name.lower() and 'data' in hist_name.lower():

		

new_file.Close()





