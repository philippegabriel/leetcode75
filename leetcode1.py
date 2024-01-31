'''
67. Add Binary
'''
from typing import List
from bisect import bisect_left
class Solution:
    #0(n log n) solution
    # pylint: disable-next=invalid-name
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        def lookup(nums:List[int],index:int, a:int) -> int:
            'Locate the leftmost value exactly equal to x'
            i = bisect_left(nums, a)
            if i == len(nums):
                return 0
            if nums[i] != a:
                return 0
            if i !=index:
                return 1
            if i+1 != len(nums) and nums[i+1] == a:
                return 2
            return 0

        nums2 = sorted(nums)
        for i,v in enumerate(nums2):
            n = lookup(nums2,i,target-v)
            if not n:
                continue
            #Found it, locate k,l in nums
            k=nums.index(v)
            l=nums.index(target-v,(k+1)*(n-1))
            return [k,l]
        assert False

    #trivial 0(n^2) solution
    # pylint: disable-next=invalid-name
    def twoSum0_n2(self, nums: List[int], target: int) -> List[int]:
        for i,v in enumerate(nums):
            for j,w in enumerate(nums):
                if i == j:
                    continue
                if v+w == target:
                    return [i,j]
        return [-1,-1]


def test() -> None:
    s=Solution()
    assert s.twoSum(nums = [3,2,3], target = 6) == [0,2]
    assert s.twoSum(nums = [2,7,11,15], target = 9) == [0,1]
    assert s.twoSum(nums = [3,2,4], target = 6) == [1,2]
    assert s.twoSum(nums = [3,3], target = 6) == [0,1]

if __name__ == "__main__":
    test()
