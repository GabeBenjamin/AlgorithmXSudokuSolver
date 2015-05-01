"""
Implmentation of Algorithm X as described by Donald E. Knuth in "Dancing Links"

By Gabe Benjamin and Dan Hu
"""
from DancingLink import DancingLink
import inspect

class AlgorithmX():
    def search(self,k,h,sol):
        pass

def lineno():
    return inspect.currentframe().f_back.f_lineno

def dLListToString(lst):
    str = "["
    for link in lst:
        if link != None:
            str += link.listHeader.toString() + ", "
        else:
            str += " , "
    return str[:-2] + "]"

def coverC(c):
    print "COVER: " + c.toString()
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

def printSolution(link, h):
    mStr = link.listHeader.toString() + ", "
    next = link.right
    print link.toString()
    while next != link:
        #print next.toString()
        mStr += next.listHeader.toString() + ", "
        next = next.right

    print "SOLUTION:: " + mStr[-2]
    print "END SOLUTION"

def search(k, h , sol,root):
    print("*"*20)
    print "SEARCH: " + str(k) + ", sol = " + dLListToString(sol), lineno()
    print(root.toString())
    # If the matrix is empty, return
    if h.right == h:
        print("~"*20)
        print(root.toString())
        print dLListToString(sol)
        print("~"*20)
        return sol
    # Choose column
    c = h.right.listHeader #TODO optimize this
    #print("SELECTING C:")
    while(c.size == 0 and c != h):
        #print("c = " + c.toString() + " size: " + str(c.size))
        c = c.right
    if c.size == 0:
        return None
    ###sol.append(c.name)

    # Cover column c
    coverC(c)
    #print(root.toString())

    r = c.down
    while c != r:
        print "r = " + r.toString()
        save = r
        sol.append(r)
        j = r.right
        while j != r and j != h:
            #print "LOOP 1"
            #cover column j
            coverC(j)
            j = j.right
        print "END LOOP 1"
        result = search(k+1, h, sol,root)

        # If we returned an answer,
        # then we can immediately stop and return
        if result != None:
            return result
        r = sol.pop()
       # r = save
        c = r.listHeader#c = c.right CHANGED B/C JAVA
        j = r.left
        #print(root.toString())
        while j != r:
            #print "Uncover:"
            #print "j = " + j.toString() + " r = " + r.toString()
            #uncover column j
            uncoverC(j)
            j = j.left
            #print(root.toString())
        print "END LOOP 2"
        print(root.toString())
        r = r.down
    #Uncover column c and return
    uncoverC(c)


def search2():
    if h.right == h:
        printSolution(sol)
        return
    col = chooseNextCol(h)
    coverC(col)
    row = col.down
    while row != col:
        sol.append(row)
        rightNode = row.right
        while rightNode != row:
            coverC(rightNode)
            rightNode = rightNode.right

        search2(k+1, h)
        sol.pop()
        col = row.listHeader
        row = row.down

def chooseColumn(h):
    node = h.right
    minVal = node.size
    minCol = node
    while node != h:
        if node.size < minVal:
            minVal = node.size
            minCol = node
        node = node.right
    return minCol


def search3(k, h, sol):
    if h.right == h:
        print "SOLUTION"
    c = chooseColumn(h)
    print "Chose col: "  + c.toString()
    r = c.down
    while r != c:
        sol.append(r)
        j = r.right
        while j != r:
            coverC(j)
            j = j.right
        search3(k+1, h, sol)
        r = sol.pop()
        c = r.listHeader
        j = r.left
        while j != r:
            uncoverC(j)
            j = j.left
        r = r.down
    uncoverC(c)


####TEST FUNCTIONS####
def testCoverC():
    arr = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
    names = ["A", "B", "C"]
    dl = DancingLink(arr,names)
    print(dl.toString())
    colB = dl.root.right
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
    arr = [[0,1,1], [1,1,0], [0,0,1],[1,0,0]]
    names = ["A", "B", "C"]
    dl = DancingLink(arr,names)
    print(dl.toString())
    result = search(0, dl.root, [], dl)
    print "Result: " + str(result)

def testBookExample():
    arr = [[0,0,1,0,1,1,0], [1,0,0,1,0,0,1], [0,1,1,0,0,1,0],[1,0,0,1,0,0,0],[0,1,0,0,0,0,1],[0,0,0,1,1,0,1]]
    names = ["A", "B", "C", "D", "E", "F", "G"]
    dl = DancingLink(arr, names)
    result = search3(0, dl.root, [])
    print "Result: " + str(result)

def main():
    #testBasic()
    testBookExample()

if __name__ == "__main__":
    main()