'''
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) 
such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order 
(i.e., an equal array).
'''
from typing import List, TypeAlias
from collections import Counter
GridItem:TypeAlias = tuple[int,...]
class Solution:
    # pylint: disable-next=invalid-name
    def equalPairs(self, grid: List[List[int]]) -> int:
        n:int=len(grid)
        c_row_hash:Counter[GridItem] = Counter(tuple(l) for l in grid)
        c_row_col:Counter[GridItem] = Counter([])
        for t in (tuple((grid[j][i] for j in range(n))) for i in range(n)):
            if t in c_row_hash:
                c_row_col.update([t])

        total = 0
        for i,item in c_row_col.items():
            total+= c_row_hash[i] * item
        return total

if __name__ == "__main__":
    s=Solution()
    assert s.equalPairs([[3,2,1],[1,7,6],[2,7,7]]) == 1
    assert s.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]) == 3
    assert s.equalPairs([[11,1],[1,11]]) == 2
