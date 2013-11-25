from Supergroup import Supergroup
from Groups import *
import palette

Data = Supergroup('Data',
                  [Data_group],
                  factor = 1.0,
                  color = palette.black,
                  style = 'points',
                  legendLabel = 'Data',
                  stack = False
                  )
QCD = Supergroup('QCD',
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
                  factor = 1.0,
                  color = palette.blue,
                  style = 'fill',
                  legendLabel = 'QCD',
                  stack = True
                  )
WeJets = Supergroup('WeJets',
                    [WeJets_group],
                    factor = 1.0,
                    color = palette.green,
                    style = 'fill',
                    legendLabel = 'WenuJets',
                    stack = True
                    )
WmJets = Supergroup('WmJets',
                    [WmJets_group],
                    factor = 1.0,
                    color = palette.brown,
                    style = 'fill',
                    legendLabel = 'WmunuJets',
                    stack = True
                    )
WtJets = Supergroup('WtJets',
                    [WtJets_group],
                    factor = 1.0,
                    color = palette.peach,
                    style = 'fill',
                    legendLabel = 'WtaunuJets',
                    stack = True
                    )
ZeeJets = Supergroup('ZeeJets',
                     [ZeeJets_group],
                     factor = 1.0,
                     color = palette.bandyellow,
                     style = 'fill',
                     legendLabel = 'ZeeJets',
                     stack = True
                     )
ZmmJets = Supergroup('ZmmJets',
                     [ZmmJets_group],
                     factor = 1.0,
                     color = palette.bandgreen,
                     style = 'fill',
                     legendLabel = 'ZmumuJets',
                     stack = True
                     )
ZttJets = Supergroup('ZttJets',
                     [ZttJets_group],
                     factor = 1.0,
                     color = palette.purple,
                     style = 'fill',
                     legendLabel = 'ZtautauJets',
                     stack = True
                     )
tt = Supergroup('tt',
                [tt_group],
                factor = 1.0,
                color = palette.pink,
                style = 'fill',
                legendLabel = 'ttbar',
                stack = True
                )
SingleTop = Supergroup('SingleTop',
                       [SingleTop_group],
                       factor = 1.0,
                       color = palette.red,
                       style = 'fill',
                       legendLabel = 'SingleTop',
                       stack = True
                       )
ZZ = Supergroup('ZZ',
                [ZZ_group],
                factor = 1.0,
                color = palette.orange,
                style = 'fill',
                legendLabel = 'ZZ',
                stack = True
                )
WW = Supergroup('WW',
                [WW_group],
                factor = 1.0,
                color = palette.indigo,
                style = 'fill',
                legendLabel = 'WW',
                stack = True
                )
WGamma = Supergroup('WGamma',
                    [WGamma_group],
                    factor = 1.0,
                    color = palette.grey,
                    style = 'fill',
                    legendLabel = 'WGamma',
                    stack = True
                    )
WZ = Supergroup('WZ',
                [WZ_group],
                factor = 1.0,
                color = palette.teal,
                style = 'fill',
                legendLabel = 'WZ',
                stack = True
                )

##### SIGNAL ########### SIGNAL ############# SIGNAL ######
WH = Supergroup('WH',
                [WH_group],
                factor = 10.0,
                color = palette.black,
                style = 'line',
                legendLabel = 'WH(x10)',
                stack = False
                )
ZH = Supergroup('ZH',
                [ZH_group],
                factor = 10.0,
                color = palette.black,
                style = 'line',
                legendLabel = 'ZH(x10)',
                stack = False
                )
