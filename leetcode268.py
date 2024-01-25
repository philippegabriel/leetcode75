'''
268. Missing Number
Given an array nums containing n distinct numbers in the range [0, n]
return the only number in the range that is missing from the array.
'''
from typing import List
class Solution:
    # pylint: disable-next=invalid-name
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        return int(n*(n+1)/2)-sum(nums)

def test() -> None:
    s=Solution()
    assert s.missingNumber([3,0,1]) == 2
    assert s.missingNumber([0,1]) == 2
    assert s.missingNumber([9,6,4,2,3,5,7,0,1]) == 8
if __name__ == "__main__":
    test()
