import random
import math

class Board:
  size = 0
  def __init__(self, mSize):
    self.size = mSize
    #Create an empty board of size mSize x mSize
    self.clearBoard()

  def clearBoard(self):
    self.board = [[0 for i in range(self.size)] for j in range(self.size)]

  def generateRandom(self):
    for i in range(self.size):
      for j in range(self.size):
        r = random.randrange(self.size)
        slot = self.board[i][r]
        while(slot != 0):
          r = random.randrange(self.size)
          slot = self.board[i][r]
        self.board[i][r] = j+1

  def printBoard(self):
    mStr = ""
    for i in range(self.size):
      if i != 0 and i % math.sqrt(self.size) == 0:
        mult = (self.size*3 + (int(math.sqrt(self.size))-1)*3)
        #print "mult = " + str(mult)
        mStr += '-'*mult
        mStr += "\n"
      for j in range(self.size):
        if j != 0 and j % math.sqrt(self.size) == 0:
          mStr += "|| "
        val = self.board[i][j]
        if val < 10:
          mStr += " "
        mStr += str(self.board[i][j]) + " "
      mStr += "\n"
    print(mStr)

  def lineToBoard(self,file,lineNum):
    f = open(file)
    self.size = 9
    lines = f.readlines()
    for i, x in enumerate(lines[lineNum]):
      if x != '\n':
        row = int(i / 9)
        col = i % 9
        #print "row = " + str(row) + " col = " + str(col) + " val = " + str(x)
        if x == ".":
          self.board[row][col] = 0
        else:
          self.board[row][col] = int(x)


  def generateRandom2(self):
    count = 0
    while count < self.size * self.size:
      r = random.randrange(self.size)
      c = random.randrange(self.size)
      if self.board[r][c] == 0:
        self.board[r][c] = count % self.size + 1
        count += 1

  def generateCorrect(self):
    from SudokuSolver import SudokuSolver
    ss = SudokuSolver()
    sv = SudokuVerifier()

    #Generate a few random numbers first

    count = 0
    while count < self.size*self.size * 0.1:
      r = random.randrange(self.size)
      c = random.randrange(self.size)
      if self.board[r][c] == 0:
        v = random.randrange(self.size) + 1
        self.board[r][c] = v
        if not sv.verifyPatial(self):
          self.board[r][c] = 0
        else:
          count += 1

    self.board = ss.solve(self).board




  def inputBoard(self, fileName):
    f = open(fileName)
    self.size = int(f.readline().split()[0])
    i = 0
    for line in f:
      self.board[i] = [int(x) for x in line.split()]
      i += 1
    

class SudokuVerifier:

  """
  Same as verify, but without the constraint that all numbers are used
  for row, col, and region
  """

  def verifyPatial(selfs, board):
    for i in range(board.size):
      rows = [False for x in range(board.size)]
      cols = [False for x in range(board.size)]
      for j in range(board.size):
        val1 = board.board[i][j]
        val2 = board.board[j][i]

        if val1 == 0:
          pass
        #check duplicates
        elif not rows[val1-1]:
          rows[val1-1] = True
        else:
          return False
        #check duplicates
        if val2 == 0:
          pass
        elif not cols[val2-1]:
          cols[val2-1] = True
        else:
          return False

    sq = int(math.sqrt(board.size))
    for i in range(sq):
      for j in range(sq):
        box = [False for x in range(board.size)]
        #check for duplicates in box
        for r in range(i*sq, (i+1)*sq):
          for c in range(j*sq, (j+1)*sq):
            val = board.board[r][c]
            #print(val)
            if val == 0:
              pass
            elif not box[val-1]:
              box[val-1] = True
            else:
              return False

    return True

  """
  Verifies if the board meets the row, column, and region constraints
  """
  def verify(self,board):
    for i in range(board.size):
      rows = [False for x in range(board.size)]
      cols = [False for x in range(board.size)]
      for j in range(board.size):
        val1 = board.board[i][j]
        val2 = board.board[j][i]
        #check duplicates
        if val1 == 0:
          return False
        #check duplicates
        elif not rows[val1-1]:
          rows[val1-1] = True
        else:
          return False
        #check duplicates
        if val2 == 0:
          return False
        elif not cols[val2-1]:
          cols[val2-1] = True
        else:
          return False
      #check to make sure all numbers satisfied
      for j in range(board.size):
        if not rows[j]:
          return False
        if not cols[j]:
          return False
    sq = int(math.sqrt(board.size))
    for i in range(sq):
      for j in range(sq):
        box = [False for x in range(board.size)]
        #check for duplicates in box
        for r in range(i*sq, (i+1)*sq):
          for c in range(j*sq, (j+1)*sq):
            val = board.board[r][c]
            #print(val)
            if val == 0:
              return False
            elif not box[val-1]:
              box[val-1] = True
            else:
              return False
        #check box uses all numbers at least once
        for x in range(board.size):
          if not box[x]:
            return False
    return True

def main():
  b = Board(9)
  b.generateRandom()
  #b.inputBoard("solved01.txt")
  b.printBoard()
  sv = SudokuVerifier()
  print("Random, likely false: " + str(sv.verify(b)))

  b2 = Board(4)
  b2.inputBoard("input/4x4_01.txt")
  b2.printBoard()
  print("Should be true: " + str(sv.verify(b2)))

  b3 = Board(4)
  b3.inputBoard("input/4x4_01_unsolved.txt")
  b3.printBoard()
  print("b3 = " + str(sv.verifyPatial(b3)))

  b4 = Board(9)
  b4.printBoard()
  print("b4 = " + str(sv.verifyPatial(b4)))

  b5 = Board(9)
  b5.generateCorrect()
  b5.printBoard()
  print("b5 = " + str(sv.verify(b5)))


if __name__ == "__main__":
  main()
