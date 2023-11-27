'''
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.

Example 1:
Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]

Example 2:
Input: nums1 = [1,2,3,3], nums2 = [1,1,2,2]
Output: [[3],[]]
'''

class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        s1:set[int] = set(nums1)
        s2:set[int] = set(nums2)
        return[list(s1-s2),list(s2-s1)]

        
if __name__ == "__main__":
    s=Solution()
    print(s.findDifference([1,2,3], [2,4,6]))
    print(s.findDifference(nums1 = [1,2,3,3], nums2 = [1,1,2,2]))
