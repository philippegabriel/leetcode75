'''
547. Number of Provinces
'''
from typing import List
class Solution:
    # pylint: disable-next=invalid-name
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def add_label(index: int, label:int) -> None:
            nonlocal labels, isConnected
            labels[index] = label
            for i,v in enumerate(isConnected[index]):
                if v and not labels[i]:
                    add_label(i, label)

        n:int = len(isConnected)
        labels:list[int] = [0] * n
        for i in range(n):
            if labels[i]:
                continue
            add_label(i, i+1)
        #print(labels)
        result = len(set(labels))
        return result

def test() -> None:
    s=Solution()
    assert s.findCircleNum([[1,1,0],[1,1,0],[0,0,1]]) == 2
    assert s.findCircleNum([[1,0,0],[0,1,0],[0,0,1]]) == 3

if __name__ == "__main__":
    test()
