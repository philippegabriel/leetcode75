'''
Given an integer array nums, 
return an array answer such that answer[i] is equal to the product of all the elements 
of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''
from typing import List
class Solution:
    # pylint: disable-next=invalid-name
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result:List[int] = []
        prodcons: List[int] = [1]
        prodcdr:List[int] = [1]
        pred:int=1
        for i in nums[:-1]:
            pred *= i
            prodcons.append(pred)
        pred:int=1
        for i in nums[-1:0:-1]:
            pred *= i
            prodcdr.append(pred)
        i = 0
        while prodcdr:
            result.append(prodcdr.pop()*prodcons[i])
            i += 1
        return result

def test() -> None:
    s=Solution()
    assert s.productExceptSelf([1,2,3,4]) == [24,12,8,6]
    assert s.productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]

if __name__ == "__main__":
    test()
