###################################################
class Cutset(list):
    """
    A class to house a set of cuts, that can either be applied as a cut string (ROOT style)
    or event-based style.
    """

    ## --------------------------------------------- ##
    def __init__(self):
        """
        Constructor
        """

        self.empty = True
    

    ## --------------------------------------------- ##
    def cut(self, variable, comparator='', value=0):
        """
        Add a cut to the cut list
        """
        self.empty = False
        self.append((variable, comparator, value))


    ## --------------------------------------------- ##
    def string(self):
        """
        Builds a string for the ROOT interpreter
        """

        single_cuts = []

        for cut in self:
            if cut[1]:
                if cut[1] == '==' and cut[2] == False:
                    single_cuts.append('(!%s)' % cut[0])
                else:
                    single_cuts.append('(%s%s%s)' % (cut[0], cut[1], cut[2]))

            else:
                single_cuts.append('(%s)' % cut[0])

        return '&&'.join(single_cuts)


    ## --------------------------------------------- ##
    def evaluate(self, event):
        """
        Evaluate if an event is a part of the subset
        """

        for cut in self:
            event_value = getattr(event, cut[0].lstrip('!'))
            comparator = cut[1]
            compared_to = cut[2]
            
            ## smaller than
            if comparator == '<':
                if not event_value < compared_to: return False

            ## smaller than or equal
            elif comparator == '<=':
                if not event_value <= compared_to: return False

            ## greater than
            elif comparator == '>':
                if not event_value > compared_to: return False

            ## greater than or equal
            elif comparator == '>=':
                if not event_value >= compared_to: return False

            ## Checking boolean to be true
            elif comparator == '':
                if cut[0][0] == '!':
                    if event_value: return False
                else:
                    if not event_value: return False
                
            ## equal
            elif comparator == '==':
                if not event_value == compared_to: return False

            else:
                raise ValueError('Comparator %s unknown, add it into the evaluate method of the CutList class.' % comparator)

        return True


    

###################################################
class Subset(list):
    """
    A collection of subsets with string and evaluate methods
    """

    ## --------------------------------------------- ##
    def __init__(self, name, logic='or'):
        """
        Constructor
        """

        self.name = name
        self.logic = logic
        self.cutset = Cutset()


        
    ## --------------------------------------------- ##
    def cut(self, variable, comparator='', value=0):
        """
        Create a cut set if Subset doesn't have its own, and add cuts to it
        """
        
        self.cutset.cut(variable, comparator, value)

        
    
    ## --------------------------------------------- ##
    def string(self):
        """
        Builds a string for the ROOT interpreter
        """

        if not self.cutset.empty:
            cut_strings = ['(%s)' % self.cutset.string()]
        else:
            cut_strings = []
        
        for subset in self:
            cut_strings.append(subset.string())

        string = ''
        if self.logic == 'and':
            string = '&&'.join(cut_strings)
        if self.logic == 'or':
            string = '||'.join(cut_strings)

        if len(self) > 0:
            string = '(%s)' % string

        return string
            


    ## --------------------------------------------- ##
    def evaluate(self, event):
        """
        Evaluate if an event is a part of the subsets, according to the logic linking the subsets
        """

        if not self.cutset.empty:
            cut_booleans = [self.cutset.evaluate(event)]
        else:
            cut_booleans = []

        for subset in self:
            cut_booleans.append(subset.evaluate(event))

        answer = False
        if self.logic == 'and':
            answer = True
            for cut_boolean in cut_booleans:
                answer = answer and cut_boolean

        if self.logic == 'or':
            answer = False
            for cut_boolean in cut_booleans:
                answer = answer or cut_boolean
        
        return answer


    
    ## --------------------------------------------- ##
    def add_subset(self, subset):
        """
        Add a subset to self
        """

        self.append(subset)



    ## --------------------------------------------- ##
    def __iadd__(self, other):
        """
        Add a subset to self
        """

        self.append(other)
        return self


    
    ## --------------------------------------------- ##
    def __add__(self, other):
        """
        Returns an and-ed subset
        """

        new_subset = Subset('%s_%s' % (self.name, other.name), 'and')
        new_subset += self
        new_subset += other

        return new_subset


    ## --------------------------------------------- ##
    def __mul__(self, other):
        """
        Returns an or-ed subset
        """

        new_subset = Subset('%s_%s' % (self.name, other.name), 'or')
        new_subset += self
        new_subset += other

        return new_subset
