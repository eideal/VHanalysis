from Group import Group
from Samples import *
from Subsets import *
import palette

Data_group = Group('Data',
             [Egamma,
#JetTauEtmiss,
              Muons],
              factor = 1.0,
              classification = 'DATA'
              ) 

Data_group_AntiTau = Group('Data_group_AntiTau',
                           [Egamma,
#JetTauEtmiss,
                            Muons],
                            factor = 1.0,
                            classification = 'DATA',
#                           subset = antitau, #THIS SEEMS TO BE THE SAME CUT AS the yesantitau
#subset = yesantitau
                            subset = antitau

                            )

MCcorr_fakes_group = Group('MCcorr_fakes_group',
                      [Powheg_ZZ_2e2mu_mll4_2pt5,
                       Powheg_ZZ_2e2tau_mll4_2pt5,
                       Powheg_ZZ_2mu2tau_mll4_2pt5,
                       Powheg_ZZ_4e_mll4_2pt5,
                       Powheg_ZZ_4mu_mll4_2pt5,
                       Powheg_ZZ_4tau_mll4_2pt5,
                       Powheg_ZZllnunu_ee_mll4,
                       Powheg_ZZllnunu_mm_mll4,
                       Powheg_ZZllnunu_tt_mll4,
                       Powheg_WZ_W11Z11_mll0p250d0_2LeptonFilter5,
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
                       gg2WW0240_WpWmtaunutaunu,
                       ttbar_dilepton,
                       ttbar_allhad,
                       SingleTopSChanWenu,
                       SingleTopSChanWmunu,
                       SingleTopSChanWtaunu,
                       SingleTopWtChanIncl,
                       singletop_tchan_e,
                       singletop_tchan_mu,
                       singletop_tchan_tau,
                       WgammaNp0,
                       WgammaNp1,
                       WgammaNp2,
                       WgammaNp3,
                       WgammaNp4,
                       WgammaNp5,
                       MadGraph_lnuee_lt7,
                       MadGraph_lnumumu_lt7,
                       MadGraph_lnutautau_lt7,
                       WWWStar_lnulnulnu,
                       ZWWStar_lllnulnu,
                       ZZZStar_nunullll,
                       WenuNp0_Auto,
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
                       WtaunuNp0_Auto,
                       WtaunuNp1_Auto,
                       WtaunuNp2_Auto,
                       WtaunuNp3_Auto,
                       WtaunuNp4_Auto,
                       WtaunuNp5incl_Auto,
                       ZeeNp0_Auto,
                       ZmumuNp0_Auto,
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
                       ZtautauNp0_Auto,
                       ZtautauNp1_Auto,
                       ZtautauNp2_Auto,
                       ZtautauNp3_Auto,
                       ZtautauNp4_Auto,
                       ZtautauNp5incl_Auto,
                       ZtautauNp0Excl_Mll10to60,
                       ZtautauNp1Excl_Mll10to60, 
                       ZtautauNp2Excl_Mll10to60,
                       ZtautauNp3Excl_Mll10to60,
                       ZtautauNp4Excl_Mll10to60,
                       ZtautauNp5Incl_Mll10to60,
                       VBFH125_WW2lep_EF_15_5,
                       VBFH125_ZZ4lep,
                       WH125_WW2lep,
                       WH125_ZZ4lep,
                       ZH125_WW2lep,
                       ZH125_ZZ4lep,
                       ggH125_WW2lep_EF_15_5,
                       ggH125_ZZ4lep,
                       ],
                       factor = -1.0 * 0.0203, #times the lumi
                       classification = 'BG',
                       subset = MCcorr,
                       )

MCcorr_fakesttbar_group = Group('MCcorr_fakesttbar_group',
                                [ttbar],
                                factor = -1.0 * 0.0203,
                                classification = 'BG',
                                subset = dilep + MCcorr,
                                )

MCcorr_fakes_group_WHhh = Group('MCcorr_fakes_group_WHhh',
                      [ZZ,
                       WZ,
                       WpWmenuenu,
                       WpWmenumunu,
                       WpWmenutaunu,
                       WpWmmunuenu,
                       WpWmmunumunu,
                       WpWmmunutaunu,
                       WpWmtaunuenu,
                       WpWmtaunumunu,
                       WpWmtaunutaunu,
                       WWqqlnuNp0,
                       WWqqlnuNp1,
                       WWqqlnuNp2,
                       WWqqlnuNp3,
                       ttbar_dilepton,
                       ttbar_allhad,
                       SingleTopSChanWenu,
                       SingleTopSChanWmunu,
                       SingleTopSChanWtaunu,
                       SingleTopWtChanIncl,
                       singletop_tchan_e,
                       singletop_tchan_mu,
                       singletop_tchan_tau,
                       WgammaNp0,
                       WgammaNp1,
                       WgammaNp2,
                       WgammaNp3,
                       WgammaNp4,
                       WgammaNp5,
                       MadGraph_lnuee_lt7,
                       MadGraph_lnumumu_lt7,
                       MadGraph_lnutautau_lt7,
                       WWWStar_lnulnulnu,
                       ZWWStar_lllnulnu,
                       ZZZStar_nunullll,
                       WenuNp0_Auto,
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
                       WtaunuNp0_Auto,
                       WtaunuNp1_Auto,
                       WtaunuNp2_Auto,
                       WtaunuNp3_Auto,
                       WtaunuNp4_Auto,
                       WtaunuNp5incl_Auto,
                       ZeeNp0_Auto,
                       ZmumuNp0_Auto,
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
                       ZtautauNp0_Auto,
                       ZtautauNp1_Auto,
                       ZtautauNp2_Auto,
                       ZtautauNp3_Auto,
                       ZtautauNp4_Auto,
                       ZtautauNp5incl_Auto,
                       ZtautauNp0Excl_Mll10to60,
                       ZtautauNp1Excl_Mll10to60, 
                       ZtautauNp2Excl_Mll10to60,
                       ZtautauNp3Excl_Mll10to60,
                       ZtautauNp4Excl_Mll10to60,
                       ZtautauNp5Incl_Mll10to60,
                       VBFH125_WW2lep_EF_15_5,
                       VBFH125_ZZ4lep,
                       WH125_WW2lep,
                       WH125_ZZ4lep,
                       ZH125_WW2lep,
                       ZH125_ZZ4lep,
                       ggH125_WW2lep_EF_15_5,
                       ggH125_ZZ4lep,
                       ],
                       factor = -1.0 * 0.0203, #times the lumi
                       classification = 'BG',
                       subset = MCcorr,
                       )

HiggsNotVHtt_group = Group('HiggsNotVHtt',
                      [VBFH125_WW2lep_EF_15_5,
                      VBFH125_ZZ4lep,
                      WH125_WW2lep,
                      WH125_ZZ4lep,
                      ZH125_WW2lep,
                      ZH125_ZZ4lep,
                      ggH125_WW2lep_EF_15_5,
                      ggH125_ZZ4lep],
                      factor = 1.0,
                      classification = 'BG',
                                              )

HiggsNotVHtt1_group = Group('HiggsNotVHtt1_group',
                      [VBFH125_WW2lep_EF_15_5],
                      factor = 1.0,
                      classification = 'BG')

HiggsNotVHtt2_group = Group('HiggsNotVHtt2_group',
                      [VBFH125_ZZ4lep],
                      factor = 1.0,
                      classification = 'BG')

HiggsNotVHtt3_group = Group('HiggsNotVHtt3_group',
                      [WH125_WW2lep],
                      factor = 1.0,
                      classification = 'BG')

HiggsNotVHtt4_group = Group('HiggsNotVHtt4_group',
                      [WH125_ZZ4lep],
                      factor = 1.0,
                      classification = 'BG')
HiggsNotVHtt5_group = Group('HiggsNotVHtt5_group',
                      [ZH125_WW2lep],
                      factor = 1.0,
                      classification = 'BG')
HiggsNotVHtt6_group = Group('HiggsNotVHtt6_group',
                      [ZH125_ZZ4lep],
                      factor = 1.0,
                      classification = 'BG')
HiggsNotVHtt7_group = Group('HiggsNotVHtt7_group',
                      [ggH125_WW2lep_EF_15_5],
                      factor = 1.0,
                      classification = 'BG')
HiggsNotVHtt8_group = Group('HiggsNotVHtt8_group',
                      [ggH125_ZZ4lep],
                      factor = 1.0,
                      classification = 'BG')


                  
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
#ZZ,
                  factor = 1.0,
                  classification = 'BG',
                  )

ZZ_4e_group =  Group('ZZ_4e_group',
                 [
                  Powheg_ZZ_4e_mll4_2pt5,
                                   ],
                  factor = 1.0,
                  classification = 'BG',
                  )
ZZ_4m_group = Group('ZZ_4m_group',
                 [
                  Powheg_ZZ_4mu_mll4_2pt5,
                                   ],
                  factor = 1.0,
                  classification = 'BG',
                  )
ZZ_4t_group = Group('ZZ_4t_group',
                 [
                  Powheg_ZZ_4tau_mll4_2pt5,
                                   ],
                  factor = 1.0,
                  classification = 'BG',
                  )
ZZ_2e2m_group = Group('ZZ_2e2m_group',
                 [
                  Powheg_ZZ_2e2mu_mll4_2pt5,
                                   ],
                  factor = 1.0,
                  classification = 'BG',
                  )
ZZ_2e2t_group = Group('ZZ_2e2t_group',
                 [
                  Powheg_ZZ_2e2tau_mll4_2pt5,
                                   ],
                  factor = 1.0,
                  classification = 'BG',
                  )
ZZ_2m2t_group = Group('ZZ_2m2t_group',
                 [
                  Powheg_ZZ_2mu2tau_mll4_2pt5,
                                   ],
                  factor = 1.0,
                  classification = 'BG',
                  )
ZZllnunu_ee_group = Group('ZZllnunu_ee_group',
                 [
                  Powheg_ZZllnunu_ee_mll4,
                                   ],
                  factor = 1.0,
                  classification = 'BG',
                  )
ZZllnunu_mm_group = Group('ZZllnunu_mm_group',
                 [
                  Powheg_ZZllnunu_mm_mll4,
                                   ],
                  factor = 1.0,
                  classification = 'BG',
                  )
ZZllnunu_tt_group = Group('ZZllnunu_tt_group',
                 [
                  Powheg_ZZllnunu_tt_mll4,
                                   ],
                  factor = 1.0,
                  classification = 'BG',
                  )

WHhh_ZZ_group = Group('ZZ_WHhh',
                      [ZZ],
                      factor = 1.0,
                      classification = 'BG')

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
#WZ,
                  factor = 1.0,
                  classification = 'BG',
                  )

WHhh_WZ_group = Group('WZ_WHhh',
                      [WZ],
                      factor = 1.0,
                      classification = 'BG')


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

WHhh_WW_group = Group('WW_WHhh',
                        [WpWmenuenu,
                        WpWmenumunu,
                        WpWmenutaunu,
                        WpWmmunuenu,
                        WpWmmunumunu,
                        WpWmmunutaunu,
                        WpWmtaunuenu,
                        WpWmtaunumunu,
                        WpWmtaunutaunu,
                        WWqqlnuNp0,
                        WWqqlnuNp1,
                        WWqqlnuNp2,
                        WWqqlnuNp3,
                        ],
                        factor = 1.0,
                        classification = 'BG')

tt_group = Group('tt',
                 [ttbar,
                  ttbar_allhad,
                  ttbar_dilepton],
                  factor = 1.0,
                  classification = 'BG',
                  )
ttbar_dilepton_group = Group('tt_dilep',
                             [ttbar_dilepton],
                             factor = 1.0,
                             classification = 'BG',
                             )
ttbar_lepfil_group = Group('tt_lepfil',
                           [ttbar],
                           factor = 1.0,
                           classification = 'BG',
                           subset = dilep
                           )
ttbar_lepfil_group_old = Group('tt_lepfil_old',
                               [ttbar],
                               factor = 1.0,
                               classification = 'BG',
                               )
ttbar_allhad_group = Group('tt_allhad',
                           [ttbar_allhad],
                           factor = 1.0,
                           classification = 'BG'
                           )
                    

Triboson_group = Group('Triboson',
                       [WWWStar_lnulnulnu,
                        ZWWStar_lllnulnu,
                        ZZZStar_nunullll],
                        factor = 1.0,
                        classification = 'BG',
                        )

ZeeJets_group = Group('ZeeJets',
                      [ZeeNp0Excl_Mll10to60,
                        ZeeNp1Excl_Mll10to60,
ZeeNp2Excl_Mll10to60,
ZeeNp3Excl_Mll10to60,
ZeeNp4Excl_Mll10to60,
ZeeNp5Incl_Mll10to60,
ZeeNp0_Auto,
                       ZeeNp1_Auto,
                       ZeeNp2_Auto,
                       ZeeNp3_Auto,
                       ZeeNp4_Auto,
                       ZeeNp5incl_Auto,
                       ],
                       factor = 1.0,
                       classification = 'BG',
                       )

ZmmJets_group = Group('ZmmJets',
                      [ZmumuNp0Excl_Mll10to60,
ZmumuNp1Excl_Mll10to60,
ZmumuNp2Excl_Mll10to60,
ZmumuNp3Excl_Mll10to60,
ZmumuNp4Excl_Mll10to60,
ZmumuNp5Incl_Mll10to60,
ZmumuNp0_Auto,
                       ZmumuNp1_Auto,
                       ZmumuNp2_Auto,
                       ZmumuNp3_Auto,
                       ZmumuNp4_Auto,
                       ZmumuNp5incl_Auto,
                       ],
factor = 1.0,
classification = 'BG',
)
#                Filtered_ZmumuNp0Excl_Mll10to6,
#               Filtered_ZmumuNp1Excl_Mll10to6,
#                Filtered_ZmumuNp2Excl_Mll10to6,
#                Filtered_ZmumuNp3Excl_Mll10to6,
#                Filtered_ZmumuNp4Excl_Mll10to6,
#ABOVE IS TO BE USED

ZttJets_group = Group('ZttJets',
[ZtautauNp0Excl_Mll10to60,
ZtautauNp1Excl_Mll10to60,
ZtautauNp2Excl_Mll10to60,
ZtautauNp3Excl_Mll10to60,
ZtautauNp4Excl_Mll10to60,
ZtautauNp5Incl_Mll10to60,

#BELOW IS TO BE USED
#Filtered_ZtautauNp0Excl_Mll10to60,
#Filtered_ZtautauNp1Excl_Mll10to60,
#Filtered_ZtautauNp2Excl_Mll10to60,
#Filtered_ZtautauNp3Excl_Mll10to60,
ZtautauNp0_Auto,
ZtautauNp1_Auto,
ZtautauNp2_Auto,
ZtautauNp3_Auto,
ZtautauNp4_Auto,
ZtautauNp5incl_Auto,
],
factor = 1.0,
classification = 'BG',
    )

WJets_group = Group('WJets',
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
 WtaunuNp0_Auto,
 WtaunuNp1_Auto,
 WtaunuNp2_Auto,
 WtaunuNp3_Auto,
 WtaunuNp4_Auto,
 WtaunuNp5incl_Auto
 ],
 factor = 1.0,
 classification = 'BG',
 )
       


###### SIGNAL ####### SIGNAL ######## SIGNAL

OtherHiggs = Group('OtherHiggs',
                    [],
                    factor = 1.0,
                    classification = 'BG'
)

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
WH120_group = Group('WH120',
                    [WH120_tautauhh],
                    factor = 1.0,
                    classification = 'SIG'
                    )
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
######
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
### Studies of Higgs pT dependence
ZH125lh_group = Group('ZH125lh',
                      [ZH125_tautaulh],
                      factor = 1.0,
                      classification = 'SIG'
                      )
ZH125ll_group = Group('ZH125ll',
                      [ZH125_tautaull],
                      factor = 1.0,
                      classification = 'SIG')
WH125lh_group = Group('WH125lh',
                      [WH125_tautaulh],
                      factor = 1.0,
                      classification = 'SIG'
                      )
WH125ll_group = Group('WH125ll',
                      [WH125_tautaull],
                      factor = 1.0,
                      classification = 'SIG')
#######

### Studies of EWK correction reweighting
ZHhh_WithEWK = Group('ZHhh_WithEWK',
                     [WithEWK],
                     factor = 1.0,
                     classification = 'SIG'
                     )
ZHhh_NoEWK = Group('ZHhh_NoEWK',
                   [NoEWK],
                   factor = 1.0,
                   classification = 'SIG'
                   )

######

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
#####
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
#####
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




####EXTRAS EXTRAS EXTRAS EXTRAS EXTRAS EXTRAS EXTRAS EXTRAS
########################################################
# Data_group_1AntiTau_1 = Group('Data_1AntiTau', 
#                             [Egamma,
#                              JetTauEtmiss,
#                              Muons],
#                              factor = 1.0,
#                              classification = 'DATA',
#                              subset = antitau2,
#                              )
# Data_group_1AntiTau_2 = Group('Data_1AntiTau_2',
#                               [Egamma,
#                                JetTauEtmiss,
#                                Muons],
#                                factor = 1.0,
#                                classification = 'DATA',
#                                subset = antitau3,
#                                )
# Data_group_2AntiTaus = Group('Data_2AntiTaus', 
#                              [Egamma,
#                               JetTauEtmiss,
#                               Muons],
#                               factor = 1.0,
#                               classification = 'DATA',
#                               subset = antitau,
#                               )




DataSSS_group = Group('DataSSS',
                 [Egamma,
                  JetTauEtmiss,
                  Muons],
                  factor = 1.0,
                  classification = 'DATA',
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
                         factor = -1.0 * 0.0203,
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
                 factor = -1.0 * 0.0203,
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
                    factor = -1.0 * 0.0203,
                    classification = 'BG'
                    )

#                Filtered_ZeeNp0Excl_Mll10to60,
#                Filtered_ZeeNp1Excl_Mll10to60,
#                Filtered_ZeeNp2Excl_Mll10to60,
#                Filtered_ZeeNp3Excl_Mll10to60,
#                Filtered_ZeeNp4Excl_Mll10to60,
#ABOVE IS TO BE USED
                 
#ZeeNp0Excl_Mll10to60,
#                ZeeNp1Excl_Mll10to60,
#                ZeeNp2Excl_Mll10to60,
#                ZeeNp3Excl_Mll10to60,
#                ZeeNp4Excl_Mll10to60,
#                ZeeNp5Incl_Mll10to60,
#],
#                factor = 1.0,
#                classification = 'BG'
#                )
SSSZeeJets_group = Group('SSSZeeJets',
                    [ZeeNp0_Auto,
                     ZeeNp1_Auto,
                     ZeeNp2_Auto,
                     ZeeNp3_Auto,
                     ZeeNp4_Auto,
                     ZeeNp5incl_Auto,
#                     ZeeNp0Excl_Mll10to60,
#                    ZeeNp1Excl_Mll10to60,
#                    ZeeNp2Excl_Mll10to60,
#                    ZeeNp3Excl_Mll10to60,
#                    ZeeNp4Excl_Mll10to60,
#                    ZeeNp5Incl_Mll10to60,
                     ],
                     factor = -1.0 * 0.0203,
                     classification = 'BG'
                     )


#ZmumuNp0Excl_Mll10to60,
#                ZmumuNp1Excl_Mll10to60,
#                ZmumuNp2Excl_Mll10to60,
#                ZmumuNp3Excl_Mll10to60,
#                ZmumuNp4Excl_Mll10to60,
#                ZmumuNp5Incl_Mll10to60,
#                 ],
#                 factor = 1.0,
#                classification = 'BG'
#                )
SSSZmmJets_group = Group('SSSZmmJets',
                 [ZmumuNp0_Auto,
                  ZmumuNp1_Auto,
                  ZmumuNp2_Auto,
                  ZmumuNp3_Auto,
                  ZmumuNp4_Auto,
                  ZmumuNp5incl_Auto,
 #                ZmumuNp0Excl_Mll10to60,
 #                ZmumuNp1Excl_Mll10to60,
 #                ZmumuNp2Excl_Mll10to60,
 #                ZmumuNp3Excl_Mll10to60,
 #                ZmumuNp4Excl_Mll10to60,
 #                ZmumuNp5Incl_Mll10to60,
                  ],
                  factor = -1.0 * 0.0203,
                  classification = 'BG'
                  )

SSSZttJets_group = Group('SSSZttJets',
                         [
 #               [ZtautauNp0Excl_Mll10to60,
 #                ZtautauNp1Excl_Mll10to60,
 #                ZtautauNp2Excl_Mll10to60,
#                  ZtautauNp3Excl_Mll10to60,
#                  ZtautauNp4Excl_Mll10to60,
#                  ZtautauNp5Incl_Mll10to60,
ZtautauNp0_Auto,
ZtautauNp1_Auto,
ZtautauNp2_Auto,
ZtautauNp3_Auto,
ZtautauNp4_Auto,
ZtautauNp5incl_Auto,
],
factor = -1.0 * 0.0203,
classification = 'BG'
    )

SSStt_group = Group('SSStt',
                    [ttbar,
                     ttbar_allhad,
                     ttbar_dilepton],
                     factor = -1.0 * 0.0203,
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
                   factor = -1.0 * 0.0203,
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
            factor = -1.0 * 0.0203,
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
            factor = -1.0 * 0.0203,
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
                factor = -1.0 * 0.0203,
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
            factor = -1.0 * 0.0203,
            classification = 'BG',
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
        
