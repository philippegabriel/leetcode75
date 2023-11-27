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
from typing import List, Optional
class Solution:
    # pylint: disable-next=invalid-name
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        fz:Optional[int] = None
        nz: int = 0
        for i,num in enumerate(nums):
            if num == 0:
                if nz == 0:
                    fz = i
                nz += 1
            elif nz != 0:
                assert fz is not None
                nums[fz] = num
                nums[i] = 0
                fz = i + 1 - nz

if __name__ == "__main__":
    s=Solution()

    input_list = [0,0,1,1,0,1]
    print(f"moveZeroes({input_list}) =>",end='')
    s.moveZeroes(input_list)
    print(input_list)
    assert input_list == [1,1,1,0,0,0]

    input_list = [0,1,0,3,12]
    print(f"moveZeroes({input_list}) =>",end='')
    s.moveZeroes(input_list)
    print(input_list)
    assert input_list == [1,3,12,0,0]
