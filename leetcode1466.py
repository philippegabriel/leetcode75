'''
1466. Reorder Routes to Make All Paths Lead to the City Zero
'''
from typing import List
from collections import defaultdict, deque
class Solution:
    # pylint: disable-next=invalid-name
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        #build adjacency list
        al: defaultdict[int,set[tuple[int,...]]] = defaultdict(set)
        for row in connections:
            al[row[0]].add((row[1],1))
            al[row[1]].add((row[0],0))
        #build the set of vertices
        vertices:set[int]=set(al.keys())
        #DFS
        flipped_edge = 0
        colors:deque[int] = deque([0])
        while colors:
            vertex:int = colors.popleft()
            vertices.discard(vertex)
            for i,v in al[vertex]:
                if i not in vertices:
                    continue
                # if tuple([i,vertex]) not in edges:
                #     print(f'cant find {i}->{vertex}, found in al:{i=},{v=}')
                # else:
                #     print(f'FOUND {i}->{vertex}')
                flipped_edge += v
                colors.append(i)
        return flipped_edge

def test() -> None:
    s=Solution()
    assert s.minReorder(6,[[0,1],[1,3],[2,3],[4,0],[4,5]]) == 3
    assert s.minReorder(5,[[1,0],[1,2],[3,2],[3,4]]) == 2
    assert s.minReorder(3,[[1,0],[2,0]]) == 0
if __name__ == "__main__":
    test()
