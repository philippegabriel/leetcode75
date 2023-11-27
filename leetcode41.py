''''
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.
'''
import heapq
from typing import List
class Solution:
    # pylint: disable-next=invalid-name
    def firstMissingPositive(self, nums: List[int]) -> int:
        hq = []
        for i in nums:
            heapq.heappush(hq,i)
        i:int = 0
        j:int = -1
        while j < 1:
            try:
                j = heapq.heappop(hq)
            except IndexError:
                return 1
        # i=0,j >= 1
        while j - i <= 1:
            i = j
            try:
                j = heapq.heappop(hq)
            except IndexError:
                break
        return i+1

if __name__ == "__main__":
    s=Solution()
    assert s.firstMissingPositive([1,2,0]) == 3
    assert s.firstMissingPositive([3,4,-1,1]) == 2
    assert s.firstMissingPositive([7,8,9,11,12]) == 1
