##################################################
## Helper classes and functions

class Style:

    ## -------------------------------------------- ##
    def __init__(self, name):
        """
        Constructor
        """

        self.name         = name
        self.fill_style   = 1001
        self.line_style   = 1
        self.line_width   = 1
        self.marker_style = 20
        self.marker_size  = 1.0
        self.draw_options = 'HIST'


    ## -------------------------------------------- ##
    def apply(self, h):
        """
        Apply the style to a histogram
        """

        h.SetLineStyle(self.line_style)
        h.SetLineWidth(self.line_width)
        h.SetMarkerStyle(self.marker_style)
        h.SetMarkerSize(self.marker_size)
        h.SetFillStyle(self.fill_style)


def default_label_offset(x,y):
    return x,y

def default_label_size(s):
    return s

class Positioning:
    
    ## -------------------------------------------- ##
    def __init__(self):
        """
        Constructor
        """

        self.y_label_size = None
        self.y_title_size = None
        self.y_title_offset = None
        
        self.x_label_size = None
        self.x_title_size = None
        self.x_title_offset = None

        self.plot_label_offset = default_label_offset
        self.plot_label_size = default_label_size

        self.legend_spacing = None
        self.legend_xmax   = None
        self.legend_ymax   = None


##################################################
## Define 1D histogram style dictionary
style1D = {}

name = 'dashLeft'
s = Style(name)
s.fill_style   = 3004
s.line_width   = 2
s.marker_style = 0
s.marker_size  = 0
style1D[name]  = s

name = 'dashRight'
s = Style(name)
s.fill_style   = 3005
s.line_width   = 2
s.marker_style = 0
s.marker_size  = 0
style1D[name]  = s

name = 'fill'
s = Style(name)
s.fill_style   = 1001
s.line_width   = 0
s.line_style   = 0
s.marker_style = 0
s.marker_size  = 0
style1D[name]  = s

name = 'line'
s = Style(name)
s.fill_style   = 0
s.line_style   = 1
s.line_width   = 2
s.marker_style = 0
s.marker_size  = 0
style1D[name]  = s

name = 'points'
s = Style(name)
s.fill_style   = 0
s.line_width   = 0
s.line_style   = 0
s.draw_options = 'P0E'
style1D[name]  = s

name = 'error'
s = Style(name)
s.fill_style   = 3154
s.line_style   = 0
s.line_width   = 0
s.marker_style = 0
s.marker_size  = 0
s.draw_options = 'E2'
style1D[name]  = s


##################################################
## Define ratio and normal positionings

## Positioning of elements for ratio plots
ratio_positioning = Positioning()

ratio_positioning.y_label_size = 0.06
ratio_positioning.y_title_size = 0.07
ratio_positioning.y_title_offset = 1.5

ratio_positioning.x_label_size = 0.06
ratio_positioning.x_title_size = 0.03
ratio_positioning.x_title_offset = 0.6

ratio_positioning.legend_spacing = 0.03
ratio_positioning.legend_xmax    = 0.87
ratio_positioning.legend_ymax    = 0.79


def normal_label_offset(x,y):
    return 1.015*x, 0.95*y#(y + (y-0.96))

def normal_label_size(s):
    return 1.4*s

normal_positioning = Positioning()

normal_positioning.y_label_size = 0.06
normal_positioning.y_title_size = 0.07
normal_positioning.y_title_offset = 1.4

normal_positioning.x_label_size = 0.06
normal_positioning.x_title_size = 0.075
normal_positioning.x_title_offset = 0.9

normal_positioning.plot_label_offset = normal_label_offset
normal_positioning.plot_label_size   = normal_label_size

normal_positioning.legend_spacing = 0.03 ####From 0.03 to 0.005
normal_positioning.legend_xmax    = 1.00
normal_positioning.legend_ymax    = 0.73
