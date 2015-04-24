"""
An implementation of Dancinc Links as described by Donald E. Knuth in his paper
"Dancing Links". Dancing links are an extended form of circular, doubly-linked
lists.

Implemented by Gabe Benjamin and Dan Hu
"""
class DancingLink(object):
    def __init__(self):
        self.root = None

    def toString(self):
        if self.root == None:
            s = "[ ]"
            return s
        else:
            s += printRow(self.root)
            start = self.root.down
            while(start != self.root):
                s += printRow(start)
                start = start.down
        return s



class Link(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.up = None
        self.down = None
        self.listHeader = None # Points to Column header

class Column(Link):
    def __init__(self):
        self.left = None
        self.right = None
        self.up = None
        self.down = None
        self.listHeader = None #?
        self.size = 0 # The number of 1's in the column
        self.name = "" # Symbolic identifier for printing
