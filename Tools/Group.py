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
                 subset = Subset.Subset(''),
        #weight = '1',
                 ):

        self.name = name
        self.factor = factor
        self.samples = samples
        self.classification = classification
        self.subset = subset
        #self.weight = weight
      


