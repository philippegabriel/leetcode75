'''
There is a biker going on a road trip. The road trip consists of n + 1 points at different
altitudes. The biker starts his trip on point 0 with altitude equal 0.
You are given an integer array gain of length n where gain[i] 
is the net gain in altitude between points i and i + 1 for all (0 <= i < n).
Return the highest altitude of a point.

Example 1:
Input: gain = [-5,1,5,0,-7]
Output: 1

Example 2:
Input: gain = [-4,-3,-2,-1,4,3,2]
Output: 0
'''
from itertools import accumulate
from typing import List
class Solution:
    # pylint: disable-next=invalid-name
    def largestAltitude(self, gain: List[int]) -> int:
        #accu = 0
        #return max([0]+[accu:=accu+i for i in gain])
        return max(accumulate([0]+gain))

if __name__ == "__main__":
    s=Solution()
    assert s.largestAltitude([-5,1,5,0,-7]) == 1
    assert s.largestAltitude([-4,-3,-2,-1,4,3,2]) == 0
