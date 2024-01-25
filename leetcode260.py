'''
260. Single Number III
Medium
Given an integer array nums, in which exactly two elements appear only once
and all the other elements appear exactly twice.
Find the two elements that appear only once. You can return the answer in any order.
You must write an algorithm that runs in linear runtime complexity
and uses only constant extra space.
'''
from typing import List
from functools import reduce
from operator import xor
class Solution:
    # pylint: disable-next=invalid-name
    def singleNumber(self, nums: List[int]) -> List[int]:
        xored_list:int = reduce(xor,nums)
        rb:int=xored_list & (0-xored_list)
        x0:int = reduce(xor,(i for i in nums if i & rb))
        return [x0,xored_list ^ x0]

def test() -> None:
    s=Solution()
    assert s.singleNumber([1,2,1,3,2,5]) == [3,5]
if __name__ == "__main__":
    test()
