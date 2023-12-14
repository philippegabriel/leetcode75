'''
334. Increasing Triplet Subsequence
Medium
7.6K
417
Companies
Given an integer array nums, return true if there exists a triple of indices (i, j, k)
such that i < j < k and nums[i] < nums[j] < nums[k].
If no such indices exists, return false.

Example 1:
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

Example 2:
Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.

Example 3:
Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.'''
from typing import List

class Solution:
    # pylint: disable-next=[invalid-name, redefined-outer-name]
    def increasingTriplet(self, nums: List[int]) -> bool:
        #Create list of rightmost max values
        n = len(nums)
        rightmax:List[int] = [0 for _ in range(n)]
        max_val = nums[-1]
        for i in range(n-2,0,-1):
            max_val = max(max_val, nums[i+1])
            rightmax[i] = max_val
        #print(nums)
        #print(rightmax)
        # Walk the list, maintain max left and check if current value is ok
        min_val = nums[0]
        for i,m in zip(nums[1:n],rightmax[1:n]):
            if min_val < i < m:
                #print(f'{min_val=} < {i=} < {m=}')
                return True
            min_val = min(min_val,i)
            #print(f'SKIP {min_val=} < {i=} < {m=}')
        return False

def test() -> None:
    s=Solution()
    result = s.increasingTriplet([1,2,3,4,5])
    assert result

    s=Solution()
    result = s.increasingTriplet([5,4,3,2,1])
    assert not result

    s=Solution()
    result = s.increasingTriplet([2,1,5,0,4,6])
    assert result

    s=Solution()
    result = s.increasingTriplet([20,100,10,12,5,13])
    assert result

    s=Solution()
    result = s.increasingTriplet([1,2,1,3])
    assert result

    s=Solution()
    result = s.increasingTriplet([1,5,0,4,1,3])
    assert result

    s=Solution()
    result = s.increasingTriplet([1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])
    assert not result

    s=Solution()
    result = s.increasingTriplet([1,0,-1,0,100000000])
    assert result

    s=Solution()
    result = s.increasingTriplet([4,5,2147483647,1,2])
    assert result

if __name__ == "__main__":
    test()
