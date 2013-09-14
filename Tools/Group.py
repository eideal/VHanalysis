import palette

#############################################
class PlottingInfo:
    """
    Constructor
    """
    def __init__(self,
                 color,
                 style,
                 legendLabel,
                 stack):

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
                 factor = 1,
                 color = palette.black,
                 style = 'line',
                 legendLabel = 'label',
                 stack = False,
                 classification = 'BG'
                 ):

        self.name = name
        self.factor = factor
        self.samples = samples
        self.classification = classification
        self.plotting = PlottingInfo(color,
                                     style,
                                     legendLabel,
                                     stack)


