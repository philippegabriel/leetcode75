'''
11. Container With Most Water
'''
from typing import List
class Solution:
    # pylint: disable-next=invalid-name
    def maxArea(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0
        l=0
        length=r=len(height)-1
        maxh=0
        while length:
            maxh=max(maxh,min(a:=height[l],b:=height[r])*length)
            #print(f'{l=},{r=},{height[l]=},{height[r]=},{cur=},{maxh}')
            if a > b:
                r-=1
            else:
                l+=1
            length -=1
        return maxh


def test() -> None:
    s=Solution()
    print(s.maxArea(height = [1,3,2,5,25,24,5]))
    print(s.maxArea(height = [1,8,6,2,5,4,8,3,7]))
    print(s.maxArea(height = [1,1]))
if __name__ == "__main__":
    test()
