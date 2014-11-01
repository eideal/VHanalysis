from Supergroup import Supergroup
from Subsets import *
from Groups_UE import *
import palette


### Supergroups made to do the reweighting from D3PD to CN for sigal using Higgs pT - this is a first measurement of an UE uncertainty
#WH125_inclusive = Supergroup('WH125_inclusive',
#                          [WH125_group,
#                          WH125lh_group,
#                          WH125ll_group],
#                          factor = 1.0,
#                          color = palette.blue,
#                          style = 'line',
#                          legendLabel = 'WH_inclusive_CN',
#                          stack = True,
#                          subset = isreal)
#
#ZH125_inclusive = Supergroup('ZH125_inclusive',
#                          [ZH125_group,
#                          ZH125lh_group,
#                          ZH125ll_group],
#                          color = palette.blue,
#                          style = 'line',
#                          legendLabel = 'ZH_inclusive_CN',
#                          stack = True,
#                          subset = isreal)

WH125_inclusive = Supergroup('WH125_inclusive',
                            [WH125_group,
                            WH125lh_group,
                            ],
                            factor = 1.0,
                            color = palette.black,
                            style = 'line',
                            legendLabel = 'WH_incl_CN',
                            stack = True,
                            subset = isreal)

ZH125_inclusive = Supergroup('ZH125_inclusive',
                            [ZH125_group,
                            ZH125lh_group,
                            ],
                            factor = 1.0,
                            color = palette.black,
                            style = 'line',
                            legendLabel = 'ZH_incl_CN',
                            stack = True,
                            subset = isreal)

WH125hh = Supergroup('WH125_hh',
                      [WH125_group],
                      factor = 1.0,
                      color = palette.black,
                      style = 'line',
                      legendLabel = 'WH125hh_CN',
                      stack = True,
                      subset = isreal,
                      )
WH125lh = Supergroup('WH125_lh',
                      [WH125lh_group],
                      factor = 1.0,
                      color = palette.black,
                      style = 'line',
                      legendLabel = 'WH125lh_CN',
                      stack = True,
                      subset = isreal,
                      )

ZH125hh = Supergroup('ZH125_hh',
                      [ZH125_group],
                      factor = 1.0,
                      color = palette.black,
                      style = 'line',
                      legendLabel = 'ZH125hh_CN',
                      stack = True,
                      subset = isreal,
                      )
ZH125lh = Supergroup('ZH125_lh',
                      [ZH125lh_group],
                      factor = 1.0,
                      color = palette.black,
                      style = 'line',
                      legendLabel = 'ZH125lh_CN',
                      stack = True,
                      subset = isreal,
                      )
WH125_inclusive_Up = Supergroup('WH125_inclusive_Up',
                                [WH125_group_Up,
                                WH125lh_group_Up,
                                ],
                                factor = 1.0,
                                color = palette.blue,
                                style = 'line',
                                legendLabel = 'WH_incl_CN_Up',
                                stack = False,
                                subset = isreal)

ZH125_inclusive_Up = Supergroup('ZH125_inclusive_Up',
                                [ZH125_group_Up,
                                ZH125lh_group_Up,
                                ],
                                factor = 1.0,
                                color = palette.blue,
                                style = 'line',
                                legendLabel = 'ZH_incl_CN_Up',
                                stack = False,
                                subset = isreal)
WH125hh_Up = Supergroup('WH125hh_Up',
                        [WH125_group_Up],
                        factor = 1.0,
                        color = palette.blue,
                        style = 'line',
                        legendLabel = 'WHhh_CN_Up',
                        stack = False,
                        subset = isreal)
WH125lh_Up = Supergroup('WH125lh_Up',
                        [WH125lh_group_Up],
                        factor = 1.0,
                        color = palette.blue,
                        style = 'line',
                        legendLabel = 'WHlh_CN_Up',
                        stack = False,
                        subset = isreal)
ZH125hh_Up = Supergroup('ZH125hh_Up',
                        [ZH125_group_Up],
                        factor = 1.0,
                        color = palette.blue,
                        style = 'line',
                        legendLabel = 'ZHhh_CN_Up',
                        stack = False,
                        subset = isreal)
ZH125lh_Up = Supergroup('ZH125lh_Up',
                        [ZH125lh_group_Up],
                        factor = 1.0,
                        color = palette.blue,
                        style = 'line',
                        legendLabel = 'ZHlh_CN_Up',
                        stack = False,
                        subset = isreal)

WH125_inclusive_Down = Supergroup('WH125_inclusive_Down',
                                [WH125_group_Down,
                                WH125lh_group_Down,
                                ],
                                factor = 1.0,
                                color = palette.green,
                                style = 'line',
                                legendLabel = 'WH_incl_CN_Down',
                                stack = False,
                                subset = isreal)

ZH125_inclusive_Down = Supergroup('ZH125_inclusive_Down',
                                [ZH125_group_Down,
                                ZH125lh_group_Down,
                                ],
                                factor = 1.0,
                                color = palette.green,
                                style = 'line',
                                legendLabel = 'ZH_incl_CN_Down',
                                stack = False,
                                subset = isreal)

WH125hh_Down = Supergroup('WH125hh_Down',
                        [WH125_group_Down],
                        factor = 1.0,
                        color = palette.green,
                        style = 'line',
                        legendLabel = 'WHhh_CN_Down',
                        stack = False,
                        subset = isreal)
WH125lh_Down = Supergroup('WH125lh_Down',
                        [WH125lh_group_Down],
                        factor = 1.0,
                        color = palette.green,
                        style = 'line',
                        legendLabel = 'WHlh_CN_Down',
                        stack = False,
                        subset = isreal)
ZH125hh_Down = Supergroup('ZH125hh_Down',
                        [ZH125_group_Down],
                        factor = 1.0,
                        color = palette.green,
                        style = 'line',
                        legendLabel = 'ZHhh_CN_Down',
                        stack = False,
                        subset = isreal)
ZH125lh_Down = Supergroup('ZH125lh_Down',
                        [ZH125lh_group_Down],
                        factor = 1.0,
                        color = palette.green,
                        style = 'line',
                        legendLabel = 'ZHlh_CN_Down',
                        stack = False,
                        subset = isreal)



