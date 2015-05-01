"""
An implementation of Dancinc Links as described by Donald E. Knuth in his paper
"Dancing Links". Dancing links are an extended form of circular, doubly-linked
lists.

Implemented by Gabe Benjamin and Dan Hu
"""
class DancingLink(object):
    def __init__(self, arr =None, names =None):
        # Set the root to be an empty column
        mRoot = Link("__H__", 0)
        mRoot.left = mRoot
        mRoot.right = mRoot
        mRoot.up = mRoot
        mRoot.down = mRoot
        mRoot.listHeader = mRoot
        self.root = mRoot
        self.numRows = 0
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
        newC = Link(name, 0)

        # Get the last column
        last = self.root.left

        # Set New Column links
        newC.right = self.root
        newC.left = last
        newC.up = newC
        newC.down = newC
        newC.listHeader = newC

        # Change last link and root to point to newC
        last.right = newC
        self.root.left = newC

    def printColumn(self, c):
        next = c.down
        mStr = c.name + "::" + str(c.row) +"\n^\n|\nv\n"
        while next != c:
            mStr += next.name + "::" + str(next.row) +"\n^\n|\nv\n"
            next = next.down
        print mStr[:-6]

    # Adds a row to links
    # Row must be list of 0's and 1's in order of columns
    # so row = [0, 0, 1, 0, 1, 1, 0] will add links to
    # C, E, and F, 
    def addRow(self, row):
        self.numRows += 1
        first = None
        prev = None
        column = self.root.right
        for (i, val) in enumerate(row):
            if i != 0 and column == self.root:
                raise ValueError("i = " + str(i) + " column = " + column.name)
            if val == 1:
                lastLink = column.up
                newLink = Link("x", self.numRows)
                
                newLink.up = lastLink
                newLink.down = column
                newLink.left = prev
                if prev != None:
                    prev.right = newLink
                lastLink.down = newLink
                newLink.listHeader = column
                column.up = newLink

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
                s += rowLink.name + "::" + str(rowLink.row) + ", "
                rowLink = rowLink.down
            colLink = colLink.right
            s += "\n"
            while(colLink != self.root):
                s += "(" + colLink.name + ", " + str(colLink.size) +"): "
                rowLink = colLink.down
                while (rowLink != colLink):
                    s += rowLink.name + "::" + str(rowLink.row) + ", "
                    rowLink = rowLink.down
                colLink = colLink.right
                s += "\n"

        return s



class Link(object):
    def __init__(self, name="-1", mRow=-1):
        self.left = None
        self.right = None
        self.up = None
        self.down = None
        self.size = 0 # The number of 1's in the column
        self.name = name # Symbolic identifier for printing
        self.row = mRow

    def toString(self):
        return self.listHeader.name + "::" + self.name + "::" + str(self.row)

