class Style:

    """
    Constructor
    """
    def __init__(self, 
                 name):
        self.name = name
        self.fill_style = 1001
        self.line_style = 1
        self.line_width = 1
        self.marker_style = 20
        self.marker_size = 1.0
        self.draw_options = 'HIST'


    def apply(self,
              h):
        h.SetLineStyle(self.line_style)
        h.SetLineWidth(self.line_width)
        h.SetMarkerStyle(self.marker_style)
        h.SetMarkerSize(self.marker_size)
        h.SetFillStyle(self.fill_style)

def
        

        
