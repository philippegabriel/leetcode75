'''
1004. Max Consecutive Ones III
'''
from typing import List
from collections import deque
class Solution:
    # pylint: disable-next=invalid-name
    def longestOnes(self, nums: List[int], k: int) -> int:
        l=0
        zp:deque[int]=deque()
        #initialise l and r
        for i,num in enumerate(nums):
            if num:
                continue
            #process zero
            if len(zp) == k:
                break
            zp.append(i)
        #Found init sequence
        if i == len(nums)-1:
            return len(nums)
        #l and r are initialised
        #find other sequences
        result = 0
        for r,num in enumerate(nums[i:],i):
            if num:
                continue
            if len(zp) == k:
                result = max(result,r-l)
                #reset l
                l=zp[0]+1
                zp.popleft()
            zp.append(r)
        return result

def test() -> None:
    s=Solution()
    print(s.longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2))
    print(s.longestOnes(nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3))

if __name__ == "__main__":
    test()
