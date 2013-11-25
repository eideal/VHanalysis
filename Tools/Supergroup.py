import palette

#############################################
class Supergroup:
    """
    Constructor
    """
    def __init__(self,
                 name = '',
                 groups = [],
                 factor = 1,
                 color = palette.black,
                 style = 'line',
                 legendLabel = 'label',
                 stack = False,
                 ):

        self.name = name
        self.factor = factor
        self.groups = groups
        self.color = color
        self.style = style
        self.legendLabel = legendLabel
        self.stack = stack
