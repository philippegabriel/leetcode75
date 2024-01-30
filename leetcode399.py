'''
399. Evaluate Division
'''
from typing import List, TypeAlias
from collections import deque
Edge: TypeAlias=tuple[str,str]
class Solution:
    # pylint: disable-next=invalid-name
    def calcEquation(self,
                     equations: List[List[str]],
                     values: List[float],
                     queries: List[List[str]]) -> List[float]:
        al:dict[Edge,float] = dict()
        nl: set[str] = set()
        #populate nl
        for i,j in equations:
            nl.add(i)
            nl.add(j)
        #Add initial & reciprocal edges
        for (i,j), v in zip(equations, values):
            al[(i,j)] = v
            al[(j,i)] = 1/v
        #Add id edges
        for i in nl:
            al[(i,i)] = 1
        #print(f'Finished Init-{al=}')
        #Add remaining edges
        for node in nl:
            processed_edges:set[Edge]=set()
            rs:deque[Edge] = deque()
            for i,j in al:
                if i == node and i!=j:
                    rs.append((i,j))
            while rs:
                #print(f'===Init:Node:{node=},{rs=}===')
                i,j = rs.popleft()
                if node == j:
                    continue
                newedge = (node,j)
                #print(f'{newedge=}', end='')
                if newedge not in al:
                    al[newedge]= al[(node,i)] * al[(i,j)]
                    #print(f'Adding {newedge=}={al[newedge]}')
                #else:
                    #print('NOT Adding')
                processed_edges.add((i,j))
                for k,l in al:
                    if k!=l and j == k and (k,l) not in processed_edges:
                        rs.append((k,l))
                #print(f'Loop:{rs=}')
            #print(al)
        #Add id edges
        # for i in nl:
        #     al[(i,i)] = 1
        #print(f'Finished Init{al=}')
        #resolve queries
        result:List[float]=[]
        for i in queries:
            edge:Edge=(i[0],i[1])
            if edge in al:
                result.append(al[edge])
            else:
                result.append(-1)
        return result

def test() -> None:
    s=Solution()
    assert not s.calcEquation([],[],[])
    equations  = [["a","b"],["b","c"]]
    values = [2.0,3.0]
    queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    s=Solution()
    result = s.calcEquation(equations, values, queries)
    assert result  ==  [6.0, 0.5, -1, 1, -1]
    equations = [["a","b"],["b","c"],["bc","cd"]]
    values = [1.5,2.5,5.0]
    queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
    s=Solution()
    assert s.calcEquation(equations, values , queries) == [3.75, 0.4, 5.0, 0.2]
    equations = [["a","e"],["b","e"]]
    values = [4.0,3.0]
    queries = [["a","b"],["e","e"],["x","x"]]
    s=Solution()
    assert s.calcEquation(equations, values, queries) == [1.3333333333333333, 1.0, -1]

if __name__ == "__main__":
    test()
