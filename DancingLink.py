"""
An implementation of Dancinc Links as described by Donald E. Knuth in his paper
"Dancing Links". Dancing links are an extended form of circular, doubly-linked
lists.

Implemented by Gabe Benjamin and Dan Hu
"""
class DancingLink(object):
    def __init__(self, arr =None, names =None):
        self.root = None
        if arr != None and names != None:
            if len(arr) == 0 or len(names) == 0:
                raise ValueError("No items in array")
            if len(arr[0]) != len(names):
                raise ValueError("Number of columns do not match")
            for col in names:
                self.addColumn(col)
            for row in arr:
                self.addRow(row)

    def addColumn(self, name):
        newC = Column(name)
        # Check for no root
        if self.root == None:
            # Set column to point to itself circularly
            newC.left = newC
            newC.right = newC
            newC.up = newC
            newC.down = newC
            newC.listHeader = newC

            # Set root to be column
            self.root = newC
        else:
            # Get the last column
            last = self.root.left

            # Set New Column links
            newC.right = self.root
            newC.left = self.root.left
            newC.up = newC
            newC.down = newC
            newC.listHeader = newC

            # Change last link and root to point to newC
            last.right = newC
            self.root.left = newC

    # Adds a row to links
    # Row must be list of 0's and 1's in order of columns
    # so row = [0, 0, 1, 0, 1, 1, 0] will add links to
    # C, E, and F, 
    def addRow(self, row):
        first = None
        prev = None
        column = self.root
        for (i, val) in enumerate(row):
            if i != 0 and column == self.root:
                raise ValueError("i = " + str(i) + " column = " + column.name)
            if val == 1:
                lastLink = column.up
                newLink = Link()
                
                newLink.up = lastLink
                newLink.down = lastLink.down
                newLink.left = prev
                if prev != None:
                    prev.right = newLink
                lastLink.down = newLink
                newLink.listHeader = column

                # Progress prev
                prev = newLink

                # Set first if not yet set
                if first == None:
                    first = newLink

                # Update column count
                column.size += 1
            column = column.right
        if first != None:
            first.left = prev
            prev.right = first


            



    def headersToString(self, root):
        s = "  " + root.name + " "
        col = root.right
        while(col != root):
            s += col.name + " "
            col = col.right
        return s + "\n"

    def toString(self):
        s = ""
        if self.root == None:
            s = "[ ]"
            return s
        else:
            #s += self.headersToString(self.root)
            colLink = self.root
            rowLink = colLink.down
            s += "(" + colLink.name +", " + str(colLink.size) +"): "
            while (rowLink != colLink):
                s += rowLink.name + " "
                rowLink = rowLink.down
            colLink = colLink.right
            s += "\n"
            while(colLink != self.root):
                s += "(" + colLink.name +", " + str(colLink.size) +"): "
                rowLink = colLink.down
                while (rowLink != colLink):
                    s += rowLink.name + " "
                    rowLink = rowLink.down
                colLink = colLink.right
                s += "\n"

        return s



class Link(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.up = None
        self.down = None
        self.listHeader = None # Points to Column header
        self.name = "1"

class Column(object):
    def __init__(self, name):
        self.left = None
        self.right = None
        self.up = None
        self.down = None
        self.listHeader = None #?
        self.size = 0 # The number of 1's in the column
        self.name = name # Symbolic identifier for printing
