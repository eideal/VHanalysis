import ROOT

## e.g. ZH125
def is_signal(name):
    supergroup_name = name.split('_')[-1].lower()
    if 'wh' in supergroup_name: return True
    if 'zh' in supergroup_name: return True
    if 'ggh' in supergroup_name: return True
    if 'vbfh' in supergroup_name: return True
    return False

## e.g. ZZ_zerofakes
def is_BG(name): 
    supergroup_name = name.split('_')[-2].lower()
    if 'zz' in supergroup_name: return True
    if 'wz' in supergroup_name: return True
    if 'tt' in supergroup_name: return True
    if 'ztautau' in supergroup_name: return True
    if 'triboson' in supergroup_name: return True
    return False

## e.g. AntitauEvents
def is_fakes(name):
    supergroup_name = name.split('_')[-1].lower()
    if 'antitauevents' in supergroup_name: return True
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

        Systematics = False

        
        for mass in self.masses:
    #goal: create a workspace by recording the structure of the analysis: channels, BGs, signals, and systematics. makes a root file that you feed to the scripts which give the limits and significances
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
                    if 'ATLAS' in histogram_name: continue

                    ## handle data
                    if 'data' in histogram_name.lower():
                        if has_data:
                            if not 'ATLAS' in histogram_name:
                                raise ValueError, "There should only be one data histogram"
                        if not 'ATLAS' in histogram_name:
                            channel.SetData(histogram_name, self.rootfile_name)
                            has_data = True


                    ## handle signal
                    else:
                        if is_signal(histogram_name):
                            if str(mass) in histogram_name:
                                sample = ROOT.RooStats.HistFactory.Sample(histogram_name, histogram_name, self.rootfile_name)
                                    
                                supergroup_name = histogram_name.split('_')[-1]
                                
                                sample.AddNormFactor('SigXsecOverSM', 0.0, 0.0, 40.0)
                                sample.AddOverallSys('ATLAS_LUMI_2012', 0.972, 1.028)

                                if Systematics:
                                    sample.AddOverallSys('ATLAS_LUMI_2012', 0.972, 1.028)
                                    ### sample.AddHistoSys('ATLAS_EL_FF','%s_ATLAS_EL_FF_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name, '', '%s_ATLAS_EL_FF_UP_%s' % (region.name, supergroup_name), self.rootfile_name, '')
                                    sample.AddHistoSys('ATLAS_EL_ID','%s_ATLAS_EL_ID_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_EL_ID_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                    sample.AddHistoSys('ATLAS_EL_ISO','%s_ATLAS_EL_ISO_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name, '', '%s_ATLAS_EL_ISO_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                    sample.AddHistoSys('ATLAS_EL_LOWPT','%s_ATLAS_EL_LOWPT_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_EL_LOWPT_UP_%s' % (region.name, supergroup_name),self.rootfile_name ,'')
                                    sample.AddHistoSys('ATLAS_EL_PS','%s_ATLAS_EL_PS_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_EL_PS_UP_%s' % (region.name, supergroup_name), self.rootfile_name, '')
                                    sample.AddHistoSys('ATLAS_EL_R12','%s_ATLAS_EL_R12_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_EL_R12_UP_%s' % (region.name, supergroup_name), self.rootfile_name, '')
                                    sample.AddHistoSys('ATLAS_EL_RES','%s_ATLAS_EL_RES_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_EL_RES_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                    sample.AddHistoSys('ATLAS_EL_TRIG','%s_ATLAS_EL_TRIG_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_EL_TRIG_UP_%s' % (region.name, supergroup_name), self.rootfile_name ,'')
                                    sample.AddHistoSys('ATLAS_EL_ZEE','%s_ATLAS_EL_ZEE_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_EL_ZEE_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                    sample.AddHistoSys('ATLAS_JER_2012','%s_ATLAS_JER_2012_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_JER_2012_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                    sample.AddHistoSys('ATLAS_JES_2012_Detector1','%s_ATLAS_JES_2012_Detector1_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_JES_2012_Detector1_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                    sample.AddHistoSys('ATLAS_JES_2012_Eta_StatMethod','%s_ATLAS_JES_2012_Eta_StatMethod_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_JES_2012_Eta_StatMethod_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                    sample.AddHistoSys('ATLAS_JES_2012_EtaModelling','%s_ATLAS_JES_2012_EtaModelling_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_JES_2012_EtaModelling_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                    sample.AddHistoSys('ATLAS_JES_2012_Modelling1','%s_ATLAS_JES_2012_Modelling1_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_JES_2012_Modelling1_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                    sample.AddHistoSys('ATLAS_JES_2012_PileRho_TAU','%s_ATLAS_JES_2012_PileRho_TAU_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_JES_2012_PileRho_TAU_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                    sample.AddHistoSys('ATLAS_JES_2012_Statistical1','%s_ATLAS_JES_2012_Statistical1_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_JES_2012_Statistical1_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                    sample.AddHistoSys('ATLAS_JES_FlavComp_TAU','%s_ATLAS_JES_FlavComp_TAU_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_JES_FlavComp_TAU_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                    sample.AddHistoSys('ATLAS_JES_Flavb','%s_ATLAS_JES_Flavb_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_JES_Flavb_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                    sample.AddHistoSys('ATLAS_JES_FlavResp','%s_ATLAS_JES_FlavResp_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_JES_FlavResp_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                    sample.AddHistoSys('ATLAS_JES_Mu','%s_ATLAS_JES_Mu_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_JES_Mu_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                    sample.AddHistoSys('ATLAS_JES_NPV','%s_ATLAS_JES_NPV_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_JES_NPV_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                    sample.AddHistoSys('ATLAS_JVF_2012','%s_ATLAS_JVF_2012_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_JVF_2012_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                    sample.AddHistoSys('ATLAS_MET_RESOSOFT','%s_ATLAS_MET_RESOSOFT_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_MET_RESOSOFT_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                    sample.AddHistoSys('ATLAS_MET_SCALESOFT','%s_ATLAS_MET_SCALESOFT_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_MET_SCALESOFT_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                    ###sample.AddHistoSys('ATLAS_MU_FF','%s_ATLAS_MU_FF_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_MU_FF_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                    sample.AddHistoSys('ATLAS_MU_ID','%s_ATLAS_MU_ID_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_MU_ID_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                    sample.AddHistoSys('ATLAS_MU_ISO','%s_ATLAS_MU_ISO_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_MU_ISO_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                    sample.AddHistoSys('ATLAS_MU_MS','%s_ATLAS_MU_MS_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_MU_MS_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                    sample.AddHistoSys('ATLAS_MU_TRIG','%s_ATLAS_MU_TRIG_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_MU_TRIG_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                    ###sample.AddHistoSys('ATLAS_PU_RESCALE_2012','%s_ATLAS_PU_RESCALE_2012_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_PU_RESCALE_2012_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                    sample.AddHistoSys('ATLAS_TAU_EFAKE_2012','%s_ATLAS_TAU_EFAKE_2012_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_TAU_EFAKE_2012_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                    ###sample.AddHistoSys('ATLAS_TAU_FF','%s_ATLAS_TAU_FF_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_TAU_FF_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                    sample.AddHistoSys('ATLAS_TAU_ID_2012','%s_ATLAS_TAU_ID_2012_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_TAU_ID_2012_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                    sample.AddHistoSys('ATLAS_TAU_ID_STAT_2012','%s_ATLAS_TAU_ID_STAT_2012_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_TAU_ID_STAT_2012_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                    sample.AddHistoSys('ATLAS_TES_TRUE_2012','%s_ATLAS_TES_TRUE_2012_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_TES_TRUE_2012_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                

                                if 'ggh' in histogram_name.lower():
                                    sample.AddNormFactor('mu_XS8_ggH', 1.0, 0.0, 200.0)

                                elif 'vbfh' in histogram_name.lower():
                                    sample.AddNormFactor('mu_XS8_VBF', 1.0, 0.0, 200.0)

                                elif 'wh' in histogram_name.lower():
                                    sample.AddNormFactor('mu_XS8_WH', 1.0, 0.0, 200.0)

                                elif 'zh' in histogram_name.lower():
                                    sample.AddNormFactor('mu_XS8_ZH', 1.0, 0.0, 200.0)

                                    
                            else:
                                continue

                        ## handle backgrounds
                        elif is_BG(histogram_name):
                            sample = ROOT.RooStats.HistFactory.Sample(histogram_name, histogram_name, self.rootfile_name)

                            supergroup_name = histogram_name.split('_')[-2] + '_' + histogram_name.split('_')[-1]
                            
                            sample.ActivateStatError()
                            sample.AddOverallSys('ATLAS_LUMI_2012', 0.972, 1.028)

                            if Systematics:
                                sample.AddOverallSys('ATLAS_LUMI_2012', 0.972, 1.028)
                                ### sample.AddHistoSys('ATLAS_EL_FF','%s_ATLAS_EL_FF_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_EL_FF_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                sample.AddHistoSys('ATLAS_EL_ID','%s_ATLAS_EL_ID_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_EL_ID_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                sample.AddHistoSys('ATLAS_EL_ISO','%s_ATLAS_EL_ISO_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_EL_ISO_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                sample.AddHistoSys('ATLAS_EL_LOWPT','%s_ATLAS_EL_LOWPT_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_EL_LOWPT_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                sample.AddHistoSys('ATLAS_EL_PS','%s_ATLAS_EL_PS_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_EL_PS_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                sample.AddHistoSys('ATLAS_EL_R12','%s_ATLAS_EL_R12_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_EL_R12_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                sample.AddHistoSys('ATLAS_EL_RES','%s_ATLAS_EL_RES_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_EL_RES_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                sample.AddHistoSys('ATLAS_EL_TRIG','%s_ATLAS_EL_TRIG_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_EL_TRIG_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                sample.AddHistoSys('ATLAS_EL_ZEE','%s_ATLAS_EL_ZEE_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_EL_ZEE_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                sample.AddHistoSys('ATLAS_JER_2012','%s_ATLAS_JER_2012_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_JER_2012_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                sample.AddHistoSys('ATLAS_JES_2012_Detector1','%s_ATLAS_JES_2012_Detector1_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_JES_2012_Detector1_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                sample.AddHistoSys('ATLAS_JES_2012_Eta_StatMethod','%s_ATLAS_JES_2012_Eta_StatMethod_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_JES_2012_Eta_StatMethod_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                sample.AddHistoSys('ATLAS_JES_2012_EtaModelling','%s_ATLAS_JES_2012_EtaModelling_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_JES_2012_EtaModelling_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                sample.AddHistoSys('ATLAS_JES_2012_Modelling1','%s_ATLAS_JES_2012_Modelling1_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_JES_2012_Modelling1_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                sample.AddHistoSys('ATLAS_JES_2012_PileRho_TAU','%s_ATLAS_JES_2012_PileRho_TAU_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_JES_2012_PileRho_TAU_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                sample.AddHistoSys('ATLAS_JES_2012_Statistical1','%s_ATLAS_JES_2012_Statistical1_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_JES_2012_Statistical1_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                sample.AddHistoSys('ATLAS_JES_FlavComp_TAU','%s_ATLAS_JES_FlavComp_TAU_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_JES_FlavComp_TAU_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                sample.AddHistoSys('ATLAS_JES_Flavb','%s_ATLAS_JES_Flavb_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_JES_Flavb_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                sample.AddHistoSys('ATLAS_JES_FlavResp','%s_ATLAS_JES_FlavResp_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_JES_FlavResp_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                sample.AddHistoSys('ATLAS_JES_Mu','%s_ATLAS_JES_Mu_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_JES_Mu_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                sample.AddHistoSys('ATLAS_JES_NPV','%s_ATLAS_JES_NPV_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_JES_NPV_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                sample.AddHistoSys('ATLAS_JVF_2012','%s_ATLAS_JVF_2012_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_JVF_2012_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                sample.AddHistoSys('ATLAS_MET_RESOSOFT','%s_ATLAS_MET_RESOSOFT_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_MET_RESOSOFT_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                sample.AddHistoSys('ATLAS_MET_SCALESOFT','%s_ATLAS_MET_SCALESOFT_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_MET_SCALESOFT_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                ###sample.AddHistoSys('ATLAS_MU_FF','%s_ATLAS_MU_FF_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_MU_FF_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                sample.AddHistoSys('ATLAS_MU_ID','%s_ATLAS_MU_ID_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_MU_ID_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                sample.AddHistoSys('ATLAS_MU_ISO','%s_ATLAS_MU_ISO_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_MU_ISO_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                sample.AddHistoSys('ATLAS_MU_MS','%s_ATLAS_MU_MS_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_MU_MS_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                sample.AddHistoSys('ATLAS_MU_TRIG','%s_ATLAS_MU_TRIG_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_MU_TRIG_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                ###sample.AddHistoSys('ATLAS_PU_RESCALE_2012','%s_ATLAS_PU_RESCALE_2012_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_PU_RESCALE_2012_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                sample.AddHistoSys('ATLAS_TAU_EFAKE_2012','%s_ATLAS_TAU_EFAKE_2012_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_TAU_EFAKE_2012_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                ###sample.AddHistoSys('ATLAS_TAU_FF','%s_ATLAS_TAU_FF_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_TAU_FF_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                sample.AddHistoSys('ATLAS_TAU_ID_2012','%s_ATLAS_TAU_ID_2012_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_TAU_ID_2012_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                sample.AddHistoSys('ATLAS_TAU_ID_STAT_2012','%s_ATLAS_TAU_ID_STAT_2012_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_TAU_ID_STAT_2012_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                sample.AddHistoSys('ATLAS_TES_TRUE_2012','%s_ATLAS_TES_TRUE_2012_DOWN_%s' % (region.name, supergroup_name), self.rootfile_name,'', '%s_ATLAS_TES_TRUE_2012_UP_%s' % (region.name, supergroup_name), self.rootfile_name,'')
                                
                                
                                
                        else:
                            if is_fakes(histogram_name):
                                sample = ROOT.RooStats.HistFactory.Sample(histogram_name, histogram_name, self.rootfile_name)
                                sample.ActivateStatError()
                                #if Systematics:
                                #sample.AddOverallSys('ATLAS_TAU_FF', 0.7, 1.3) 

                        channel.AddSample(sample)

                combination_measurement.AddChannel(channel)

            ## Now that the workspace is specified create it
            combination_measurement.CollectHistograms()
            combination_measurement.PrintTree()

            ## Dump xml file
            combination_measurement.PrintXML(self.name, '')

            ## Make the workspace
            ROOT.RooStats.HistFactory.MakeModelAndMeasurementFast(combination_measurement)

                        
                    
                        
                    
                
                  
                 
                 
                 

             
        
