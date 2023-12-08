'''
37. Sudoku Solver
Hard
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:
Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.
Example 1:
Input: board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]]

Output: [
    ["5","3","4","6","7","8","9","1","2"],
    ["6","7","2","1","9","5","3","4","8"],
    ["1","9","8","3","4","2","5","6","7"],
    ["8","5","9","7","6","1","4","2","3"],
    ["4","2","6","8","5","3","7","9","1"],
    ["7","1","3","9","2","4","8","5","6"],
    ["9","6","1","5","3","7","2","8","4"],
    ["2","8","7","4","1","9","6","3","5"],
    ["3","4","5","2","8","6","1","7","9"]]
'''
from typing import TypeAlias, List, Optional

Board:TypeAlias=List[List[str]]
Index:TypeAlias=tuple[int,int,tuple[int,int]]

def inc(i: Optional[Index]) -> Index:
    if i is None:
        return (0,0,(0,0))
    row,col,_ = i
    col +=1
    if col == 9:
        col = 0
        row +=1
    sq = (row//3, col//3)
    return (row,col,sq)

class Sudoku():
    '''Implements Sudoku with  backtracking'''

    @staticmethod
    def print_board(a:Board) -> None:
        for i in a:
            print(''.join(i))

    def __init__(self, board:Board) -> None:
        super().__init__()
        self.finished: bool=False
        self.board:Board = board
        self.all_values:frozenset[str] = frozenset(['1','2','3','4','5','6','7','8','9'])
        # Init constraint sets from the board
        self.constraint_rows = [set(i) for i in board]
        self.constraint_cols = \
            [set([board[row][col] for row in range(9)])\
                for col in range(9)]
        self.constraint_sq:dict[tuple[int,int],set[str]] = \
            {(row,col):set([]) for col in range(3) for row in range(3)}
        i:Index = Index((0,0,(0,0)))
        while True:
            row,col,sq = i
            if row == 9:
                break
            self.constraint_sq[sq].add(board[row][col])
            i = inc(i)

        #print(self.init_constraint_rows)
        #print(self.init_constraint_cols)
        #print(self.init_constraint_sq)

    def isasolution(self, i:Optional[Index]) -> bool:
        if i is None:
            return False
        return i[0] == i[1] == 8

    def process_solution(self) -> None:
        self.finished = True
        Sudoku.print_board(self.board)

    def construct_candidates(self, row:int, col:int, sq:tuple[int,int]) \
            -> tuple[bool,frozenset[str]]:
        #check if the next pick is constrained
        #row,col,sq = i
        #print(f'cc {row=}, {col=}, {sq=}, {self.board[row]=}',end='')
        v = self.board[row][col]
        if v != '.':
            #print(f'const: {v=}')
            return (True,frozenset([v]))
        #Unconstrained
        candidates:frozenset[str]= self.all_values - \
            self.constraint_cols[col] -\
            self.constraint_rows[row] -\
            self.constraint_sq[sq]
        #print(f'unconst {candidates=}')
        return (False,candidates)


    def make_move(self, guess:str, row:int, col: int, sq: tuple[int,int]) -> None:
        #row,col,sq = i
        #commit the move
        self.board[row][col] = guess
        self.constraint_rows[row].add(guess)
        self.constraint_cols[col].add(guess)
        self.constraint_sq[sq].add(guess)
        return

    def unmake_move(self, guess:str,  row:int, col: int, sq: tuple[int,int]) -> None:
        #row,col,sq = i
        self.board[row][col] = '.'
        self.constraint_rows[row].discard(guess)
        self.constraint_cols[col].discard(guess)
        self.constraint_sq[sq].discard(guess)

    def backtrack(self, i:Optional[Index]=None) -> None:
        #print(i)
        if self.isasolution(i):
            self.process_solution()
        else:
            succ:Index = inc(i)
            constrained, candidates = self.construct_candidates(*succ)
            for k in candidates:
                if not constrained:
                    self.make_move(k, *succ)
                self.backtrack(succ)
                if self.finished:
                    return
                if not constrained:
                    self.unmake_move(k, *succ)

class Solution:
    # pylint: disable-next=[invalid-name, redefined-outer-name]
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        su = Sudoku(board)
        su.backtrack()


if __name__ == "__main__":
    s=Solution()
    testboard:Board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    s.solveSudoku(testboard)
