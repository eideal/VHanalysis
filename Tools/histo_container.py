import ROOT

def is_signal(name):
    supergroup_name = name.split('_')[-1].lower()
    if 'wh' in supergroup_name: return True
    if 'zh' in supergroup_name: return True
    if 'ggh' in supergroup_name: return True
    if 'vbfh' in supergroup_name: return True
    return False

class Region(list):

    def __init__(self, name):
        self.name = name
        
        
    def add(self, name, th1f):
        self.append((name, th1f))
    
   
        
class HistoContainer(dict):

    def __init__(self, name):
        self.name = name
        self.masses = [100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150]
        self.rootfile_name = self.name + '.root'
        

    def add_region(self, region_name):
        self[region_name] = Region(region_name)


    def add(self, region_name, name, th1f):
        self[region_name].add(name, th1f)
        
    
    def save(self):
        f = ROOT.TFile(self.rootfile_name, 'recreate')

        for region in self.itervalues():
            for histogram in region:
                name = histogram[0]
                th1f = histogram[1]

                th1f.SetName(name)
                th1f.Write()
        
        f.Close()
        
    
    def make_workspace(self):
        """
        Makes the HistFactory Workspace
        """

        for mass in self.masses:

            #Set up the combination measurement
            combination_measurement = ROOT.RooStats.HistFactory.Measurement('VHhh_%d' % mass, 'VHhh_%d' % mass)
            combination_measurement.SetOutputFilePrefix('./results/MEAS')
            combination_measurement.SetPOI('SigXsecOverSM')
            combination_measurement.AddConstantParam('Lumi')
            combination_measurement.AddConstantParam('mu_XS8_ggH')
            combination_measurement.AddConstantParam('mu_XS8_VBF')
            combination_measurement.AddConstantParam('mu_XS8_WH')
            combination_measurement.AddConstantParam('mu_XS8_ZH')
            combination_measurement.SetLumi(1.0)
            combination_measurement.SetLumiRelErr(0.028)
            combination_measurement.SetExportOnly(True)
            combination_measurement.SetParamValue('BinHigh', 40)

            for region in self.itervalues():
                #Instantiate channel object
                channel = ROOT.RooStats.HistFactory.Channel(region.name) # e.g. WeHtt, WmuHtt, ZmumuHtt, ZeeHtt

                #Set error configuration
                channel.SetStatErrorConfig(0.05, 'Poisson') ### 5% threshold on the relative stat. error per bin such that the stat. error is considered, can be changed. Relative error computed by Poisson relative error (not exactly sqrt(N)/N, but something like that)

                ## Sanity check for data
                has_data = False
                
                for histogram in region:
                    histogram_name = histogram[0]

                    ## handle data
                    if 'data' in histogram_name.lower():
                        if has_data:
                            raise ValueError, "There should only be one data histogram"
                        channel.SetData(histogram_name, self.rootfile_name)
                        has_data = True

                    ## handle signal
                    else:
                        if is_signal(histogram_name):
                            if str(mass) in histogram_name:
                                sample = ROOT.RooStats.HistFactory.Sample(histogram_name, histogram_name, self.rootfile_name)
                                sample.AddNormFactor('SigXsecOverSM', 0.0, 0.0, 40.0)

                                if 'ggh' in histogram_name.lower():
                                    sample.AddNormFactor('mu_XS8_ggH', 1.0, 0.0, 200.0)

                                if 'vbfh' in histogram_name.lower():
                                    sample.AddNormFactor('mu_XS8_VBF', 1.0, 0.0, 200.0)

                                if 'wh' in histogram_name.lower():
                                    sample.AddNormFactor('mu_XS8_WH', 1.0, 0.0, 200.0)

                                if 'zh' in histogram_name.lower():
                                    sample.AddNormFactor('mu_XS8_ZH', 1.0, 0.0, 200.0)

                                sample.SetNormalizeByTheory(True)
                            else:
                                continue

                        ## handle backgrounds
                        else:
                            sample = ROOT.RooStats.HistFactory.Sample(histogram_name, histogram_name, self.rootfile_name)
                            sample.ActivateStatError()
                            sample.SetNormalizeByTheory(False)

                        channel.AddSample(sample)

                combination_measurement.AddChannel(channel)

            ## Now that the workspace is specified create it
            combination_measurement.CollectHistograms()
            combination_measurement.PrintTree()

            ## Dump xml file
            combination_measurement.PrintXML(self.name, '')

            ## Make the workspace
            ROOT.RooStats.HistFactory.MakeModelAndMeasurementFast(combination_measurement)

                        
                    
                        
                    
                
                  
                 
                 
                 

             
        
