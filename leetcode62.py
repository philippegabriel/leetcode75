'''
62. Unique Paths
Medium
There is a robot on an m x n grid. 
The robot is initially located at the top-left corner (i.e., grid[0][0]).
The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths
that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.
'''
from math import factorial
class Solution:
    # pylint: disable-next=invalid-name
    def uniquePaths(self, m: int, n: int) -> int:
        return int(factorial(m+n-2)/(factorial(m-1)*factorial(n-1)))
def test() -> None:
    s=Solution()
    assert s.uniquePaths(m = 3, n = 7) == 28
    assert s.uniquePaths(m = 3, n = 2) == 3

if __name__ == "__main__":
    test()
