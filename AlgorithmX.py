"""
Implmentation of Algorithm X as described by Donald E. Knuth in "Dancing Links"

By Gabe Benjamin and Dan Hu
"""
from DancingLink import DancingLink
import inspect

class AlgorithmX():
    """
    Finds a solution to the exact cover problem and returns it
    If there is no solution, it returns None
    """
    def search(self,k,h,sol):
        if h.right == h:
            #print dLListToString(sol)
            return sol
        c = chooseColumn(h)
        if c == None:
            return None
        #print "Chose col: "  + c.toString()

        coverC(c)

        r = c.down
        while r != c:
            sol.append(r)
            j = r.right
            while j != r:
                coverC(j)
                j = j.right
            result = self.search(k+1, h, sol)
            if result != None:
                return result
            r = sol.pop()
            c = r.listHeader
            j = r.left
            while j != r:
                uncoverC(j)
                j = j.left
            r = r.down
        uncoverC(c)

def lineno():
    return inspect.currentframe().f_back.f_lineno

def dLListToString(lst):
    str = "["
    for link in lst:
        if link != None:
            str += link.toString() + ", "
        else:
            str += " , "
    return str[:-2] + "]"

"""
Covers column c
"""
def coverC(c):
    #print "COVER: " + c.toString()
    c.listHeader.right.left = c.listHeader.left
    c.listHeader.left.right = c.listHeader.right
    i = c.listHeader.down
    while i != c.listHeader:
        #print "LOOP C1"
        #print "i = " + i.toString() + " c = " + c.toString()
        j = i.right
        while j != i:
            j.down.up = j.up
            j.up.down = j.down
            j.listHeader.size -= 1
            j = j.right
        i = i.down

"""
Uncovers column c
"""
def uncoverC(c):
    #print "**BEGIN UNCOVER**"
    #print "uncover: " + c.listHeader.toString()
    i = c.listHeader.up
    while i != c.listHeader:
        j = i.left
        while j != i:
            j.listHeader.size += 1
            j.down.up = j
            j.up.down = j
            j = j.left
        i = i.up
    c.listHeader.right.left = c.listHeader
    c.listHeader.left.right = c.listHeader

def chooseColumn(h):
    node = h.right
    minVal = -1
    minCol = None
    while node != h:
        if node.size != 0 and (minVal == -1 or node.size < minVal):
            minVal = node.size
            minCol = node
        node = node.right
    return minCol


####TEST FUNCTIONS####
def testCoverC():
    arr = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
    names = ["A", "B", "C"]
    dl = DancingLink(arr,names)
    print(dl.toString())
    colB = dl.root.right.right
    colC = colB.right
    print("SHOULD BE 'B' = " + colB.name)
    print("SHOULD BE 'C' = " + colC.name)
    dl.printColumn(colB)
    dl.printColumn(colC)
    coverC(colB)
    print(dl.toString())
    dl.printColumn(colC)

def testCoverUncover():
    arr = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
    names = ["A", "B", "C"]
    dl = DancingLink(arr,names)
    print(dl.toString())
    colB = dl.root.right
    coverC(colB)
    print(dl.toString())
    uncoverC(colB)
    print(dl.toString())

def testBasic():
    arr = [[0,1,0], [1,1,0], [0,0,1],[1,0,0]]
    names = ["A", "B", "C"]
    dl = DancingLink(arr,names)
    print(dl.toString())
    result = search(0, dl.root, [], dl)
    if result != None:
        print dLListToString(result)

def testBasic2():
    arr = [[1,0,0,0],[0,1,1,0],[1,0,0,0],[0,0,0,1]]
    names = ["A", "B", "C", "D"]
    dl = DancingLink(arr,names)
    print(dl.toString())
    result = search(0, dl.root, [], dl)
    if result != None:
        print dLListToString(result)

def main():
    #testCoverC()
    testBasic2()

if __name__ == "__main__":
    main()