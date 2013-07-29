from Group import Group
from Samples import *
import palette

WJets = Group('WJets',
              [P2011C_WenuNp0,
               P2011C_WenuNp1,
               P2011C_WenuNp2,
               P2011C_WenuNp3,
               P2011C_WenuNp4,
               P2011C_WenuNp5incl,
               P2011C_WmunuNp0,
               P2011C_WmunuNp1,
               P2011C_WmunuNp2,
               P2011C_WmunuNp3,
               P2011C_WmunuNp4,
               P2011C_WmunuNp5incl,
               P2011C_WtaunuNp0,
               P2011C_WtaunuNp1,
               P2011C_WtaunuNp2,
               P2011C_WtaunuNp3,
               P2011C_WtaunuNp4,
               P2011C_WtaunuNp5incl],
              factor = 1.0,
              color = palette.orange,
              style = 'fill',
              legendLabel =  'W+Jets',
              stack = True,
              classification = 'BG'
              )

WW = Group('WW',
           [gg2WW0240_WpWmenuenu,
            gg2WW0240_WpWmenumunu,
            gg2WW0240_WpWmenutaunu,
            gg2WW0240_WpWmmunuenu,
            gg2WW0240_WpWmmunumunu,
            gg2WW0240_WpWmmunutaunu,
            gg2WW0240_WpWmtaunuenu,
            gg2WW0240_WpWmtaunumunu,
            gg2WW0240_WpWmtaunutaunu,
            Powheg_WpWm_ee,
            Powheg_WpWm_em,
            Powheg_WpWm_et,
            Powheg_WpWm_me,
            Powheg_WpWm_mm,
            Powheg_WpWm_mt,
            Powheg_WpWm_te,
            Powheg_WpWm_tm,
            Powheg_WpWm_tt],
           factor = 1.0,
           color = palette.pink,
           style = 'fill',
           legendLabel = 'WW',
           stack = True,
           classification = 'BG'
           )

WZ = Group('WZ',
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
            Powheg_WZ_Wm15Z15_mll3p804d0_2LeptonFilter5],
           factor = 1.0,
           color = palette.skyblue,
           style = 'fill',
           legendLabel = 'WZ',
           stack = True,
           classification = 'BG'
           )

ZJets = Group('ZJets',
              [ZeeNp0Excl_Mll10to60,
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
               ZtautauNp1Excl_Mll10to60,
               ZtautauNp2Excl_Mll10to60,
               ZtautauNp3Excl_Mll10to60,
               ZtautauNp4Excl_Mll10to60,
               ZtautauNp5Incl_Mll10to60],
              factor = 1.0,
              color = palette.green,
              style = 'fill',
              legendLabel = 'Z+Jets',
              stack = True,
              classification = 'BG'
              )

ZZ = Group('ZZ',
           [Powheg_ZZ_2e2mu_mll4_2pt5,
            Powheg_ZZ_2e2tau_mll4_2pt5,
            Powheg_ZZ_2mu2tau_mll4_2pt5,
            Powheg_ZZ_2mu2tau_mll4_2pt5,
            Powheg_ZZ_4e_mll4_2pt5,
            Powheg_ZZ_4mu_mll4_2pt5,
            Powheg_ZZ_4tau_mll4_2pt5,
            Powheg_ZZllnunu_ee_mll4,
            Powheg_ZZllnunu_mm_mll4,
            Powheg_ZZllnunu_tt_mll4],
           factor = 1.0,
           color = palette.purple,
           style = 'fill',
           legendLabel = 'ZZ',
           stack = True,
           classification = 'BG'
           )

SingleTop = Group('SingleTop',
            [SingleTopSChanWenu,
             SingleTopSChanWmunu,
             SingleTopSChanWtaunu,
             SingleTopWtChanIncl,
             singletop_tchan_e,
             singletop_tchan_mu,
             singletop_tchan_tau],
            factor = 1.0,
            color = palette.grey,
            style = 'fill',
            legendLabel = 'SingleTop',
            stack = True,
            classification = 'BG'
            )


ttbar_allh = Group('ttbar_allh',
                     [ttbar_allhad],
                     factor = 1.0,
                     color = palette.peach,
                     style = 'fill',
                     legendLabel = 'ttbar_allhad',
                     stack = True,
                     classification = 'BG'
                     )

ttbar_dilep = Group('ttbar_dilep',
                    [ttbar_dilepton],
                    factor = 1.0,
                    color = palette.slime,
                    style = 'fill',
                    legendLabel = 'ttbar_dilep',
                    stack = True,
                    classification = 'BG'
                    )

ttbar_lepfil = Group('ttbar_lepfil',
                     [ttbar],
                     factor = 1.0,
                     color = palette.indigo,
                     style = 'fill',
                     legendLabel = 'ttbar_lepfil',
                     stack = True,
                     classification = 'BG'
                     )

Top = Group('Top',
            [ttbar,
             SingleTopSChanWenu,
             SingleTopSChanWmunu,
             SingleTopSChanWtaunu,
             SingleTopWtChanIncl,
             singletop_tchan_e,
             singletop_tchan_mu,
             singletop_tchan_tau,
             ttbar_allhad
             ],
            factor = 1.0,
            color = palette.brown,
            style = 'fill',
            legendLabel = 'Top',
            stack = True,
            classification = 'BG'
            )

WH = Group('WH',
           [test_WH125_VHtautau_hh_ntuple],
           factor = 1.0,
           color = palette.red,
           style = 'line',
           legendLabel = 'WH',
           stack = False,
           classification = 'SIG'
           )

#ZH = Group('ZH',
 #          [ZH125],
  #         factor = 1.0,
   #        color = palette.red,
    #       style = 'line',
     #      legendLabel = 'ZH',
      #     stack = False,
       #    classification = 'SIG'
        #   )
             
             
