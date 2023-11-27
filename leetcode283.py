'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order
of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]

'''
from typing import Optional
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        fz:Optional[int] = None
        nz: int = 0
        lnumsRange = range(len(nums))
        for i in lnumsRange:
            if nums[i] == 0:
                if nz == 0:
                    fz = i
                nz += 1
            elif nz != 0:
                assert fz != None
                nums[fz] = nums[i]
                nums[i] = 0
                fz = i + 1 - nz
        
if __name__ == "__main__":
    s=Solution()
    inputs = [
        [0,0,1,1,0,1],
        [0,1,0,3,12]
        ]
    for i in inputs:       
        print(f"moveZeroes({i}) =>",end='')
        s.moveZeroes(i)
        print(i)

