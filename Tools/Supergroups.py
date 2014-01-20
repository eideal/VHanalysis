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
                  subset = istau #+ SS
                  )
AntitauEvents = Supergroup('AntitauEvents',
                     [Data_group_1AntiTau,
                      Data_group_2AntiTaus,
                      Data_group_1AntiTau_2,
                      Data_group_2AntiTaus_2,
                      Data_group_1AntiTau_3,
                      Data_group_2AntiTaus_3,
                      Data_group_1AntiTau_4,
                      Data_group_2AntiTaus_4],
                     factor = 1.0,
                     color = palette.green,
                     style = 'fill',
                     legendLabel = 'Fake tau',
                     stack = True,
#subset = antitau2 * antitau3 #+ SS
#subset = antitau * antitau2 * antitau3
#subset = antitau2
#subset = antitau3
                     )
#AntiTauEvents_2AntiTau = Supergroup('AntiTauEvents_2AntiTau',
#                                   [Data_group],
#                                   factor = -1.0,
#                                   color = palette.green,
#                                   style = 'fill',
#                                   legendLabel = 'Faketau_sub',
#                                   stack = True,
#                                   subset  = antitau
#                                   )
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
                  subset = SSS
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


WeJets = Supergroup('WeJets',
                    [WeJets_group],
                    factor = 1.0,
                    color = palette.green,
                    style = 'fill',
                    legendLabel = 'WenuJets',
                    stack = True,
                    subset = istau #+ SS
)

WmJets = Supergroup('WmJets',
                    [WmJets_group],
                    factor = 1.0,
                    color = palette.brown,
                    style = 'fill',
                    legendLabel = 'WmunuJets',
                    stack = True,
                    subset = istau #+ SS
                    )
WmJets_zerofakes = Supergroup('WmJets_zerofakes',
                             [WmJets_group],
                             factor = 1.0,
                             color = palette.brown,
                             style = 'fill',
                             legendLabel = 'WmJets(true)',
                             stack = True,
                             subset = truetaus + istau
                             )
WmJets_onefake = Supergroup('WmJets_onefake',
                             [WmJets_group],
                             factor = 1.0,
                             color = palette.brown,
                             style = 'fill',
                             legendLabel = 'WmJets(1 fake)',
                             stack = True,
                             subset = istau + (onefaketau * onefaketau2)
                             )
WmJets_twofakes = Supergroup('WmJets_twofakes',
                             [WmJets_group],
                             factor = 1.0,
                             color = palette.brown,
                             style = 'fill',
                             legendLabel = 'WmJets(2 fakes)',
                             stack = True,
                             subset = istau + twofaketau
                             )
                                                          
WtJets = Supergroup('WtJets',
                    [WtJets_group],
                    factor = 1.0,
                    color = palette.peach,
                    style = 'fill',
                    legendLabel = 'WtaunuJets',
                    stack = True,
                    subset = istau# + SS
                    )
ZeeJets = Supergroup('ZeeJets',
                     [ZeeJets_group],
                     factor = 1.0,
                     color = palette.bandyellow,
                     style = 'fill',
                     legendLabel = 'ZeeJets',
                     stack = True,
                     subset = istau# + SS
                     )
ZmmJets = Supergroup('ZmmJets',
                     [ZmmJets_group],
                     factor = 1.0, ###k-factor
                     color = palette.bandgreen,
                     style = 'fill',
                     legendLabel = 'ZmumuJets',
                     stack = True,
                     subset = istau #+ SS
                     )
ZmmJets_zerofakes = Supergroup('ZmmJets_zerofakes',
                     [ZmmJets_group],
                     factor = 1.0,
                     color = palette.bandgreen,
                     style = 'fill',
                     legendLabel = 'Zmm(true)',
                     stack = True,
                     subset = truetaus + istau #+ SS
                     )
ZmmJets_onefake = Supergroup('ZmmJets_onefake',
                     [ZmmJets_group],
                     factor = 1.0,
                     color = palette.bandgreen,
                     style = 'fill',
                     legendLabel = 'Zmm(1f)',
                     stack = True,
                     subset = istau + (onefaketau * onefaketau2) #+ SS
                     )
ZmmJets_twofakes = Supergroup('ZmmJets_twofakes',
                     [ZmmJets_group],
                     factor = 1.0,
                     color = palette.bandgreen,
                     style = 'fill',
                     legendLabel = 'Zmm(2f)',
                     stack = True,
                     subset = twofaketau + istau
                     )

ZttJets = Supergroup('ZttJets',
                     [ZttJets_group],
                     factor = 1.0,
                     color = palette.purple,
                     style = 'fill',
                     legendLabel = 'ZtautauJets',
                     stack = True,
                     subset = istau #+ SS
                     )
ZttJets_zerofakes = Supergroup('ZttJets_zerofakes',
                     [ZttJets_group],
                     factor = 1.0,
                     color = palette.purple,
                     style = 'fill',
                     legendLabel = 'Ztt(true)',
                     stack = True,
                     subset = truetaus + istau# + SS
                     )
ZttJets_onefake = Supergroup('ZttJets_onefake',
                     [ZttJets_group],
                     factor = 1.0,
                     color = palette.purple,
                     style = 'fill',
                     legendLabel = 'Ztt(1f)',
                     stack = True,
                     subset = istau + (onefaketau * onefaketau2) #+ SS
                     )
ZttJets_twofakes = Supergroup('ZttJets_twofakes',
                     [ZttJets_group],
                     factor = 1.0,
                     color = palette.purple,
                     style = 'fill',
                     legendLabel = 'Ztt(2f)',
                     stack = True,
                     subset = twofaketau + istau
                     )

tt = Supergroup('tt',
                [tt_group],
                factor = 1.0,
                color = palette.pink,
                style = 'fill',
                legendLabel = 'ttbar',
                stack = True,
                subset = istau #+ SS
                )
tt_zerofakes = Supergroup('tt_zerofakes',
                [tt_group],
                factor = 1.0,
                color = palette.pink,
                style = 'fill',
                legendLabel = 'tt(true)',
                stack = True,
                subset = istau + truetaus #+ SS
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

SingleTop = Supergroup('SingleTop',
                       [SingleTop_group],
                       factor = 1.0,
                       color = palette.red,
                       style = 'fill',
                       legendLabel = 'SingleTop',
                       stack = True,
                       subset = istau #+ SS
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
ZZ_zerofakes = Supergroup('ZZ_zerofakes',
                          [ZZ_group],
                          factor = 1.0,
                          color = palette.orange,
                          style = 'fill',
                          legendLabel = 'ZZ(true)',
                          stack = True,
                          subset = istau + truetaus #+ SS
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
                          
WW = Supergroup('WW',
                [WW_group],
                factor = 1.0,
                color = palette.indigo,
                style = 'fill',
                legendLabel = 'WW',
                stack = True,
                subset = istau #+ SS
                )
WGamma = Supergroup('WGamma',
                    [WGamma_group],
                    factor = 1.0,
                    color = palette.grey,
                    style = 'fill',
                    legendLabel = 'WGamma',
                    stack = True,
                    subset = istau# + SS
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
WZ_zerofakes = Supergroup('WZ_zerofakes',
                [WZ_group],
                factor = 1.0,
                color = palette.teal,
                style = 'fill',
                legendLabel = 'WZ(true)',
                stack = True,
                subset = istau + truetaus #+ SS
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
                    

##### SIGNAL ########### SIGNAL ############# SIGNAL ######
WH100 = Supergroup('WH100',
                [WH100_group],
                factor = 1.0,
                color = palette.black,
                style = 'line',
                legendLabel = 'WH100',
                stack = False,
                subset = istau
                )
WH105 = Supergroup('WH105',
                [WH105_group],
                factor = 1.0,
                color = palette.black,
                style = 'line',
                legendLabel = 'WH105',
                stack = False,
                subset = istau
                )
WH110 = Supergroup('WH110',
                [WH110_group],
                factor = 1.0,
                color = palette.black,
                style = 'line',
                legendLabel = 'WH110',
                stack = False,
                subset = istau
                )
WH115 = Supergroup('WH115',
                [WH115_group],
                factor = 1.0,
                color = palette.black,
                style = 'line',
                legendLabel = 'WH115',
                stack = False,
                subset = istau
                )
#WH120 = Supergroup('WH120',
#               [WH120_group],
#               factor = 1.0,
#               color = palette.black,
#               style = 'line',
#               legendLabel = 'WH120',
#               stack = False,
#               subset = istau
#               )
WH125 = Supergroup('WH125',
                [WH125_group],
                factor = 1.0,
                color = palette.black,
                style = 'line',
                legendLabel = 'WH125',
                stack = False,
                subset = istau
                )
WH130 = Supergroup('WH130',
                [WH130_group],
                factor = 1.0,
                color = palette.black,
                style = 'line',
                legendLabel = 'WH130',
                stack = False,
                subset = istau
                )
WH135 = Supergroup('WH135',
                [WH135_group],
                factor = 1.0,
                color = palette.black,
                style = 'line',
                legendLabel = 'WH135',
                stack = False,
                subset = istau
                )
WH140 = Supergroup('WH140',
                [WH140_group],
                factor = 1.0,
                color = palette.black,
                style = 'line',
                legendLabel = 'WH140',
                stack = False,
                subset = istau
                )
WH145 = Supergroup('WH145',
                [WH145_group],
                factor = 1.0,
                color = palette.black,
                style = 'line',
                legendLabel = 'WH145',
                stack = False,
                subset = istau
                )
WH150 = Supergroup('WH150',
                [WH150_group],
                factor = 1.0,
                color = palette.black,
                style = 'line',
                legendLabel = 'WH150',
                stack = False,
                subset = istau
                )
###
ZH100 = Supergroup('ZH100',
                [ZH100_group],
                factor = 1.0,
                color = palette.black,
                style = 'line',
                legendLabel = 'ZH100',
                stack = False,
                subset = istau
                )
ZH105 = Supergroup('ZH105',
                [ZH105_group],
                factor = 1.0,
                color = palette.black,
                style = 'line',
                legendLabel = 'ZH105',
                stack = False,
                subset = istau
                )
ZH110 = Supergroup('ZH110',
                [ZH110_group],
                factor = 1.0,
                color = palette.black,
                style = 'line',
                legendLabel = 'ZH110',
                stack = False,
                subset = istau
                )
ZH115 = Supergroup('ZH115',
                [ZH115_group],
                factor = 1.0,
                color = palette.black,
                style = 'line',
                legendLabel = 'ZH115',
                stack = False,
                subset = istau
                )
ZH120 = Supergroup('ZH120',
                [ZH120_group],
                factor = 1.0,
                color = palette.black,
                style = 'line',
                legendLabel = 'ZH120',
                stack = False,
                subset = istau
                )
ZH125 = Supergroup('ZH125',
                [ZH125_group],
                factor = 1.0,
                color = palette.black,
                style = 'line',
                legendLabel = 'ZH125',
                stack = False,
                subset = istau
                )
ZH130 = Supergroup('ZH130',
                [ZH130_group],
                factor = 1.0,
                color = palette.black,
                style = 'line',
                legendLabel = 'ZH130',
                stack = False,
                subset = istau
                )
ZH135 = Supergroup('ZH135',
                [ZH135_group],
                factor = 1.0,
                color = palette.black,
                style = 'line',
                legendLabel = 'ZH135',
                stack = False,
                subset = istau
                )
ZH140 = Supergroup('ZH140',
                [ZH140_group],
                factor = 1.0,
                color = palette.black,
                style = 'line',
                legendLabel = 'ZH140',
                stack = False,
                subset = istau
                )
ZH145 = Supergroup('ZH145',
                [ZH145_group],
                factor = 1.0,
                color = palette.black,
                style = 'line',
                legendLabel = 'ZH145',
                stack = False,
                subset = istau
                )
ZH150 = Supergroup('ZH150',
                [ZH150_group],
                factor = 1.0,
                color = palette.black,
                style = 'line',
                legendLabel = 'ZH150',
                stack = False,
                subset = istau
                )
####
VBFH100 = Supergroup('VBFH100',
                [VBFH100_group],
                factor = 1.0,
                color = palette.black,
                style = 'line',
                legendLabel = 'VBFH100',
                stack = False,
                subset = istau
                )
VBFH105 = Supergroup('VBFH105',
                [VBFH105_group],
                factor = 1.0,
                color = palette.black,
                style = 'line',
                legendLabel = 'VBFH105',
                stack = False,
                subset = istau
                )
VBFH110 = Supergroup('VBFH110',
                [VBFH110_group],
                factor = 1.0,
                color = palette.black,
                style = 'line',
                legendLabel = 'VBFH110',
                stack = False,
                subset = istau
                )
VBFH115 = Supergroup('VBFH115',
                [VBFH115_group],
                factor = 1.0,
                color = palette.black,
                style = 'line',
                legendLabel = 'VBFH115',
                stack = False,
                subset = istau
                )
VBFH120 = Supergroup('VBFH120',
                [VBFH120_group],
                factor = 1.0,
                color = palette.black,
                style = 'line',
                legendLabel = 'VBFH120',
                stack = False,
                subset = istau
                )
VBFH125 = Supergroup('VBFH125',
                [VBFH125_group],
                factor = 1.0,
                color = palette.black,
                style = 'line',
                legendLabel = 'VBFH125',
                stack = False,
                subset = istau
                )
VBFH130 = Supergroup('VBFH130',
                [VBFH130_group],
                factor = 1.0,
                color = palette.black,
                style = 'line',
                legendLabel = 'VBFH130',
                stack = False,
                subset = istau
                )
VBFH135 = Supergroup('VBFH135',
                [VBFH135_group],
                factor = 1.0,
                color = palette.black,
                style = 'line',
                legendLabel = 'VBFH135',
                stack = False,
                subset = istau
                )
VBFH140 = Supergroup('VBFH140',
                [VBFH140_group],
                factor = 1.0,
                color = palette.black,
                style = 'line',
                legendLabel = 'VBFH140',
                stack = False,
                subset = istau
                )
VBFH145 = Supergroup('VBFH145',
                [VBFH145_group],
                factor = 1.0,
                color = palette.black,
                style = 'line',
                legendLabel = 'VBFH145',
                stack = False,
                subset = istau
                )
VBFH150 = Supergroup('VBFH150',
                [VBFH150_group],
                factor = 1.0,
                color = palette.black,
                style = 'line',
                legendLabel = 'VBFH150',
                stack = False,
                subset = istau
                )
#####
ggH100 = Supergroup('ggH100',
                [ggH100_group],
                factor = 1.0,
                color = palette.black,
                style = 'line',
                legendLabel = 'ggH100',
                stack = False,
                subset = istau
                )
ggH105 = Supergroup('ggH105',
                [ggH105_group],
                factor = 1.0,
                color = palette.black,
                style = 'line',
                legendLabel = 'ggH105',
                stack = False,
                subset = istau
                )
ggH110 = Supergroup('ggH110',
                [ggH110_group],
                factor = 1.0,
                color = palette.black,
                style = 'line',
                legendLabel = 'ggH110',
                stack = False,
                subset = istau
                )
ggH115 = Supergroup('ggH115',
                [ggH115_group],
                factor = 1.0,
                color = palette.black,
                style = 'line',
                legendLabel = 'ggH115',
                stack = False,
                subset = istau
                )
ggH120 = Supergroup('ggH120',
                [ggH120_group],
                factor = 1.0,
                color = palette.black,
                style = 'line',
                legendLabel = 'ggH120',
                stack = False,
                subset = istau
                )
ggH125 = Supergroup('ggH125',
                [ggH125_group],
                factor = 1.0,
                color = palette.black,
                style = 'line',
                legendLabel = 'ggH125',
                stack = False,
                subset = istau
                )
ggH130 = Supergroup('ggH130',
                [ggH130_group],
                factor = 1.0,
                color = palette.black,
                style = 'line',
                legendLabel = 'ggH130',
                stack = False,
                subset = istau
                )
ggH135 = Supergroup('ggH135',
                [ggH135_group],
                factor = 1.0,
                color = palette.black,
                style = 'line',
                legendLabel = 'ggH135',
                stack = False,
                subset = istau
                )
ggH140 = Supergroup('ggH140',
                [ggH140_group],
                factor = 1.0,
                color = palette.black,
                style = 'line',
                legendLabel = 'ggH140',
                stack = False,
                subset = istau
                )
ggH145 = Supergroup('ggH145',
                [ggH145_group],
                factor = 1.0,
                color = palette.black,
                style = 'line',
                legendLabel = 'ggH145',
                stack = False,
                subset = istau
                )
ggH150 = Supergroup('ggH150',
                [ggH150_group],
                factor = 1.0,
                color = palette.black,
                style = 'line',
                legendLabel = 'ggH150',
                stack = False,
                subset = istau
                )
