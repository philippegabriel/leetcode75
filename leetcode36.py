'''
36. Valid Sudoku
'''
from typing import List
from collections import Counter
from itertools import product
class Solution:
    # pylint: disable-next=invalid-name
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen:set[str]=set()
        #check rows
        for row in board:
            seen=set()
            for i in row:
                if i == '.':
                    continue
                if i in seen:
                    return False
                seen.add(i)
        #check columns
        for col in range(9):
            seen=set()
            for row in range(9):
                if (i:=board[row][col]) == '.':
                    continue
                if i in seen:
                    return False
                seen.add(i)
        intervals:tuple[tuple[int,...],...]=((0,1,2),(3,4,5),(6,7,8))
        #check squares
        for rows, cols in product(intervals, intervals):
            seen=set()
            for row in rows:
                for col in cols:
                    if (i:=board[row][col]) == '.':
                        continue
                    if i in seen:
                        return False
                    seen.add(i)
        return True

    # pylint: disable-next=invalid-name
    def isValidSudokuCounter(self, board: List[List[str]]) -> bool:
        rcounter:list[Counter[str]]=[]
        #check rows
        for row in board:
            rcounter.append(Counter(row))
        #check columns
        for col in range(9):
            rcounter.append(Counter([board[row][col] for row in range(9)]))
        intervals:tuple[tuple[int,...],...]=((0,1,2),(3,4,5),(6,7,8))
        #check squares
        for rows, cols in product(intervals, intervals):
            rcounter.append(Counter([board[row][col] for row in rows for col in cols]))
        # for i,l in enumerate(rcounter):
        #     print(f'{i=},{l=}')
        #check counters
        for i in rcounter:
            i['.']=0
            _,v = i.most_common(1)[0]
            if v>1:
                return False
        return True

def test() -> None:
    s=Solution()
    board= [[".",".","4",".",".",".","6","3","."]
                            ,[".",".",".",".",".",".",".",".","."]
                            ,["5",".",".",".",".",".",".","9","."]
                            ,[".",".",".","5","6",".",".",".","."]
                            ,["4",".","3",".",".",".",".",".","1"]
                            ,[".",".",".","7",".",".",".",".","."]
                            ,[".",".",".","5",".",".",".",".","."]
                            ,[".",".",".",".",".",".",".",".","."]
                            ,[".",".",".",".",".",".",".",".","."]]
    assert not s.isValidSudoku(board)

    board = [["5","3",".",".","7",".",".",".","."]
                            ,["6",".",".","1","9","5",".",".","."]
                            ,[".","9","8",".",".",".",".","6","."]
                            ,["8",".",".",".","6",".",".",".","3"]
                            ,["4",".",".","8",".","3",".",".","1"]
                            ,["7",".",".",".","2",".",".",".","6"]
                            ,[".","6",".",".",".",".","2","8","."]
                            ,[".",".",".","4","1","9",".",".","5"]
                            ,[".",".",".",".","8",".",".","7","9"]]
    assert s.isValidSudoku(board)
    board = [["8","3",".",".","7",".",".",".","."]
                            ,["6",".",".","1","9","5",".",".","."]
                            ,[".","9","8",".",".",".",".","6","."]
                            ,["8",".",".",".","6",".",".",".","3"]
                            ,["4",".",".","8",".","3",".",".","1"]
                            ,["7",".",".",".","2",".",".",".","6"]
                            ,[".","6",".",".",".",".","2","8","."]
                            ,[".",".",".","4","1","9",".",".","5"]
                            ,[".",".",".",".","8",".",".","7","9"]]
    assert not s.isValidSudoku(board)
if __name__ == "__main__":
    test()
