# Algorithm X Sudoku Solver

This is a project to implement [Donald Knuth's Algorithm X](http://arxiv.org/abs/cs/0011047 "Algorithm X") using his [DancingLinks data](http://en.wikipedia.org/wiki/Dancing_Links) structure, which is a solution to the NP-Complete Exact Cover Problem. We then use this aglorithm to solve an n x n sudoku board. There are two main parts to this project: the Sudoku Verifier and the Sudoku Solver. Solving a sudoku board is a form of the exact cover problem and thereofre is also NP-Complete. THis means that we can write a polynomial time verifier, but not a solver.

## How to run
To see all the pieces working together you can simply run 
```
python SudokuSolver.py
```
In SudokuSolver.py, there are a few test cases you can run and the default is to run the solver against 95 hard (i.e. sparse) Sudoku problems. You can also create your own Sudoku board. The easiest way to do this is to create an input file that is formatted like this:
```
<size>
<first row>
<second row>
...
```
where <size> is a single int, and each row is <size> ints long, separated by commas. For examples of this see the input folder. Use 0's if you want to have a spot blank.

You can then simply call:
```python
mBoard = Board(9)
mBoard.inputBoard("myInput.txt")
```

Then to solve the board you simply pass the board to a SudokuSolver like so:
```python
ss = SudokuSolver()
solvedBoard = ss.solve(mBoard)
```
## Sudoku Verifier
//TODO

## Sudoku Solver
We use Knuth's Algorithm X and DancingLinks to create a Sudoku Solver relatively efficiently.
//TODO

### DancingLinks
//TODO

### Algorithm X
//TODO

## ToDo List
- [x] Implement Sudoku Verifier
- [ ] Implment DancingLinks data structure
- [ ] Implement Algorithm X using DancingLinks
- [ ] Implement Sudoku Solver using Algorithm X
- [ ] Finish README
