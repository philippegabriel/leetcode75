'''
643. Maximum Average Subarray I
'''
from typing import List
from random import choices
class Solution:
    # pylint: disable-next=invalid-name
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if not nums or not k:
            return 0
        result=tmpsum=sum(nums[0:k])
        for r in range(k,len(nums)):
            tmpsum += nums[r] - nums[r-k]
            result=max(result, tmpsum)
        return result/k

def test() -> None:
    s=Solution()
    assert s.findMaxAverage(nums = [1,12,-5,-6,50,3], k = 4) == 12.75
    assert s.findMaxAverage(nums = [5], k = 1) == 5.0
    assert s.findMaxAverage(nums = [-1], k = 1) == -1.0
    assert s.findMaxAverage(nums = [0,1,1,3,3], k = 4) == 2.0
    k=3000
    nums=choices(range(100),k=k*3)+[1000]*k+choices(range(100),k=k*3)
    assert s.findMaxAverage(nums = nums, k = k) == 1000.0

if __name__ == "__main__":
    test()
