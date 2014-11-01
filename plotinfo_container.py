import array
from ROOT import std
from Tools.Histogram import Histogram

"""
A class to keep track of plot information
"""
class Plotinfo:
    def __init__(self,
                 variable,
                 testing,#testing if I can append something to .png name
                 nbins,
                 binlow,
                 binhigh,
                 color, ##TEST
                 style, ##TEST
                 legendLabel,
                 axislabel,
                 factor,
                 logplot = False,
                 rootfile = False):
        self.variable = variable
        self.testing = testing
        self.nbins = nbins
        self.binlow = binlow
        self.binhigh = binhigh
        self.color = color ##TEST
        self.style = style ##TEST
        self.legendLabel = legendLabel
        self.axislabel = axislabel
        self.factor = factor
        self.logplot = logplot
        self.rootfile = rootfile

        ## Placeholder for histogram, because you want to keep the histogram along with the other
        ## plotinfo parameters
        self.histogram = Histogram(self.variable,
                                   self.testing,
                                   self.axislabel,
                                   self.nbins,
                                   self.binlow,
                                   self.binhigh,
                                   self.factor)


"""
A class to keep track of variable distributions and each's plot information
"""

class plotinfo_container(list):
                
    def Add(self, variable, testing, nbins, binlow, binhigh, color, style, legendLabel, axislabel, factor, logplot, rootfile ):
        self.append(Plotinfo(variable, testing, nbins, binlow, binhigh, color, style, legendLabel, axislabel, factor, logplot, rootfile))
    
                 
                 
