import palette, Subset

#############################################
class Group:
    """
    Constructor
    """
    def __init__(self,
                 name = '',
                 samples = [],
                 factor = 1,
                 classification = 'BG',
                 subset = Subset.Subset('')
                 ):

        self.name = name
        self.factor = factor
        self.samples = samples
        self.classification = classification
        self.subset = subset
      


