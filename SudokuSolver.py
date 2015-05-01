__author__ = 'Gabe Benjamin'

from SudokuVerifier import Board
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
        AX.search(0, dl.root, [])


def main():
    ss = SudokuSolver()
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


if __name__ == "__main__":
    main()