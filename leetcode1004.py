'''
1004. Max Consecutive Ones III
'''
from typing import List
from collections import deque
class Solution:
    # pylint: disable-next=invalid-name
    def longestOnes(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        l=0
        zp:deque[int]=deque()
        result = 0
        for r,num in enumerate(nums):
            if not num:
                zp.append(r)
                if len(zp) == k+1:
                    #reset l
                    l=zp[0]+1
                    zp.popleft()
            result = max(result,r-l+1)
        return result

def test() -> None:
    s=Solution()
    assert s.longestOnes(nums = [], k = 2) == 0
    assert s.longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2) == 6
    assert s.longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 0) == 4
    assert s.longestOnes(nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3) == 10
    assert s.longestOnes(nums = [1]*100, k = 3) == 100

if __name__ == "__main__":
    test()
