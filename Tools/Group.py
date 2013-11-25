import palette

#############################################
class Group:
    """
    Constructor
    """
    def __init__(self,
                 name = '',
                 samples = [],
                 factor = 1,
                 classification = 'BG'
                 ):

        self.name = name
        self.factor = factor
        self.samples = samples
        self.classification = classification
      


