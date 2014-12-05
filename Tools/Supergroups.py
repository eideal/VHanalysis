from Supergroup import Supergroup
from Subsets import *
from Groups import *
import palette

Data = Supergroup('Data',
                  [Data_group],
                  factor = 1.0,
                  color = palette.black,
                  style = 'points',
                  legendLabel = 'Data',
                  stack = False,
                  subset = isreal
                  )
AntitauEvents = Supergroup('AntitauEvents',
                           [Data_group_AntiTau,
							              MCcorr_fakes_group,
                            MCcorr_fakesttbar_group], 
                            #],
                           #this last group is to ensure I have all 3 ttbar samples in the MCcorr and am filtering out the dilepton from the lep_fil sample
                            factor = 1.0,
                            color = palette.green,
                            style = 'fill',
                            legendLabel = 'Fakes',
                            stack = True,
                            )
WHhh_AntitauEvents = Supergroup('WHhh_AntitauEvents',
                           [Data_group_AntiTau,
                            MCcorr_fakes_group_WHhh,
                            MCcorr_fakesttbar_group], 
                            #],
                           #this last group is to ensure I have all 3 ttbar samples in the MCcorr and am filtering out the dilepton from the lep_fil sample
                            factor = 1.0,
                            color = palette.green,
                            style = 'fill',
                            legendLabel = 'Fakes',
                            stack = True,
                            )

tt_zerofakes = Supergroup('tt_zerofakes',
                          [ttbar_lepfil_group,
                           ttbar_allhad_group,
                           ttbar_dilepton_group],
                           factor = 1.0,
                           color = palette.pink,
                           style = 'fill',
                           legendLabel = 'tt',
                           stack = True,
                           subset = isreal + truetaus
                           )
ZZ_zerofakes = Supergroup('ZZ_zerofakes',
                          [ZZ_group],
                          factor = 1.0,
                          color = palette.orange,
                          style = 'fill',
                          legendLabel = 'ZZ',
                          stack = True,
                          subset = isreal + truetaus
                          )
WHhh_ZZ_zerofakes = Supergroup('WHhh_ZZ_zerofakes',
                          [WHhh_ZZ_group],
                          factor = 1.0,
                          color = palette.orange,
                          style = 'fill',
                          legendLabel = 'ZZ',
                          stack = True,
                          subset = isreal + truetaus
                          )
WZ_zerofakes = Supergroup('WZ_zerofakes',
                          [WZ_group],
                          factor = 1.0,
                          color = palette.teal,
                          style = 'fill',
                          legendLabel = 'WZ',
                          stack = True,
                          subset = isreal + truetaus
                          )
WHhh_WZ_zerofakes = Supergroup('WHhh_WZ_zerofakes',
                          [WHhh_WZ_group],
                          factor = 1.0,
                          color = palette.teal,
                          style = 'fill',
                          legendLabel = 'WZ',
                          stack = True,
                          subset = isreal + truetaus
                          )
Triboson_zerofakes = Supergroup('Triboson_zerofakes',
                                [Triboson_group],
                                factor = 1.0,
                                color = palette.red,
                                style = 'fill',
                                legendLabel = 'Triboson',
                                stack = True,
                                subset = isreal + truetaus
                                )
WW_zerofakes = Supergroup('WW_zerofakes',
                          [WW_group],
                          factor = 1.0,
                          color = palette.indigo,
                          style = 'fill',
                          legendLabel = 'WW',
                          stack = True,
                          subset = isreal + truetaus
                          )
WHhh_WW_zerofakes = Supergroup('WHhh_WW_zerofakes',
                                [WHhh_WW_group],
                                factor = 1.0,
                                color = palette.indigo, 
                                style = 'fill',
                                legendLabel = 'WW',
                                stack = True,
                                subset = isreal + truetaus
                                )
WGamma_zerofakes = Supergroup('WGamma_zerofakes',
                              [WGamma_group],
                              factor = 1.0,
                              color = palette.grey,
                              style = 'fill',
                              legendLabel = 'WGamma',
                              stack = True,
                              subset = isreal + truetaus
                              )

SingleTop_zerofakes = Supergroup('SingleTop_zerofakes',
                       [SingleTop_group],
                       factor = 1.0,
                       color = palette.darkpink,
                       style = 'fill',
                       legendLabel = 'SingleTop',
                       stack = True,
                       subset = isreal + truetaus
                       )
Ztautau_zerofakes = Supergroup('Ztautau_zerofakes',
                               [ZttJets_group],
                               factor = 1.0,
                               color = palette.purple,
                               style = 'fill',
                               legendLabel = 'ZttJets',
                               stack = True,
                               subset = isreal + truetaus
                               )

MC_ZHhh = Supergroup('MC_ZHhh',
                      [ttbar_lepfil_group,
                      ttbar_allhad_group,
                      ttbar_dilepton_group,
                      ZttJets_group,
                      ZZ_group,
                      WZ_group,
                      Triboson_group],
                      factor = 1.0,
                      color = palette.red,
                      style = 'fill',
                      legendLabel = 'All_MC',
                      stack = True,
                      subset = isreal + truetaus
                    )

MC_WHhh = Supergroup('MC_WHhh',
                    [ttbar_lepfil_group,
                    ttbar_allhad_group,
                    ttbar_dilepton_group,
                    ZttJets_group,
                    WHhh_ZZ_group,
                    WHhh_WZ_group,
                    Triboson_group],
                    factor = 1.0,
                    color = palette.red,
                    style = 'fill',
                    legendLabel = 'All_MC',
                    stack = True,
                    subset = isreal + truetaus
                    )

#################
WJets_zerofakes = Supergroup('WJets_zerofakes',
				   [WJets_group],
				   factor = 1.0,
				   color = palette.teal,
				   style = 'fill',
				   legendLabel = 'WJets',
				   stack = True,
				   subset = isreal + truetaus
				   )
WeJets_zerofakes = Supergroup('WeJets_zerofakes',
				   [WeJets_group],
				   factor = 1.0,
				   color = palette.blue,
				   style = 'fill',
				   legendLabel = 'WeJets',
				   stack = True,
				   subset = isreal + truetaus
				   )
WmJets_zerofakes = Supergroup('WmJets_zerofakes',
				   [WmJets_group],
				   factor = 1.0,
				   color = palette.skyblue,
				   style = 'fill',
				   legendLabel = 'WmJets',
				   stack = True,
				   subset = isreal + truetaus
				   )
WtJets_zerofakes = Supergroup('WtJets_zerofakes',
				   [WtJets_group],
				   factor = 1.0,
				   color = palette.beige,
				   style = 'fill',
				   legendLabel = 'WtJets',
				   stack = True,
				   subset = isreal + truetaus
				   )

ZeeJets_zerofakes = Supergroup('ZeeJets',
					 [ZeeJets_group],
					 factor = 1.0,
					 color = palette.bandyellow,
					 style = 'fill',
					 legendLabel = 'ZeeJets',
					 stack = True,
					 subset = isreal + truetaus
                     )
ZmmJets_zerofakes = Supergroup('ZmmJets',
					           [ZmmJets_group],
                     factor = 1.0, ###k-factor
#                     factor = 0.8,
					 color = palette.bandgreen,
					 style = 'fill',
					 legendLabel = 'ZmmJets',
					 stack = True,
					 subset = isreal + truetaus
                     )

##### SIGNAL ########### SIGNAL ############# SIGNAL ######

######## Supergroups made to do the UE reweighting between CN and D3PD
WH_inclusive = Supergroup('WH_inclusive',
                          [WH125_group,
                          WH125lh_group,
                          WH125ll_group],
                          factor = 1.0,
                          color = palette.blue,
                          style = 'line',
                          legendLabel = 'WH125_CN',
                          stack = True,
                          subset = isreal)

ZH_inclusive = Supergroup('ZH_inclusive',
                          [ZH125_group,
                          ZH125lh_group,
                          ZH125ll_group],
                          factor = 1.0,
                          color = palette.blue,
                          style = 'line',
                          legendLabel = 'ZH125_CN',
                          stack = True,
                          subset = isreal)

########


WH100 = Supergroup('WH100',
                   [WH100_group],
                   factor = 1.0,
                   color = palette.black,
                   style = 'line',
                   legendLabel = 'WH100',
                   stack = False,
                   subset = isreal
                   )
WH105 = Supergroup('WH105',
                   [WH105_group],
                   factor = 1.0,
                   color = palette.black,
                   style = 'line',
                   legendLabel = 'WH105',
                   stack = False,
                   subset = isreal
                   )
WH110 = Supergroup('WH110',
                   [WH110_group],
                   factor = 1.0,
                   color = palette.black,
                   style = 'line',
                   legendLabel = 'WH110',
                   stack = False,
                   subset = isreal
                   )
WH115 = Supergroup('WH115',
                   [WH115_group],
                   factor = 1.0,
                   color = palette.black,
                   style = 'line',
                   legendLabel = 'WH115',
                   stack = False,
                   subset = isreal
                   )
WH120 = Supergroup('WH120',
                   [WH120_group],
                   factor = 1.0,
                   color = palette.black,
                   style = 'line',
                   legendLabel = 'WH120',
                   stack = False,
                   subset = isreal
                   )
WH125 = Supergroup('WH125',
                   [WH125_group],
                   factor = 1.0,
                   color = palette.black,
                   style = 'line',
                   legendLabel = 'WH125',
                   stack = False,
                   subset = isreal
                   )
WH130 = Supergroup('WH130',
                   [WH130_group],
                   factor = 1.0,
                   color = palette.black,
                   style = 'line',
                   legendLabel = 'WH130',
                   stack = False,
                   subset = isreal
                   )
WH135 = Supergroup('WH135',
                   [WH135_group],
                   factor = 1.0,
                   color = palette.black,
                   style = 'line',
                   legendLabel = 'WH135',
                   stack = False,
                   subset = isreal
                   )
WH140 = Supergroup('WH140',
                   [WH140_group],
                   factor = 1.0,
                   color = palette.black,
                   style = 'line',
                   legendLabel = 'WH140',
                   stack = False,
                   subset = isreal
                   )
WH145 = Supergroup('WH145',
                   [WH145_group],
                   factor = 1.0,
                   color = palette.black,
                   style = 'line',
                   legendLabel = 'WH145',
                   stack = False,
                   subset = isreal
                   )
WH150 = Supergroup('WH150',
                   [WH150_group],
                   factor = 1.0,
                   color = palette.black,
                   style = 'line',
                   legendLabel = 'WH150',
                   stack = False,
                   subset = isreal
                   )
###
ZH100 = Supergroup('ZH100',
                   [ZH100_group],
                   factor = 1.0,
                   color = palette.black,
                   style = 'line',
                   legendLabel = 'ZH100',
                   stack = False,
                   subset = isreal
                   )
ZH105 = Supergroup('ZH105',
                   [ZH105_group],
                   factor = 1.0,
                   color = palette.black,
                   style = 'line',
                   legendLabel = 'ZH105',
                   stack = False,
                   subset = isreal
                   )
ZH110 = Supergroup('ZH110',
                   [ZH110_group],
                   factor = 1.0,
                   color = palette.black,
                   style = 'line',
                   legendLabel = 'ZH110',
                   stack = False,
                   subset = isreal
                   )
ZH115 = Supergroup('ZH115',
                   [ZH115_group],
                   factor = 1.0,
                   color = palette.black,
                   style = 'line',
                   legendLabel = 'ZH115',
                   stack = False,
                   subset = isreal
                   )
ZH120 = Supergroup('ZH120',
                   [ZH120_group],
                   factor = 1.0,
                   color = palette.black,
                   style = 'line',
                   legendLabel = 'ZH120',
                   stack = False,
                   subset = isreal
                   )
ZH125 = Supergroup('ZH125',
                   [ZH125_group],
                   factor = 100.0,
                   color = palette.black,
                   style = 'line',
                   legendLabel = 'ZH125*100',
                   stack = False,
                   subset = isreal
                   )

##Some supergroups made to study pT Higgs dependence after making selection cuts
ZH125_cat = Supergroup('ZH125_cat',
                       [ZH125_group],
                       factor = 0.4, #1.0
                       color = palette.blue,
                       style = 'line',
                       legendLabel = 'ZH125_cat *0.4',
                       stack = True,
                       subset = isreal + ZHcat
)
ZH125_trig = Supergroup('ZH125_trig',
                        [ZH125_group],
                        factor = 2.0,#1.0
                        color = palette.purple,
                        style = 'line',
                        legendLabel = 'ZH125_trig(x2)',
                        stack = False,
                        subset = isreal + ZHtrig
                        )
ZH125_flav = Supergroup('ZH125_flav',
                        [ZH125_group],
                        factor = 10.9,#1.0
                        color = palette.orange,
                        style = 'line',
                        legendLabel = 'ZH125_flav *10.9',
                        stack = True,
                        subset = isreal + ZHflav
                        )
ZH125_charge = Supergroup('ZH125_charge',
                          [ZH125_group],
                          factor = 2.0,#1.0
                          color = palette.pink,
                          style = 'line',
                          legendLabel = 'ZH125_charge (x2)',
                          stack = False,
                          subset = isreal + ZHcharge
                          ) 
ZH125_all = Supergroup('ZH125_all',
                       [ZH125_group],
                       factor = 1.0,#1.0
                       color = palette.green,
                       style = 'line',
                       legendLabel = 'ZH125_all',
                       stack = False,
                       subset = isreal + ZHall
                       )
ZH125_lh = Supergroup('ZH125_lh',
                      [ZH125lh_group],
                      factor = 1.0,
                      color = palette.black,
                      style = 'line',
                      legendLabel = 'ZH125lh',
                      stack = True,
                      subset = isreal
                      )
                
ZH125_lh_cat = Supergroup('ZH125_lh_cat',
                          [ZH125lh_group],
                          factor = 1.0, #1.0
                          color = palette.blue,
                          style = 'line',
                          legendLabel = 'ZH125lh_cat',
                          stack = False,
                          subset = isreal + ZHcat
                          )
ZH125_lh_all = Supergroup('ZH125_lh_all',
                          [ZH125lh_group],
                          factor = 1.0, #1.0
                          color = palette.green,
                          style = 'line',
                          legendLabel = 'ZH125lh_allcuts',
                          stack = False,
                          subset = isreal + ZHall
                          )
WH125_lh = Supergroup('WH125_lh',
                      [WH125lh_group],
                      factor = 100.0,
                      color = palette.black,
                      style = 'line',
                      legendLabel = 'WH125lh(*100)',
                      stack = False,
                      subset = isreal
                      )
WH125_lh_cat = Supergroup('WH125_lh_cat',
                         [WH125lh_group],
                         factor = 0.17,#1.0
                         color = palette.blue,
                         style = 'line',
                         legendLabel = 'WH125lh_cat *0.17',
                         stack = True,
                         subset = isreal + WHcat
                         ) 
WH125_lh_presel = Supergroup('WH125_lh_presel',
                             [WH125lh_group],
                             factor = 1.0,#1.0
                             color = palette.bandyellow,
                             style = 'line',
                             legendLabel = 'WH125lh_presel',
                             stack = False,
                             subset = isreal + WHpresel
                             ) 

WH125_lh_zmass = Supergroup('WH125_lh_zmass',
                            [WH125lh_group],
                            factor = 1.0,#1.0
                            color = palette.orange,
                            style = 'line',
                            legendLabel = 'WH125lh_zmass',
                            stack = False,
                            subset = isreal + WHzmassveto
                            ) 
WH125_lh_all = Supergroup('WH125_lh_all',
                          [WH125lh_group],
                          factor = 1.0,
                          color = palette.green,
                          style = 'line',
                          legendLabel = 'WH125lh_allcuts',
                          stack = False,
                          subset = isreal + WHall
                          ) 

############# END of supergroups made to study Higgs pT in VH channels, ref. July 23 2014

### Studies of EWK reweighting ###
ZH125hh_WithEWK = Supergroup('ZH125hh_WithEWK',
                             [ZHhh_WithEWK],
                             factor = 1.0,
                             color = palette.blue,
                             style = 'line',
                             legendLabel = 'ZH125hh_EWK',
                             stack = True,
                             subset = isreal
                             )
ZH125hh_NoEWK = Supergroup('ZH125hh_NoEWK',
                           [ZHhh_NoEWK],
                           factor = 1.0,
                           color = palette.black,
                           style = 'line',
                           legendLabel = 'ZH125hh_NoEWK',
                           stack = False,
                           subset = isreal
                           )


######################
ZH130 = Supergroup('ZH130',
                   [ZH130_group],
                   factor = 1.0,
                   color = palette.black,
                   style = 'line',
                   legendLabel = 'ZH130',
                   stack = False,
                   subset = isreal
                   )
ZH135 = Supergroup('ZH135',
                   [ZH135_group],
                   factor = 1.0,
                   color = palette.black,
                   style = 'line',
                   legendLabel = 'ZH135',
                   stack = False,
                   subset = isreal
                   )
ZH140 = Supergroup('ZH140',
                   [ZH140_group],
                   factor = 1.0,
                   color = palette.black,
                   style = 'line',
                   legendLabel = 'ZH140',
                   stack = False,
                   subset = isreal
                   )
ZH145 = Supergroup('ZH145',
                   [ZH145_group],
                   factor = 1.0,
                   color = palette.black,
                   style = 'line',
                   legendLabel = 'ZH145',
                   stack = False,
                   subset = isreal
                   )
ZH150 = Supergroup('ZH150',
                   [ZH150_group],
                   factor = 1.0,
                   color = palette.black,
                   style = 'line',
                   legendLabel = 'ZH150',
                   stack = False,
                   subset = isreal
                   )
####
VBFH100 = Supergroup('VBFH100',
                     [VBFH100_group],
                     factor = 1.0,
                     color = palette.black,
                     style = 'line',
                     legendLabel = 'VBFH100',
                     stack = False,
                     subset = isreal
                     )
VBFH105 = Supergroup('VBFH105',
                     [VBFH105_group],
                     factor = 1.0,
                     color = palette.black,
                     style = 'line',
                     legendLabel = 'VBFH105',
                     stack = False,
                     subset = isreal
                     )
VBFH110 = Supergroup('VBFH110',
                     [VBFH110_group],
                     factor = 1.0,
                     color = palette.black,
                     style = 'line',
                     legendLabel = 'VBFH110',
                     stack = False,
                     subset = isreal
                     )
VBFH115 = Supergroup('VBFH115',
                     [VBFH115_group],
                     factor = 1.0,
                     color = palette.black,
                     style = 'line',
                     legendLabel = 'VBFH115',
                     stack = False,
                     subset = isreal
                     )
VBFH120 = Supergroup('VBFH120',
                     [VBFH120_group],
                     factor = 1.0,
                     color = palette.black,
                     style = 'line',
                     legendLabel = 'VBFH120',
                     stack = False,
                     subset = isreal
                     )
VBFH125 = Supergroup('VBFH125',
                     [VBFH125_group],
                     factor = 1.0,
                     color = palette.black,
                     style = 'line',
                     legendLabel = 'VBFH125',
                     stack = False,
                     subset = isreal
                     )
VBFH130 = Supergroup('VBFH130',
                     [VBFH130_group],
                     factor = 1.0,
                     color = palette.black,
                     style = 'line',
                     legendLabel = 'VBFH130',
                     stack = False,
                     subset = isreal
                     )
VBFH135 = Supergroup('VBFH135',
                     [VBFH135_group],
                     factor = 1.0,
                     color = palette.black,
                     style = 'line',
                     legendLabel = 'VBFH135',
                     stack = False,
                     subset = isreal
                     )
VBFH140 = Supergroup('VBFH140',
                     [VBFH140_group],
                     factor = 1.0,
                     color = palette.black,
                     style = 'line',
                     legendLabel = 'VBFH140',
                     stack = False,
                     subset = isreal
                     )
VBFH145 = Supergroup('VBFH145',
                     [VBFH145_group],
                     factor = 1.0,
                     color = palette.black,
                     style = 'line',
                     legendLabel = 'VBFH145',
                     stack = False,
                     subset = isreal
                     )
VBFH150 = Supergroup('VBFH150',
                     [VBFH150_group],
                     factor = 1.0,
                     color = palette.black,
                     style = 'line',
                     legendLabel = 'VBFH150',
                     stack = False,
                     subset = isreal
                     )
#####
ggH100 = Supergroup('ggH100',
                    [ggH100_group],
                    factor = 1.0,
                    color = palette.black,
                    style = 'line',
                    legendLabel = 'ggH100',
                    stack = False,
                    subset = isreal
                    )
ggH105 = Supergroup('ggH105',
                    [ggH105_group],
                    factor = 1.0,
                    color = palette.black,
                    style = 'line',
                    legendLabel = 'ggH105',
                    stack = False,
                    subset = isreal
                    )
ggH110 = Supergroup('ggH110',
                    [ggH110_group],
                    factor = 1.0,
                    color = palette.black,
                    style = 'line',
                    legendLabel = 'ggH110',
                    stack = False,
                    subset = isreal
                    )
ggH115 = Supergroup('ggH115',
                    [ggH115_group],
                    factor = 1.0,
                    color = palette.black,
                    style = 'line',
                    legendLabel = 'ggH115',
                    stack = False,
                    subset = isreal
                    )
ggH120 = Supergroup('ggH120',
                    [ggH120_group],
                    factor = 1.0,
                    color = palette.black,
                    style = 'line',
                    legendLabel = 'ggH120',
                    stack = False,
                    subset = isreal
                    )
ggH125 = Supergroup('ggH125',
                    [ggH125_group],
                    factor = 1.0,
                    color = palette.black,
                    style = 'line',
                    legendLabel = 'ggH125',
                    stack = False,
                    subset = isreal
                    )
ggH130 = Supergroup('ggH130',
                    [ggH130_group],
                    factor = 1.0,
                    color = palette.black,
                    style = 'line',
                    legendLabel = 'ggH130',
                    stack = False,
                    subset = isreal
                    )
ggH135 = Supergroup('ggH135',
                    [ggH135_group],
                    factor = 1.0,
                    color = palette.black,
                    style = 'line',
                    legendLabel = 'ggH135',
                    stack = False,
                    subset = isreal
                    )
ggH140 = Supergroup('ggH140',
                    [ggH140_group],
                    factor = 1.0,
                    color = palette.black,
                    style = 'line',
                    legendLabel = 'ggH140',
                    stack = False,
                    subset = isreal
                    )
ggH145 = Supergroup('ggH145',
                    [ggH145_group],
                    factor = 1.0,
                    color = palette.black,
                    style = 'line',
                    legendLabel = 'ggH145',
                    stack = False,
                    subset = isreal
                    )
ggH150 = Supergroup('ggH150',
                    [ggH150_group],
                    factor = 1.0,
                    color = palette.black,
                    style = 'line',
                    legendLabel = 'ggH150',
                    stack = False,
                    subset = isreal
                    )



#### EXTRAS EXTRAS EXTRAS EXTRAS EXTRAS EXTRAS EXTRAS
######################################################
QCD = Supergroup('QCD', #### FOR WH
                  [DataSSS_group,
                   SSSWeJets_group,
                   SSSWmJets_group,
                   SSSWtJets_group,
                   SSSZeeJets_group,
                   SSSZmmJets_group,
                   SSSZttJets_group,
                   SSStt_group,
                   SSSSingleTop_group,
                   SSSZZ_group,
                   SSSWW_group,
                   SSSWGamma_group,
                   SSSWZ_group,
                   ],
                   factor = 2.0, #from rQCD measurement
                   color = palette.blue,
                   style = 'fill',
                   legendLabel = 'QCD',
                   stack = True,
                   subset = SSS + isreal
                   )
AllMC_RQCD = Supergroup('AllMC_RQCD',
                    [WeJets_group,
                     WmJets_group,
                     WtJets_group,
                     ZeeJets_group,
                     ZmmJets_group,
                     ZttJets_group,
                     tt_group,
                     SingleTop_group,
                     ZZ_group,
                     WW_group,
                     WGamma_group,
                     WZ_group,
                     ],
                    factor = -1.0,
                    color = palette.yellow,
                    style = 'fill',
                    legendLabel = 'AllMC_RQCD',
                    stack = True,
 #subset = ''
                    )
Data_RQCD = Supergroup('Data_RQCD',
                        [Data_group],
                        factor = 1.0,
                        color = palette.black,
                        style = 'line',
                        legendLabel = 'Data_RQCD',
                        stack = False,
 #                      subset = ''
                        )

		
# WeJets = Supergroup('WeJets',
#                     [WeJets_group],
#                     factor = 1.0,
#                     color = palette.green,
#                     style = 'fill',
#                     legendLabel = 'WenuJets',
#                     stack = True,
#                     subset = istau #+ SS
# )
# WmJets = Supergroup('WmJets',
#                     [WmJets_group],
#                     factor = 1.0,
#                     color = palette.brown,
#                     style = 'fill',
#                     legendLabel = 'WmunuJets',
#                     stack = True,
#                     subset = istau #+ SS
#                     )
# WmJets_zerofakes = Supergroup('WmJets_zerofakes',
#                              [WmJets_group],
#                              factor = 1.0,
#                              color = palette.brown,
#                              style = 'fill',
#                              legendLabel = 'WmJets(true)',
#                              stack = True,
#                              subset = truetaus + istau
#                              )
# WmJets_onefake = Supergroup('WmJets_onefake',
#                              [WmJets_group],
#                              factor = 1.0,
#                              color = palette.brown,
#                              style = 'fill',
#                              legendLabel = 'WmJets(1 fake)',
#                              stack = True,
#                              subset = istau + (onefaketau * onefaketau2)
#                              )
# WmJets_twofakes = Supergroup('WmJets_twofakes',
#                              [WmJets_group],
#                              factor = 1.0,
#                              color = palette.brown,
#                              style = 'fill',
#                              legendLabel = 'WmJets(2 fakes)',
#                              stack = True,
#                              subset = istau + twofaketau
#                              )                                                       
# WtJets = Supergroup('WtJets',
#                     [WtJets_group],
#                     factor = 1.0,
#                     color = palette.peach,
#                     style = 'fill',
#                     legendLabel = 'WtaunuJets',
#                     stack = True,
#                     subset = istau# + SS
#                     )

# ZmmJets_zerofakes = Supergroup('ZmmJets_zerofakes',
#                      [ZmmJets_group],
#                      factor = 1.0,
#                      color = palette.bandgreen,
#                      style = 'fill',
#                      legendLabel = 'Zmm(true)',
#                      stack = True,
#                      subset = truetaus + istau #+ SS
#                      )
# ZmmJets_onefake = Supergroup('ZmmJets_onefake',
#                      [ZmmJets_group],
#                      factor = 1.0,
#                      color = palette.bandgreen,
#                      style = 'fill',
#                      legendLabel = 'Zmm(1f)',
#                      stack = True,
#                      subset = istau + (onefaketau * onefaketau2) #+ SS
#                      )
# ZmmJets_twofakes = Supergroup('ZmmJets_twofakes',
#                      [ZmmJets_group],
#                      factor = 1.0,
#                      color = palette.bandgreen,
#                      style = 'fill',
#                      legendLabel = 'Zmm(2f)',
#                      stack = True,
#                      subset = twofaketau + istau
#                      )

# ZttJets_zerofakes = Supergroup('ZttJets_zerofakes',
#                      [ZttJets_group],
#                      factor = 1.0,
#                      color = palette.purple,
#                      style = 'fill',
#                      legendLabel = 'Ztt(true)',
#                      stack = True,
#                      subset = truetaus + istau# + SS
#                      )
# ZttJets_onefake = Supergroup('ZttJets_onefake',
#                      [ZttJets_group],
#                      factor = 1.0,
#                      color = palette.purple,
#                      style = 'fill',
#                      legendLabel = 'Ztt(1f)',
#                      stack = True,
#                      subset = istau + (onefaketau * onefaketau2) #+ SS
#                      )
# ZttJets_twofakes = Supergroup('ZttJets_twofakes',
#                      [ZttJets_group],
#                      factor = 1.0,
#                      color = palette.purple,
#                      style = 'fill',
#                      legendLabel = 'Ztt(2f)',
#                      stack = True,
#                      subset = twofaketau + istau
#                      )
# AntitauEvents = Supergroup('AntitauEvents',
# [#Data_group_1AntiTau_1,
# #                          Data_group_1AntiTau_2,
# #                           Data_group_2AntiTaus,
# Data_group_ZH_AntiTau,
# MCcorr_fakes_group,
#                             ],
#                             factor = 1.0,
#                             color = palette.green,
#                             style = 'fill',
#                             legendLabel = 'Fake tau',
#                             stack = True,
#                             )
#ttbar_dilep = Supergroup('tt_dilep_zerofakes',
#                        [ttbar_dilepton_group],
#factor = 1.0,
                         #                        color = palette.grey,
                         #style = 'fill',
                         #legendLabel = 'tt dilep(true)',
                         #stack = True,
                         #subset = isreal + truetaus2#truetaus#truthObj#isreal + truetaus #istau + truetaus
                         #)
                         #ttbar_lepfil = Supergroup('tt_lepfil_zerofakes',
                         #[ttbar_lepfil_group],
                         #factor = 1.0,
                         # color = palette.yellow,
                         #style = 'fill',
                         #legendLabel = 'tt lepfil(true)',
                         #stack = True,
                         #subset = isreal + truetaus2#truetaus#truthObj#isreal + truetaus #istau + truetaus
                         #)
                         #ttbar_allhad = Supergroup('tt_allhad_zerofakes',
                         #[ttbar_allhad_group],
                         #factor = 1.0,
                         #color = palette.blue,
                         #style = 'fill',
                         #legendLabel = 'tt allhad(true)',
                         #stack = True,
                         #subset = isreal + truetaus2#truetaus#truthObj#isreal + truetaus #istau + truetaus
                         #)
tt = Supergroup('tt',
                [tt_group],
                factor = 1.0,
                color = palette.pink,
                style = 'fill',
                legendLabel = 'ttbar',
                stack = True,
                subset = istau #+ SS
                )
tt_onefake = Supergroup('tt_onefake',
                [tt_group],
                factor = 1.0,
                color = palette.darkred,
                style = 'fill',
                legendLabel = 'tt(1f)',
                stack = True,
                subset = istau + (onefaketau * onefaketau2)# + SS
                )
tt_twofakes = Supergroup('tt_twofakes',
                [tt_group],
                factor = 1.0,
                color = palette.red,
                style = 'fill',
                legendLabel = 'tt(2f)',
                stack = True,
                subset = istau + twofaketau
                )

ZZ = Supergroup('ZZ',
                [ZZ_group],
                factor = 1.0,
                color = palette.orange,
                style = 'fill',
                legendLabel = 'ZZ',
                stack = True,
                subset = istau #+ SS 
                )
ZZ_onefake = Supergroup('ZZ_onefake',
                        [ZZ_group],
                        factor = 1.0,
                        color = palette.orange,
                        style = 'fill',
                        legendLabel = 'ZZ(1f)',
                        stack = True,
                        subset = istau + (onefaketau * onefaketau2) + SS
                        )
ZZ_twofakes = Supergroup('ZZ_twofakes',
                         [ZZ_group],
                         factor = 1.0,
                         color = palette.orange,
                         style = 'fill',
                         legendLabel = 'ZZ(2f)',
                         stack = True,
                         subset = istau + twofaketau
                         )                        

WZ = Supergroup('WZ',
                [WZ_group],
                factor = 1.0,
                color = palette.teal,
                style = 'fill',
                legendLabel = 'WZ',
                stack = True,
                subset = istau #+ SS
                )
WZ_onefake = Supergroup('WZ_onefake',
                        [WZ_group],
                        factor = 1.0,
                        color = palette.teal,
                        style = 'fill',
                        legendLabel = 'WZ(1f)',
                        stack = True,
                        subset = istau + (onefaketau * onefaketau2) #+ SS
                        )
WZ_twofakes = Supergroup('WZ_twofakes',
                         [WZ_group],
                         factor = 1.0,
                         color = palette.teal,
                         style = 'fill',
                         legendLabel = 'WZ(2f)',
                         stack = True,
                         subset = istau + twofaketau# + SS
                         )
