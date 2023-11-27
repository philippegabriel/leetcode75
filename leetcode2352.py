'''
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) 
such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order 
(i.e., an equal array).
'''
from typing import List, TypeAlias
from collections import Counter
gridtem:TypeAlias = tuple[int,...]
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n:int=len(grid)
        cRowHash:Counter[gridtem] = Counter(tuple(l) for l in grid)
        cRowCol:Counter[gridtem] = Counter([])
        for t in (tuple([grid[j][i] for j in range(n)]) for i in range(n)):
            if t in cRowHash:
                cRowCol.update([t])

        total = 0
        for i,s in cRowCol.items():
            total+= cRowHash[i] * s
        return total

if __name__ == "__main__":
    s=Solution()
    print(s.equalPairs([[3,2,1],[1,7,6],[2,7,7]]))
    print(s.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))
    print(s.equalPairs([[11,1],[1,11]]))
