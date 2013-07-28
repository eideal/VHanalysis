1;2c#############################################
class PlottingInfo:
    """
    Constructor
    """
    def __init__(self,
                 product,
                 color,
                 style,
                 legendLabel,
                 stack):

        self.product = product
        self.color = color
        self.style = style
        self.legendLabel = legendLabel
        self.stack = stack
                 

#############################################
class Group:
    """
    Constructor
    """
    def __init__(self,
                 name = '',
                 samples = [],
                 product = 1,
                 color = palette.black,
                 style = 'line',
                 legendLabel = 'label',
                 stack = False,
                 classification = 'BG'
                 ):

        self.name = name
        self.product = product
        self.samples = samples
        self.plotting = PlottingInfo(color,
                                     style,
                                     legendLabel,
                                     stack)


