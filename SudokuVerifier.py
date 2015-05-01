import random
import math

class Board:
  size = 0
  def __init__(self, mSize):
    self.size = mSize
    #Create an empty board of size mSize x mSize
    self.clearBoard()

  def clearBoard(self):
    self.board = [[-1 for i in range(self.size)] for j in range(self.size)]
  def generateRandom(self):
    for i in range(self.size):
      for j in range(self.size):
        r = random.randrange(self.size)
        slot = self.board[i][r]
        while(slot != -1):
          r = random.randrange(self.size)
          slot = self.board[i][r]
        self.board[i][r] = j+1
  def printBoard(self):
    mStr = ""
    for i in range(self.size):
      if i != 0 and i % math.sqrt(self.size) == 0:
        mult = (self.size*3 + (int(math.sqrt(self.size))-1)*3)
        print "mult = " + str(mult)
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

  def generateRandom2(self):
    count = 0
    while count < self.size * self.size:
      r = random.randrange(self.size)
      c = random.randrange(self.size)
      if self.board[r][c] == -1:
        self.board[r][c] = count % self.size + 1
        count += 1

  def generateCorrect(self):
    #TODO
    pass

  def inputBoard(self, fileName):
    f = open(fileName)
    self.size = int(f.readline().split()[0])
    i = 0
    for line in f:
      self.board[i] = [int(x) for x in line.split()]
      i += 1
    

class SudokuVerifier:

  def verify(self,board):
    for i in range(board.size):
      rows = [False for x in range(board.size)]
      cols = [False for x in range(board.size)]
      for j in range(board.size):
        val1 = board.board[i][j]
        val2 = board.board[j][i]
        #check duplicates
        if not rows[val1-1]:
          rows[val1-1] = True
        else:
          return False
        #check duplicates
        if not cols[val2-1]:
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
            if not box[val-1]:
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
  print(sv.verify(b))

if __name__ == "__main__":
  main()
