#from Tools.Systematics.sys_classes import *
from sys_classes import *

## Special lists, True (weight), False (tree)
WHhh_mc_shape_systematics = [
    ('ATLAS_BTag_BEFF', True), 
    ('ATLAS_BTag_CEFF', True), 
    ('ATLAS_BTag_LEFF', True), 
    ('ATLAS_EL_SCALE_ZEE', False),
    ('ATLAS_EL_SCALE_R12', False),
    ('ATLAS_EL_SCALE_PS', False),  
    ('ATLAS_EL_SCALE_LOWPT', False),
    ('ATLAS_EL_RES', True),
    ('ATLAS_EL_EFF_ID', True),
    ('ATLAS_EL_EFF_ISO', True),
    ('ATLAS_EL_EFF_TRIG', True),
    ('ATLAS_JER_2012', False),
    ('ATLAS_JES_2012_Statistical1', False),
    ('ATLAS_JES_2012_Modelling1', False),
    ('ATLAS_JES_2012_Detector1', False), 
    ('ATLAS_JES_2012_EtaModelling', False), 
    ('ATLAS_JES_2012_Eta_StatMethod', False), 
    ('ATLAS_JES_2012_PileRho_TAU', False), 
    ('ATLAS_JES_NPV', False), 
    ('ATLAS_JES_Mu', False), 
    ('ATLAS_JES_FlavComp_TAU', False), 
    ('ATLAS_JES_FlavResp', False),
    ('ATLAS_JES_Flavb', False), 
    ('ATLAS_JVF_2012', False),  
    ('ATLAS_MET_RESOSOFT', False),
    ('ATLAS_MET_SCALESOFT', False),
    ('ATLAS_MU_MS', False), 
    ('ATLAS_MU_EFF_ID', True), 
    ('ATLAS_MU_EFF_ISO', True), 
    ('ATLAS_MU_EFF_TRIG', True),
    ('ATLAS_PU_RESCALE_2012', True), ### PROBLEM WITH NAN?
    ('ATLAS_TAU_EFAKE_2012', True),
    ('ATLAS_TAU_ID_2012', True), 
    ('ATLAS_TAU_ID_STAT_2012', True),
    ('ATLAS_TES_TRUE_2012', False),
]

ZHhh_mc_shape_systematics = [
    ('ATLAS_EL_ZEE', False),
    ('ATLAS_EL_R12', False),
    ('ATLAS_EL_PS', False),  
    ('ATLAS_EL_LOWPT', False),
    ('ATLAS_EL_RES', True),
    ('ATLAS_EL_EFF_ID', True),
    ('ATLAS_EL_EFF_ISO', True),
    ('ATLAS_EL_EFF_TRIG', True),
    ('ATLAS_JER_2012', False),
    ('ATLAS_JES_2012_Statistical1', False),
    ('ATLAS_JES_2012_Modelling1', False),
    ('ATLAS_JES_2012_Detector1', False), 
    ('ATLAS_JES_2012_EtaModelling', False), 
    ('ATLAS_JES_2012_Eta_StatMethod', False), 
    ('ATLAS_JES_2012_PileRho_TAU', False), 
    ('ATLAS_JES_NPV', False), 
    ('ATLAS_JES_Mu', False), 
    ('ATLAS_JES_FlavComp_TAU', False), 
    ('ATLAS_JES_FlavResp', False),
    ('ATLAS_JES_Flavb', False), 
    ('ATLAS_JVF_2012', False),  
    ('ATLAS_MET_RESOSOFT', False),
    ('ATLAS_MET_SCALESOFT', False),
    ('ATLAS_MU_MS', False), 
    ('ATLAS_MU_EFF_ID', True), 
    ('ATLAS_MU_EFF_ISO', True), 
    ('ATLAS_MU_EFF_TRIG', True),
    ('ATLAS_PU_RESCALE_2012', True), ### PROBLEM WITH NAN?
    ('ATLAS_TAU_EFAKE_2012', True),
    ('ATLAS_TAU_ID_2012', True), 
    ('ATLAS_TAU_ID_STAT_2012', True),
    ('ATLAS_TES_TRUE_2012', False),
]

#mass, br_tautau, QCDscale_ZH, pdf_Higgs_WH, pdf_Higgs_ZH
br_tautau = [
    (100, [1.069, 0.933], [1.024, 0.976], [1.023, 0.977], [1.023, 0.977] ),
    (105, [1.068, 0.933], [1.025, 0.975], [1.023, 0.977], [1.023, 0.977] ),
    (110, [1.066, 0.935], [1.027, 0.973], [1.024, 0.976], [1.024, 0.976] ),
    (115, [1.064, 0.937], [1.028, 0.972], [1.023, 0.977], [1.025, 0.975] ),
    (120, [1.061, 0.940], [1.030, 0.970], [1.025, 0.975], [1.025, 0.975] ),
    (125, [1.057, 0.943], [1.031, 0.969], [1.023, 0.977], [1.025, 0.975] ),
    (130, [1.053, 0.948], [1.033, 0.967], [1.024, 0.976], [1.024, 0.976] ),
    (135, [1.048, 0.952], [1.035, 0.965], [1.025, 0.975], [1.027, 0.973] ),
    (140, [1.036, 0.964], [1.036, 0.964], [1.024, 0.976], [1.027, 0.973] ),
    (145, [1.033, 0.967], [1.038, 0.962], [1.024, 0.976], [1.027, 0.973] ),
    (150, [1.030, 0.969], [1.039, 0.961], [1.026, 0.974], [1.027, 0.973] ),
]


## Instantiate limit channels
wh_SR  = LimitChannel('wh', 'SR')

zh_SR  = LimitChannel('zh', 'SR')


LimitChannels = [
    wh_SR,
    zh_SR,
]

##########################################################################
## Add signal samples
for lc in LimitChannels:

    if lc.category == 'wh':
        mc_shape_systematics = WHhh_mc_shape_systematics
    else:
        mc_shape_systematics = ZHhh_mc_shape_systematics
    
    if not 'SR' == lc.control_region: continue
    
    for mass in br_tautau:
        #VBFH = Sample('VBFH%d' % mass[0])
        #ggH  = Sample('ggH%d' % mass[0])
        WH   = Sample('WH%d' % mass[0])
        ZH   = Sample('ZH%d' % mass[0])

        for shape in mc_shape_systematics:
            #VBFH.add_shape(shape[0], shape[1])
            #ggH.add_shape(shape[0], shape[1])
            WH.add_shape(shape[0], shape[1])
            ZH.add_shape(shape[0], shape[1])
        
        ## Decorrelated shapes
        #VBFH.add_shape('ATLAS_JES_2012_PileRho_TAU_QQ')
        #ggH.add_shape('ATLAS_JES_2012_PileRho_TAU_GG')
        #WH.add_shape('ATLAS_JES_2012_PileRho_TAU_QQ')
        #ZH.add_shape('ATLAS_JES_2012_PileRho_TAU_QQ')

        #VBFH.add_shape('ATLAS_JES_FlavComp_TAU_Q')
        #ggH.add_shape('ATLAS_JES_FlavComp_TAU_G')
        #WH.add_shape('ATLAS_JES_FlavComp_TAU_Q')
        #ZH.add_shape('ATLAS_JES_FlavComp_TAU_Q')

        #VBFH.add_shape('ATLAS_TRIGGER_LH_2012', True)
        #ggH.add_shape('ATLAS_TRIGGER_LH_2012', True)
        #WH.add_shape('ATLAS_TRIGGER_LH_2012', True)
        #ZH.add_shape('ATLAS_TRIGGER_LH_2012', True)

        #VBFH.add_shape('ATLAS_TES_TRUE_2012')
        #ggH.add_shape('ATLAS_TES_TRUE_2012')
        #WH.add_shape('ATLAS_TES_TRUE_2012')
        #ZH.add_shape('ATLAS_TES_TRUE_2012')
        
        ## Branching fraction uncertainty
        #VBFH.add_overall('ATLAS_BR_tautau', mass[2], mass[1])
        #ggH.add_overall('ATLAS_BR_tautau', mass[2], mass[1])
        WH.add_overall('ATLAS_BR_tautau', mass[1][1], mass[1][0])
        ZH.add_overall('ATLAS_BR_tautau', mass[1][1], mass[1][0])

        ## Lumi uncertainty
        #VBFH.add_overall('ATLAS_LUMI_2012', 0.972, 1.028)
        #ggH.add_overall('ATLAS_LUMI_2012', 0.972, 1.028)
        WH.add_overall('ATLAS_LUMI_2012', 0.972, 1.028)
        ZH.add_overall('ATLAS_LUMI_2012', 0.972, 1.028)

    
        ## WH category
        if lc.category == 'wh':
            #VBFH.add_overall('QCDscale_qqH', 0.979, 1.021)
            #VBFH.add_overall('pdf_Higgs_qq', 0.97, 1.03)

            #ggH.add_shape('QCDscale_ggH3in')
            #ggH.add_overall('ATLAS_UE_gg', 0.70, 1.30)
            #ggH.add_overall('Gen_Qmass_ggH', 0.82, 1.18)
            #ggH.add_overall('QCDscale_ggH2in', 0.80, 1.25)
            #ggH.add_overall('pdf_Higgs_gg', 0.93, 1.08)

            WH.add_overall('QCDscale_WH', 0.99, 1.01)
            WH.add_overall('ATLAS_UE_VH', 0.99, 1.01)
            WH.add_overall('pdf_Higgs_WH', mass[3][1], mass[3][0])
            #!!!!!!!!!!!!!!!!!!!!!!!!!!! NEED TO ADD IN WH.add_shape('ATLAS_EWK', True)
            
            ZH.add_overall('QCDscale_ZH', mass[2][1], mass[2][0])
            ZH.add_overall('ATLAS_UE_VH', 0.979, 1.021)
            ZH.add_overall('pdf_Higgs_ZH', mass[4][1], mass[4][0])
            #!!!!!!!!!!!!!!!!!!!!  NEED TO ADD IN  ZH.add_shape('ATLAS_EWK', True)
    
            #wh_SR.add(VBFH)
            #wh_SR.add(ggH)
            wh_SR.add(WH)
            wh_SR.add(ZH)


        ## ZH category
        if lc.category == 'zh':
            #VBFH.add_overall('QCDscale_qqH', 0.986, 1.014)
            #VBFH.add_overall('pdf_Higgs_qq', 0.97, 1.03)

            #ggH.add_overall('Gen_Qmass_ggH', 0.71, 1.29)
            #ggH.add_overall('QCDscale_ggH1in', 0.78, 1.29)
            #ggH.add_overall('QCDscale_ggH2in', 1.05, 0.95)
            #ggH.add_overall('pdf_Higgs_gg', 0.93, 1.08)

            #WH.add_overall('QCDscale_WH', 0.960, 1.041)
            #WH.add_overall('pdf_Higgs_qq', 0.97, 1.03)

            ZH.add_overall('QCDscale_ZH', mass[2][1], mass[2][0])
            ZH.add_overall('ATLAS_UE_VH', 0.979, 1.021)
            ZH.add_overall('pdf_Higgs_ZH', mass[4][1], mass[4][0])
            #!!!!!!!!!!!!!!!! NEEED TO ADD  ZH.add_shape('ATLAS_EWK', True)
            
            #boosted_SR.add(VBFH)
            #boosted_SR.add(ggH)
            #boosted_SR.add(WH)
            zh_SR.add(ZH)


    

##########################################################################
## Add background samples

## Ztautau (true tau)
#for lc in LimitChannels:
#    if lc.category == 'wh':
#        mc_shape_systematics = WHhh_mc_shape_systematics
#    else:
#        mc_shape_systematics = ZHhh_mc_shape_systematics
#
#    ztt = Sample('Ztautau_zerofakes')
#    
#    for shape in mc_shape_systematics:
#        ztt.add_shape(shape[0], shape[1])
#
#    ## Lumi uncertainty
#    ztt.add_overall('ATLAS_LUMI_2012', 0.972, 1.028)
#
#    lc.add(ztt)


## ttbar (true tau)
#for lc in LimitChannels:
#    if lc.category == 'wh':
#        mc_shape_systematics = WHhh_mc_shape_systematics
#    else:
#        mc_shape_systematics = ZHhh_mc_shape_systematics
#
#    top = Sample('tt_zerofakes')
#
#    #if lc.category == 'zeroj' and lc.control_region == 'SS': continue
#
#    for shape in mc_shape_systematics:
#        top.add_shape(shape[0], shape[1])
#
#    ## Lumi uncertainty
#    top.add_overall('ATLAS_LUMI_2012', 0.972, 1.028)
#
#    lc.add(top)


## WZ (true tau)
for lc in LimitChannels:
    if lc.category == 'wh':
        mc_shape_systematics = WHhh_mc_shape_systematics
    else:
        mc_shape_systematics = ZHhh_mc_shape_systematics

    if lc.category == 'zh':
        WZ = Sample('WZ_zerofakes')

        for shape in mc_shape_systematics:
            WZ.add_shape(shape[0], shape[1])
    
            ## Theory uncertainties
            #VV.add_overall('QCDscale_VV', 0.95, 1.05)
            #VV.add_overall('pdf_qq', 0.96, 1.04)
    
            ## Lumi uncertainty
        WZ.add_overall('ATLAS_LUMI_2012', 0.972, 1.028)
    
        lc.add(WZ)
    if lc.category == 'wh':
        WZ = Sample('WHhh_WZ_zerofakes')

        for shape in mc_shape_systematics:
            WZ.add_shape(shape[0], shape[1])
    
            ## Theory uncertainties
            #VV.add_overall('QCDscale_VV', 0.95, 1.05)
            #VV.add_overall('pdf_qq', 0.96, 1.04)
    
            ## Lumi uncertainty
        WZ.add_overall('ATLAS_LUMI_2012', 0.972, 1.028)
    
        lc.add(WZ)


## ZZ (true tau)
for lc in LimitChannels:
    if lc.category == 'wh':
        mc_shape_systematics = WHhh_mc_shape_systematics
    else:
        mc_shape_systematics = ZHhh_mc_shape_systematics

    if lc.category == 'zh':
        ZZ = Sample('ZZ_zerofakes')

        for shape in mc_shape_systematics:
            ZZ.add_shape(shape[0], shape[1])

        ## Theory uncertainties
        #VV.add_overall('QCDscale_VV', 0.95, 1.05)
        #VV.add_overall('pdf_qq', 0.96, 1.04)

        ## Lumi uncertainty
        ZZ.add_overall('ATLAS_LUMI_2012', 0.972, 1.028)

        lc.add(ZZ)
    if lc.category == 'wh':
        ZZ = Sample('WHhh_ZZ_zerofakes')

        for shape in mc_shape_systematics:
            ZZ.add_shape(shape[0], shape[1])

        ## Theory uncertainties
        #VV.add_overall('QCDscale_VV', 0.95, 1.05)
        #VV.add_overall('pdf_qq', 0.96, 1.04)

        ## Lumi uncertainty
        ZZ.add_overall('ATLAS_LUMI_2012', 0.972, 1.028)

        lc.add(ZZ)


## Triboson (true tau)
for lc in LimitChannels:
    if lc.category == 'wh':
        mc_shape_systematics = WHhh_mc_shape_systematics
    else:
        mc_shape_systematics = ZHhh_mc_shape_systematics

    trib = Sample('Triboson_zerofakes')

    for shape in mc_shape_systematics:
        trib.add_shape(shape[0], shape[1])

    ## Lumi uncertainty
    trib.add_overall('ATLAS_LUMI_2012', 0.972, 1.028)

    lc.add(trib)


## Fake factor
for lc in LimitChannels:

    if lc.category == 'zh':
        ff = Sample('AntitauEvents')
        ff.add_shape('ATLAS_TAU_FF', True)

        lc.add(ff)
    if lc.category == 'wh':
        ff = Sample('WHhh_AntitauEvents')
        ff.add_shape('ATLAS_TAU_FF', True)

        lc.add(ff)


##########################################################################
## Construct the Sys_set

ss = SysSet('EmmaSys')
for lc in LimitChannels:
    ss.add(lc)

ss.print_all()

## Save the sys-set
import pickle

#f = open('Tools/Systematics/%s.sys' % ss.name, 'wb')
f = open('%s.sys' % ss.name, 'wb')
pickle.dump(ss, f)
f.close()
