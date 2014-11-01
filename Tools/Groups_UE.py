from Group import Group
from Samples_UE import *
from Subsets import *
import palette


WH125_group = Group('WH125',
                    [WH125_tautauhh],
                    factor = 1.0,
                    classification = 'SIG'
                    )

ZH125_group = Group('ZH125',
                    [ZH125_tautauhh],
                    factor = 1.0,
                    classification = 'SIG'
                    )

ZH125lh_group = Group('ZH125lh',
                      [ZH125_tautaulh],
                      factor = 1.0,
                      classification = 'SIG'
                      )
WH125lh_group = Group('WH125lh',
                      [WH125_tautaulh],
                      factor = 1.0,
                      classification = 'SIG'
                      )
#WH125ll_group = Group('WH125ll',
#                      [WH125_tautaull],
#                      factor = 1.0,
#                      classification = 'SIG')
#ZH125ll_group = Group('ZH125ll',
#                      [ZH125_tautaull],
#                      factor = 1.0,
#                      classification = 'SIG')

############# These are groups with the D3PD to CN reweighting systematic variation branches:
WH125_group_Up = Group('WH125_group_Up',
                    [WH125_tautauhh_Up],
                    factor = 1.0,
                    classification = 'SIG'
                    )

ZH125_group_Up = Group('ZH125_group_Up',
                    [ZH125_tautauhh_Up],
                    factor = 1.0,
                    classification = 'SIG'
                    )

ZH125lh_group_Up = Group('ZH125lh_group_Up',
                      [ZH125_tautaulh_Up],
                      factor = 1.0,
                      classification = 'SIG'
                      )
WH125lh_group_Up = Group('WH125lh_group_Up',
                      [WH125_tautaulh_Up],
                      factor = 1.0,
                      classification = 'SIG'
                      )

WH125_group_Down = Group('WH125_group_Down',
                    [WH125_tautauhh_Down],
                    factor = 1.0,
                    classification = 'SIG'
                    )

ZH125_group_Down = Group('ZH125_group_Down',
                    [ZH125_tautauhh_Down],
                    factor = 1.0,
                    classification = 'SIG'
                    )

ZH125lh_group_Down = Group('ZH125lh_group_Down',
                      [ZH125_tautaulh_Down],
                      factor = 1.0,
                      classification = 'SIG'
                      )
WH125lh_group_Down = Group('WH125lh_group_Down',
                      [WH125_tautaulh_Down],
                      factor = 1.0,
                      classification = 'SIG'
                      )

