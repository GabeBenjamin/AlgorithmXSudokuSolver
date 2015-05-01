__author__ = 'Gabe Benjamin'

from SudokuVerifier import Board
from SudokuVerifier import SudokuVerifier
from AlgorithmX import AlgorithmX
from DancingLink import DancingLink
import math

class SudokuSolver():

    def getRegion(self, r, c, width):
        mRow = int(r/width)
        mCol = int(c/width)
        return int(mCol + mRow*width)

    def generateRow(self, val, r, c, size):
        row = [0 for x in range(size*size*4)]
        # Constraint 1
        row[r*size+c] = 1

        # Row Constraint
        row[size*size + r*size + (val-1)] = 1

        # Col Constraint
        row[2*size*size + c*size + (val-1)] = 1

        # Region Constraint
        region = self.getRegion(r,c, math.sqrt(size))
        row[3*size*size + region*size + (val-1)] = 1

        return row

    def get1ColsForRow(self, row):
        cols = []
        for i, val in enumerate(row):
            if val == 1:
                cols.append(i)
        return cols

    def generate2DEP(self, board):
        rows = []
        for i in range(board.size):
            for j in range(board.size):
                # If empty, generate rows for all possible
                if board.board[i][j] <= 0:
                    for k in range(board.size):
                        row = self.generateRow(k+1, i, j, board.size)
                        rows.append(row)
                else:
                    row = self.generateRow(board.board[i][j], i, j, board.size)
                    rows.append(row)
        return rows



    def solve(self, board):
        cols = []
        for i in range(board.size*board.size*4):
            cols.append(str(i))
        rows = self.generate2DEP(board)
        dl = DancingLink(rows,cols)
        AX = AlgorithmX()
        result = AX.search(0, dl.root, [])
        if result == None:
            print "NO POSSIBLE SOLUTION"
            return None
        else:
            size = board.size
            for answer in result:
                cols = self.get1ColsForRow(rows[answer.row - 1])
                #print "COLS: " + str(cols)
                ar = answer.row
                val = ((cols[2] - size*size) % size) + 1
                row = int((cols[1] - size*size)/size)
                col = int((cols[2] - 2*size*size)/size)
                #print "val = " + str(val) + " row = " + str(row) + " col = " + str(col)

                if (board.board[row][col] == 0) or (board.board[row][col] == -1):
                    board.board[row][col] = val
                else:
                    print "ACTUAL = " + str(board.board[row][col]) + " GUESS = " + str(val)
        return board



def main():
    ss = SudokuSolver()
    """
    b = Board(4)
    #b.board[0][0] = 3
    ep = ss.generate2DEP(b)
    for x, row in enumerate(ep):
        mStr = ""
        for i, col in enumerate(row):
            if i == 0:
                if x < 10:
                    mStr += " "
                mStr += str(x) + "| "
            elif i % 16 == 0:
                mStr += " || "
            mStr += str(col) + ", "
        print mStr
    """
    b2 = Board(4)
    b2.inputBoard("input/4x4_01_unsolved.txt")
    ep = ss.generate2DEP(b2)
    for x, row in enumerate(ep):
        mStr = ""
        for i, col in enumerate(row):
            if i == 0:
                if x < 10:
                    mStr += " "
                mStr += str(x) + "| "
            elif i % 16 == 0:
                mStr += " || "
            mStr += str(col) + ", "
        print mStr
    b2.printBoard()
    result = ss.solve(b2)
    result.printBoard()
    sv = SudokuVerifier()
    print sv.verify(result)

    b3 = Board(9)
    b3.inputBoard("input/partial01.txt")
    b3.printBoard()
    result2 = ss.solve(b3)
    result2.printBoard()
    print sv.verify(result2)


if __name__ == "__main__":
    main()