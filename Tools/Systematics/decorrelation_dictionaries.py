###########################################################
class DecorrelatorCollection(dict):
    """
    A class to decorrelate certain systematics
    """
        

    ## ----------------------------------------------------- ##
    def add(self, input_name, output_name):
        """
        Add a decorrelator
        """

        self[input_name] = output_name


    ## ----------------------------------------------------- ##
    def get(self, sys_name):
        """
        Obtain the 
        """

        if not sys_name in self.keys():
            return sys_name

        else:
            return self[sys_name]


"""
===========================================================
Define correlators
===========================================================
"""

decorrelations = DecorrelatorCollection()

## FF decorrelations
#decorrelations.add('ATLAS_ANA_LH12_Fake_boost', 'ATLAS_ANA_LH12_SR_FF') #First element is the new name, second element is the name in the CN
