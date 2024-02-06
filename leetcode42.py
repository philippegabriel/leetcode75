'''
42. Trapping Rain Water
'''
from typing import List
from itertools import dropwhile
from random import choices
class Solution:
    def trap_maxleft_maxright(self, height: List[int]) -> int:
        result=0
        c=0
        maxleft = [0]+[c:=max(c,i) for i in height[:-1]]
        c=0
        maxright = [0]+[c:=max(c,i) for i in height[:0:-1]]
        maxright.reverse()

        for l,r,h in zip(maxleft,maxright,height):
            result += max(0,min(l,r) - h)
        return result


    def trap_iterate(self, height: List[int]) -> int:
        m=max(height)
        result=0
        for row in range(1,m+1):
            result += sum( dropwhile(lambda x: x,
                    reversed(list(dropwhile(lambda x: x,
                                (h < row for h in height))))
                                ))
        return result

    def trapfsm(self, height: List[int]) -> int:
        m=max(height)
        result=0
        for row in range(1,m+1):
            state:int=0
            curw=0
            for rock in (h >= row for h in height):
            #for rock in dropwhile(lambda x: x,(h >= row for h in height)):
                if not state:
                    if rock:
                        state = 1
                elif state == 1:
                    if rock:
                    #solid block
                        result += curw
                        curw=0
                        state=2
                    else:
                        curw+=1
                else:
                    if not rock:
                        curw +=1
                        state = 1
        return result

def test() -> None:
    s=Solution()
    trap = s.trap_maxleft_maxright
    height = choices(range(10000),k=10732)
    print(trap(height))
    height = [2,0,2]
    assert trap(height) == 2
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    assert trap(height) == 6
    height = [4,2,0,3,2,5]
    assert trap(height) == 9

if __name__ == "__main__":
    test()
