'''
198. House Robber
Medium
Topics
Companies
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint
stopping you from robbing each of them is that adjacent houses have security
systems connected and it will automatically contact the police if two adjacent
houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house,
return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
'''
from functools import cache
from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        @cache
        def rob_rec(i:int) -> int:
            nonlocal nums
            if i < 0:
                return 0
            if i == 0:
                return nums[0]
            return max(nums[i]+rob_rec(i-2),nums[i-1]+rob_rec(i-3))
        return rob_rec(len(nums)-1)

def test() -> None:
    s = Solution()
    assert s.rob([1,2,3,1]) == 4
    assert s.rob([2,7,9,3,1]) == 12
    assert s.rob([1,2]) == 2
    assert s.rob([1,7,9,2]) ==10
  
if __name__ == "__main__":
    test()
