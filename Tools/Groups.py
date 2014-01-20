from Group import Group
from Samples import *
from Subsets import *
import palette

Data_group = Group('Data',
             [Egamma,
              JetTauEtmiss,
              Muons],
              factor = 1.0,
              classification = 'DATA'
              ) 
Data_group_1AntiTau = Group('Data_1AntiTau', ##1 anti-tau + 1 selected tau, no extra jets in data event that could be an antitau
                            [Egamma,
                             JetTauEtmiss,
                             Muons],
                             factor = 1.0,
                             classification = 'DATA',
                             subset = antitau2 * antitau3
                             )
Data_group_2AntiTaus = Group('Data_2AntiTaus', #2 anti-taus, no extra jets in event that could be an anti-tau
                             [Egamma,
                              JetTauEtmiss,
                              Muons],
                              factor = -1.0,
                              classification = 'DATA',
                              subset = antitau
                              )
Data_group_1AntiTau_2 = Group('Data_1AntiTau_2', #1 anti-tau + 1 selected tau + 1 jet in the event that could also be the anti-tau
                              [Egamma,
                               JetTauEtmiss,
                               Muons],
                               factor = 0.5,
                               classification = 'DATA',
                               subset = antitau4 * antitau5
                               )
Data_group_2AntiTaus_2 = Group('Data_2AntiTaus_2', #2 anti-taus + 1 add. jet in the event that could also be an anti-tau
                               [Egamma,
                                JetTauEtmiss,
                                Muons],
                                factor = -.667,
                                classification = 'DATA',
                                subset = antitau6
                                )
Data_group_1AntiTau_3 = Group('Data_1AntiTau_3', #1 anti-tau + 1 selected tau + 2 add. jets in the event that could be anti-taus
                              [Egamma,
                               JetTauEtmiss,
                               Muons],
                               factor = 0.333,
                               classification = 'DATA',
                               subset = antitau8 * antitau9
                               )
Data_group_2AntiTaus_3 = Group('Data_2AntiTaus_3', #2 anti-taus + 2 add. jets in the event that could be anti-taus
                               [Egamma,
                               JetTauEtmiss,
                               Muons],
                               factor = -0.5,
                               classification = 'DATA',
                               subset = antitau7
                               )
Data_group_1AntiTau_4 = Group('Data_1AntiTau_4', #1 anti-tau + 1 selected tau + 3 add. jets in the event that could also be the anti-tau
                              [Egamma,
                               JetTauEtmiss,
                               Muons],
                               factor = 0.25,
                               classification = 'DATA',
                               subset = antitau10 * antitau11
                               )
Data_group_2AntiTaus_4 = Group('Data_2AntiTaus_4', #2 anti-taus + 3 add. jets in the event that could also be the anti-tau
                              [Egamma,
                               JetTauEtmiss,
                               Muons],
                               factor = -0.4,
                               classification = 'DATA',
                               subset = antitau12
                               )

                        


DataSSS_group = Group('DataSSS',
                [Egamma,
                 JetTauEtmiss,
                 Muons],
                 factor = 1.0,
                 classification = 'DATA'
                 )
WeJets_group = Group('WeJets',
               [WenuNp0_Auto,
                WenuNp1_Auto,
                WenuNp2_Auto,
                WenuNp3_Auto,
                WenuNp4_Auto,
                WenuNp5incl_Auto,
                ],
                factor = 1.0,
                classification = 'BG'
                )
SSSWeJets_group = Group('SSSWeJets',
                  [WenuNp0_Auto,
                   WenuNp1_Auto,
                   WenuNp2_Auto,
                   WenuNp3_Auto,
                   WenuNp4_Auto,
                   WenuNp5incl_Auto,
                   ],
                   factor = -1.0,
                   classification = 'BG'
                   )
WmJets_group = Group('WmJets',
               [WmunuNp0_Auto,
                WmunuNp1_Auto,
                WmunuNp2_Auto,
                WmunuNp3_Auto,
                WmunuNp4_Auto,
                WmunuNp5incl_Auto,
                ],
                factor = 1.0,
                classification = 'BG'
                )
SSSWmJets_group = Group('SSSWmJets',
               [WmunuNp0_Auto,
                WmunuNp1_Auto,
                WmunuNp2_Auto,
                WmunuNp3_Auto,
                WmunuNp4_Auto,
                WmunuNp5incl_Auto,
                ],
                factor = -1.0,
                classification = 'BG'
                )
WtJets_group = Group('WtJets',
               [WtaunuNp0_Auto,
                WtaunuNp1_Auto,
                WtaunuNp2_Auto,
                WtaunuNp3_Auto,
                WtaunuNp4_Auto,
                WtaunuNp5incl_Auto,
                ],
                factor = 1.0,
                classification = 'BG'
                )
SSSWtJets_group = Group('SSSWtJets',
                  [WtaunuNp0_Auto,
                   WtaunuNp1_Auto,
                   WtaunuNp2_Auto,
                   WtaunuNp3_Auto,
                   WtaunuNp4_Auto,
                   WtaunuNp5incl_Auto,
                   ],
                   factor = -1.0,
                   classification = 'BG'
                   )
ZeeJets_group = Group('ZeeJets',
                [ZeeNp0_Auto,
                 ZeeNp1_Auto,
                 ZeeNp2_Auto,
                 ZeeNp3_Auto,
                 ZeeNp4_Auto,
                 ZeeNp5incl_Auto,
                 Filtered_ZeeNp0Excl_Mll10to60,
                 Filtered_ZeeNp1Excl_Mll10to60,
                 Filtered_ZeeNp2Excl_Mll10to60,
                 Filtered_ZeeNp3Excl_Mll10to60,
                 Filtered_ZeeNp4Excl_Mll10to60,
#ZeeNp0Excl_Mll10to60,
#                ZeeNp1Excl_Mll10to60,
#                ZeeNp2Excl_Mll10to60,
#                ZeeNp3Excl_Mll10to60,
#                ZeeNp4Excl_Mll10to60,
#                ZeeNp5Incl_Mll10to60,
],
                 factor = 1.0,
                 classification = 'BG'
                 )
SSSZeeJets_group = Group('SSSZeeJets',
                   [ZeeNp0_Auto,
                    ZeeNp1_Auto,
                    ZeeNp2_Auto,
                    ZeeNp3_Auto,
                    ZeeNp4_Auto,
                    ZeeNp5incl_Auto,
                    ZeeNp0Excl_Mll10to60,
                    ZeeNp1Excl_Mll10to60,
                    ZeeNp2Excl_Mll10to60,
                    ZeeNp3Excl_Mll10to60,
                    ZeeNp4Excl_Mll10to60,
                    ZeeNp5Incl_Mll10to60,
                    ],
                    factor = -1.0,
                    classification = 'BG'
                    )
ZmmJets_group = Group('ZmmJets',
                [ZmumuNp0_Auto,
                 ZmumuNp1_Auto,
                 ZmumuNp2_Auto,
                 ZmumuNp3_Auto,
                 ZmumuNp4_Auto,
                 ZmumuNp5incl_Auto,
                 Filtered_ZmumuNp0Excl_Mll10to6,
                 Filtered_ZmumuNp1Excl_Mll10to6,
                 Filtered_ZmumuNp2Excl_Mll10to6,
                 Filtered_ZmumuNp3Excl_Mll10to6,
                 Filtered_ZmumuNp4Excl_Mll10to6,
#ZmumuNp0Excl_Mll10to60,
#                ZmumuNp1Excl_Mll10to60,
#                ZmumuNp2Excl_Mll10to60,
#                ZmumuNp3Excl_Mll10to60,
#                ZmumuNp4Excl_Mll10to60,
#                ZmumuNp5Incl_Mll10to60,
                 ],
                 factor = 1.0,
                 classification = 'BG'
                 )
SSSZmmJets_group = Group('SSSZmmJets',
                [ZmumuNp0_Auto,
                 ZmumuNp1_Auto,
                 ZmumuNp2_Auto,
                 ZmumuNp3_Auto,
                 ZmumuNp4_Auto,
                 ZmumuNp5incl_Auto,
                 ZmumuNp0Excl_Mll10to60,
                 ZmumuNp1Excl_Mll10to60,
                 ZmumuNp2Excl_Mll10to60,
                 ZmumuNp3Excl_Mll10to60,
                 ZmumuNp4Excl_Mll10to60,
                 ZmumuNp5Incl_Mll10to60,
                 ],
                 factor = -1.0,
                 classification = 'BG'
                 )
ZttJets_group = Group('ZttJets',
[#ZtautauNp0Excl_Mll10to60,
#               ZtautauNp1Excl_Mll10to60,
#                ZtautauNp2Excl_Mll10to60,
#                ZtautauNp3Excl_Mll10to60,
#                ZtautauNp4Excl_Mll10to60,
#                ZtautauNp5Incl_Mll10to60,
Filtered_ZtautauNp0Excl_Mll10to60,
Filtered_ZtautauNp1Excl_Mll10to60,
Filtered_ZtautauNp2Excl_Mll10to60,
Filtered_ZtautauNp3Excl_Mll10to60,
                 ZtautauNp0_Auto,
                 ZtautauNp1_Auto,
                 ZtautauNp2_Auto,
                 ZtautauNp3_Auto,
                 ZtautauNp4_Auto,
                 ZtautauNp5incl_Auto,
                 ],
                 factor = 1.0,
                 classification = 'BG'
                 )
SSSZttJets_group = Group('SSSZttJets',
                [ZtautauNp0Excl_Mll10to60,
                 ZtautauNp1Excl_Mll10to60,
                 ZtautauNp2Excl_Mll10to60,
                 ZtautauNp3Excl_Mll10to60,
                 ZtautauNp4Excl_Mll10to60,
                 ZtautauNp5Incl_Mll10to60,
                 ZtautauNp0_Auto,
                 ZtautauNp1_Auto,
                 ZtautauNp2_Auto,
                 ZtautauNp3_Auto,
                 ZtautauNp4_Auto,
                 ZtautauNp5incl_Auto,
                 ],
                 factor = -1.0,
                 classification = 'BG'
                 )
tt_group = Group('tt',
[#ttbar,
 ttbar_allhad,
ttbar_dilepton],
factor = 1.0,
classification = 'BG',
    )
SSStt_group = Group('SSStt',
[ttbar,
            ttbar_allhad,
# ttbar_dilepton],
],
factor = -1.0,
classification = 'BG',
    )
SingleTop_group = Group('SingleTop',
                  [SingleTopSChanWenu,
                   SingleTopSChanWmunu,
                   SingleTopSChanWtaunu,
                   SingleTopWtChanIncl,
                   singletop_tchan_e,
                   singletop_tchan_mu,
                   singletop_tchan_tau
                   ],
                   factor = 1.0,
                   classification = 'BG',
                   )
SSSSingleTop_group = Group('SSSSingleTop',
                  [SingleTopSChanWenu,
                   SingleTopSChanWmunu,
                   SingleTopSChanWtaunu,
                   SingleTopWtChanIncl,
                   singletop_tchan_e,
                   singletop_tchan_mu,
                   singletop_tchan_tau
                   ],
                   factor = -1.0,
                   classification = 'BG',
                   )
ZZ_group = Group('ZZ',
           [Powheg_ZZ_2e2mu_mll4_2pt5,
            Powheg_ZZ_2e2tau_mll4_2pt5,
            Powheg_ZZ_2mu2tau_mll4_2pt5,
            Powheg_ZZ_4e_mll4_2pt5,
            Powheg_ZZ_4mu_mll4_2pt5,
            Powheg_ZZ_4tau_mll4_2pt5,
            Powheg_ZZllnunu_ee_mll4,
            Powheg_ZZllnunu_mm_mll4,
            Powheg_ZZllnunu_tt_mll4,
            ],
            #ZZ],
            factor = 1.0,
            classification = 'BG',
            )
SSSZZ_group = Group('SSSZZ',
           [Powheg_ZZ_2e2mu_mll4_2pt5,
            Powheg_ZZ_2e2tau_mll4_2pt5,
            Powheg_ZZ_2mu2tau_mll4_2pt5,
            Powheg_ZZ_4e_mll4_2pt5,
            Powheg_ZZ_4mu_mll4_2pt5,
            Powheg_ZZ_4tau_mll4_2pt5,
            Powheg_ZZllnunu_ee_mll4,
            Powheg_ZZllnunu_mm_mll4,
            Powheg_ZZllnunu_tt_mll4,
            ],
            #ZZ],
            factor = -1.0,
            classification = 'BG',
            )
WW_group = Group('WW',
           [#WW,
            WWqqlnuNp0,
            WWqqlnuNp1,
            WWqqlnuNp2,
            WWqqlnuNp3,
            Powheg_WpWm_ee,
            Powheg_WpWm_em,
            Powheg_WpWm_et,
            Powheg_WpWm_me,
            Powheg_WpWm_mm,
            Powheg_WpWm_mt,
            Powheg_WpWm_te,
            Powheg_WpWm_tm,
            Powheg_WpWm_tt,
            gg2WW0240_WpWmenuenu,
            gg2WW0240_WpWmenumunu,
            gg2WW0240_WpWmenutaunu,
            gg2WW0240_WpWmmunuenu,
            gg2WW0240_WpWmmunumunu,
            gg2WW0240_WpWmmunutaunu,
            gg2WW0240_WpWmtaunuenu,
            gg2WW0240_WpWmtaunumunu,
            gg2WW0240_WpWmtaunutaunu
            ],
            factor = 1.0,
            classification = 'BG',
            )
SSSWW_group = Group('SSSWW',
           [#WW,
            WWqqlnuNp0,
            WWqqlnuNp1,
            WWqqlnuNp2,
            WWqqlnuNp3,
            Powheg_WpWm_ee,
            Powheg_WpWm_em,
            Powheg_WpWm_et,
            Powheg_WpWm_me,
            Powheg_WpWm_mm,
            Powheg_WpWm_mt,
            Powheg_WpWm_te,
            Powheg_WpWm_tm,
            Powheg_WpWm_tt,
            gg2WW0240_WpWmenuenu,
            gg2WW0240_WpWmenumunu,
            gg2WW0240_WpWmenutaunu,
            gg2WW0240_WpWmmunuenu,
            gg2WW0240_WpWmmunumunu,
            gg2WW0240_WpWmmunutaunu,
            gg2WW0240_WpWmtaunuenu,
            gg2WW0240_WpWmtaunumunu,
            gg2WW0240_WpWmtaunutaunu
            ],
            factor = -1.0,
            classification = 'BG',
            )
WGamma_group = Group('WGamma',
               [WgammaNp0,
                WgammaNp1,
                WgammaNp2,
                WgammaNp3,
                WgammaNp4,
                WgammaNp5,
                MadGraph_lnuee_lt7,
                MadGraph_lnumumu_lt7,
                MadGraph_lnutautau_lt7],
                factor = 1.0,
                classification = 'BG',
                )
SSSWGamma_group = Group('SSSWGamma',
               [WgammaNp0,
                WgammaNp1,
                WgammaNp2,
                WgammaNp3,
                WgammaNp4,
                WgammaNp5,
                MadGraph_lnuee_lt7,
                MadGraph_lnumumu_lt7,
                MadGraph_lnutautau_lt7],
                factor = -1.0,
                classification = 'BG',
                )
WZ_group = Group('WZ',
           [Powheg_WZ_W11Z11_mll0p250d0_2LeptonFilter5,
            Powheg_WZ_W11Z13_mll0p4614d0_2LeptonFilter5,
            Powheg_WZ_W11Z15_mll3p804d0_2LeptonFilter5,
            Powheg_WZ_W13Z11_mll0p250d0_2LeptonFilter5,
            Powheg_WZ_W13Z13_mll0p4614d0_2LeptonFilter5,
            Powheg_WZ_W13Z15_mll3p804d0_2LeptonFilter5,
            Powheg_WZ_W15Z11_mll0p250d0_2LeptonFilter5,
            Powheg_WZ_W15Z13_mll0p4614d0_2LeptonFilter5,
            Powheg_WZ_W15Z15_mll3p804d0_2LeptonFilter5,
            Powheg_WZ_Wm11Z11_mll0p250d0_2LeptonFilter5,
            Powheg_WZ_Wm11Z13_mll0p4614d0_2LeptonFilter5,
            Powheg_WZ_Wm11Z15_mll3p804d0_2LeptonFilter5,
            Powheg_WZ_Wm13Z11_mll0p250d0_2LeptonFilter5,
            Powheg_WZ_Wm13Z13_mll0p4614d0_2LeptonFilter5,
            Powheg_WZ_Wm13Z15_mll3p804d0_2LeptonFilter5,
            Powheg_WZ_Wm15Z11_mll0p250d0_2LeptonFilter5,
            Powheg_WZ_Wm15Z13_mll0p4614d0_2LeptonFilter5,
            Powheg_WZ_Wm15Z15_mll3p804d0_2LeptonFilter5,
            ],
#WZ],
            factor = 1.0,
            classification = 'BG',
            )
SSSWZ_group = Group('SSSWZ',
           [Powheg_WZ_W11Z11_mll0p250d0_2LeptonFilter5,
            Powheg_WZ_W11Z13_mll0p4614d0_2LeptonFilter5,
            Powheg_WZ_W11Z15_mll3p804d0_2LeptonFilter5,
            Powheg_WZ_W13Z11_mll0p250d0_2LeptonFilter5,
            Powheg_WZ_W13Z13_mll0p4614d0_2LeptonFilter5,
            Powheg_WZ_W13Z15_mll3p804d0_2LeptonFilter5,
            Powheg_WZ_W15Z11_mll0p250d0_2LeptonFilter5,
            Powheg_WZ_W15Z13_mll0p4614d0_2LeptonFilter5,
            Powheg_WZ_W15Z15_mll3p804d0_2LeptonFilter5,
            Powheg_WZ_Wm11Z11_mll0p250d0_2LeptonFilter5,
            Powheg_WZ_Wm11Z13_mll0p4614d0_2LeptonFilter5,
            Powheg_WZ_Wm11Z15_mll3p804d0_2LeptonFilter5,
            Powheg_WZ_Wm13Z11_mll0p250d0_2LeptonFilter5,
            Powheg_WZ_Wm13Z13_mll0p4614d0_2LeptonFilter5,
            Powheg_WZ_Wm13Z15_mll3p804d0_2LeptonFilter5,
            Powheg_WZ_Wm15Z11_mll0p250d0_2LeptonFilter5,
            Powheg_WZ_Wm15Z13_mll0p4614d0_2LeptonFilter5,
            Powheg_WZ_Wm15Z15_mll3p804d0_2LeptonFilter5,
            ],
#WZ],
            factor = -1.0,
            classification = 'BG',
            )       
##### WH Signals
WH100_group = Group('WH100',
                    [WH100_tautauhh],
                    factor = 1.0,
                    classification = 'SIG'
                    )                    
WH105_group = Group('WH105',
           [WH105_tautauhh],
           factor = 1.0,
           classification = 'SIG'
           )
WH110_group = Group('WH110',
           [WH110_tautauhh],
           factor = 1.0,
           classification = 'SIG'
           )
WH115_group = Group('WH115',
           [WH115_tautauhh],
           factor = 1.0,
           classification = 'SIG'
           )
#WH120_group = Group('WH120',
#          [WH120_tautauhh],
#          factor = 1.0,
#          classification = 'SIG'
#          )
WH125_group = Group('WH125',
           [WH125_tautauhh],
           factor = 1.0,
           classification = 'SIG'
           )
WH130_group = Group('WH130',
           [WH130_tautauhh],
           factor = 1.0,
           classification = 'SIG'
           )
WH135_group = Group('WH135',
           [WH135_tautauhh],
           factor = 1.0,
           classification = 'SIG'
           )
WH140_group = Group('WH140',
           [WH140_tautauhh],
           factor = 1.0,
           classification = 'SIG'
           )
WH145_group = Group('WH145',
           [WH145_tautauhh],
           factor = 1.0,
           classification = 'SIG'
           )
WH150_group = Group('WH150',
           [WH150_tautauhh],
           factor = 1.0,
           classification = 'SIG'
           )
###### ZH Signals
ZH100_group = Group('ZH100',
           [ZH100_tautauhh],
           factor = 1.0,
           classification = 'SIG'
           )
ZH105_group = Group('ZH105',
           [ZH105_tautauhh],
           factor = 1.0,
           classification = 'SIG'
           )
ZH110_group = Group('ZH110',
           [ZH110_tautauhh],
           factor = 1.0,
           classification = 'SIG'
           )
ZH115_group = Group('ZH115',
           [ZH115_tautauhh],
           factor = 1.0,
           classification = 'SIG'
           )
ZH120_group = Group('ZH120',
           [ZH120_tautauhh],
           factor = 1.0,
           classification = 'SIG'
           )
ZH125_group = Group('ZH125',
           [ZH125_tautauhh],
           factor = 1.0,
           classification = 'SIG'
           )
ZH130_group = Group('ZH130',
           [ZH130_tautauhh],
           factor = 1.0,
           classification = 'SIG'
           )
ZH135_group = Group('ZH135',
           [ZH135_tautauhh],
           factor = 1.0,
           classification = 'SIG'
           )
ZH140_group = Group('ZH140',
           [ZH140_tautauhh],
           factor = 1.0,
           classification = 'SIG'
           )
ZH145_group = Group('ZH145',
           [ZH145_tautauhh],
           factor = 1.0,
           classification = 'SIG'
           )
ZH150_group = Group('ZH150',
           [ZH150_tautauhh],
           factor = 1.0,
           classification = 'SIG'
           )
##### VBF hh Signals
VBFH100_group = Group('VBFH100',
           [VBFH100_tautauhh],
           factor = 1.0,
           classification = 'SIG'
           )
VBFH105_group = Group('VBFH105',
           [VBFH105_tautauhh],
           factor = 1.0,
           classification = 'SIG'
           )
VBFH110_group = Group('VBFH110',
           [VBFH110_tautauhh],
           factor = 1.0,
           classification = 'SIG'
           )
VBFH115_group = Group('VBFH115',
           [VBFH115_tautauhh],
           factor = 1.0,
           classification = 'SIG'
           )
VBFH120_group = Group('VBFH120',
           [VBFH120_tautauhh],
           factor = 1.0,
           classification = 'SIG'
           )
VBFH125_group = Group('VBFH125',
           [VBFH125_tautauhh],
           factor = 1.0,
           classification = 'SIG'
           )
VBFH130_group = Group('VBFH130',
           [VBFH130_tautauhh],
           factor = 1.0,
           classification = 'SIG'
           )
VBFH135_group = Group('VBFH135',
           [VBFH135_tautauhh],
           factor = 1.0,
           classification = 'SIG'
           )
VBFH140_group = Group('VBFH140',
           [VBFH140_tautauhh],
           factor = 1.0,
           classification = 'SIG'
           )
VBFH145_group = Group('VBFH145',
           [VBFH145_tautauhh],
           factor = 1.0,
           classification = 'SIG'
           )
VBFH150_group = Group('VBFH150',
           [VBFH150_tautauhh],
           factor = 1.0,
           classification = 'SIG'
           )

##### ggF Signals
ggH100_group = Group('ggH100',
           [ggH100_tautauhh],
           factor = 1.0,
           classification = 'SIG'
           )
ggH105_group = Group('ggH105',
           [ggH105_tautauhh],
           factor = 1.0,
           classification = 'SIG'
           )
ggH110_group = Group('ggH110',
           [ggH110_tautauhh],
           factor = 1.0,
           classification = 'SIG'
           )
ggH115_group = Group('ggH115',
           [ggH115_tautauhh],
           factor = 1.0,
           classification = 'SIG'
           )
ggH120_group = Group('ggH120',
           [ggH120_tautauhh],
           factor = 1.0,
           classification = 'SIG'
           )
ggH125_group = Group('ggH125',
           [ggH125_tautauhh],
           factor = 1.0,
           classification = 'SIG'
           )
ggH130_group = Group('ggH130',
           [ggH130_tautauhh],
           factor = 1.0,
           classification = 'SIG'
           )
ggH135_group = Group('ggH135',
           [ggH135_tautauhh],
           factor = 1.0,
           classification = 'SIG'
           )
ggH140_group = Group('ggH140',
           [ggH140_tautauhh],
           factor = 1.0,
           classification = 'SIG'
           )
ggH145_group = Group('ggH145',
           [ggH145_tautauhh],
           factor = 1.0,
           classification = 'SIG'
           )
ggH150_group = Group('ggH150',
           [ggH150_tautauhh],
           factor = 1.0,
           classification = 'SIG'
           )










# ggF = Group('ggF',
#             [ggH125_tautauhh],
#             factor = 1.0,
#             color = palette.slime,
#             style = 'fill',
#             legendLabel = 'WW',
#             stack = False,
#             classification = 'SIG',
#             )

           # ZJetsAFII = Group('ZJetsAFII',
#                   [ZeeNp0_AFII,
#                    ZmumuNp0_AFII,
#                    ZeeNp1_AFII,
#                    ZeeNp2_AFII,
#                    ZeeNp3_AFII,
#                    ZeeNp4_AFII,
#                    ZeeNp5incl_AFII,
#                    ZmumuNp1_AFII,
#                    ZmumuNp2_AFII,
#                    ZmumuNp3_AFII,
#                    ZmumuNp4_AFII,
#                    ZmumuNp5incl_AFII],
#                    factor = 1.0,
#                    color = palette.green,
#                    style = 'fill',
#                    legendLabel = 'ZJetsAFII',
#                    stack = True,
#                    classification = 'BG'
#                    )
                        
                   
# WJetsAFII = Group('WJetsAFII',
#                   [WenuNp0_AFII,
#                    WenuNp1_AFII,
#                    WenuNp2_AFII,
#                    WenuNp3_AFII,
#                    WenuNp4_AFII,
#                    WenuNp5incl_AFII,
#                    WmunuNp0_AFII,
#                    WmunuNp1_AFII,
#                    WmunuNp2_AFII,
#                    WmunuNp3_AFII,
#                    WmunuNp4_AFII,
#                    WmunuNp5incl_AFII,
#                    WtaunuNp0_AFII,
#                    WtaunuNp1_AFII,
#                    WtaunuNp2_AFII,
#                    WtaunuNp3_AFII,
#                    WtaunuNp4_AFII,
#                    WtaunuNp5incl_AFII],
#                    factor = 1.0,
#                    color = palette.blue,
#                    style = 'fill',
#                    legendLabel = 'WJetsAFII',
#                    stack = True,
#                    classification = 'BG'
#                    )
"""
WJets = Group('WJets',
[WenuNp0_Auto,
 WmunuNp0_Auto,
 WenuNp1_Auto,
 WenuNp2_Auto,
 WenuNp3_Auto,
 WenuNp4_Auto,
 WenuNp5incl_Auto,
 WmunuNp1_Auto,
 WmunuNp2_Auto,
 WmunuNp3_Auto,
 WmunuNp4_Auto,
 WmunuNp5incl_Auto,
#WtaunuNp0_Auto,
 # WtaunuNp1_Auto,
 # WtaunuNp2_Auto,
 # WtaunuNp3_Auto,
 # WtaunuNp4_Auto,
 # WtaunuNp5incl_Auto
 ],
 factor = 1.0,
 color = palette.green,
 style = 'fill',
 legendLabel = 'WJets',
 stack = True,
 classification = 'BG'
    )
"""
"""
ZJets = Group('ZJets',
              [ZeeNp0_Auto,
               ZmumuNp0_Auto,
               ZeeNp1_Auto,
               ZeeNp2_Auto,
               ZeeNp3_Auto,
               ZeeNp4_Auto,
               ZeeNp5incl_Auto,
               ZmumuNp1_Auto,
               ZmumuNp2_Auto,
               ZmumuNp3_Auto,
               ZmumuNp4_Auto,
               ZmumuNp5incl_Auto,
               ZeeNp0Excl_Mll10to60,
               ZeeNp1Excl_Mll10to60,
               ZeeNp2Excl_Mll10to60,
               ZeeNp3Excl_Mll10to60,
               ZeeNp4Excl_Mll10to60,
               ZeeNp5Incl_Mll10to60,
               ZmumuNp0Excl_Mll10to60,
               ZmumuNp1Excl_Mll10to60,
               ZmumuNp2Excl_Mll10to60,
               ZmumuNp3Excl_Mll10to60,
               ZmumuNp4Excl_Mll10to60,
               ZmumuNp5Incl_Mll10to60,
               ZtautauNp0Excl_Mll10to60,
               ZtautauNp0_Auto,
               ZtautauNp1_Auto,
               ZtautauNp2_Auto,
               ZtautauNp3_Auto,
               ZtautauNp4_Auto,
               ZtautauNp5incl_Auto,
               ZtautauNp1Excl_Mll10to60,
               ZtautauNp2Excl_Mll10to60,
               ZtautauNp3Excl_Mll10to60,
               ZtautauNp4Excl_Mll10to60,
               ZtautauNp5Incl_Mll10to60
               ],
# #factor = 0.80916,#factor when plotting is_WHlephad
factor = 1.0,
color = palette.blue,
style = 'fill',
legendLabel = 'ZJets',
stack = True,
classification = 'BG'
)
"""
        
