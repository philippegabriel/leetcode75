'''
216. Combination Sum III
Medium
5.6K
102
Companies
Find all valid combinations of k numbers that sum up to n such that the
following conditions are true:

Only numbers 1 through 9 are used.
Each number is used at most once.
Return a list of all possible valid combinations.
The list must not contain the same combination twice,
and the combinations may be returned in any order.

Example 1:
Input: k = 3, n = 7
Output: [[1,2,4]]
Explanation:
1 + 2 + 4 = 7
There are no other valid combinations.

Example 2:
Input: k = 3, n = 9
Output: [[1,2,6],[1,3,5],[2,3,4]]
Explanation:
1 + 2 + 6 = 9
1 + 3 + 5 = 9
2 + 3 + 4 = 9
There are no other valid combinations.

Example 3:
Input: k = 4, n = 1
Output: []
Explanation: There are no valid combinations.
Using 4 different numbers in the range [1,9],
the smallest sum we can get is 1+2+3+4 = 10 and since 10 > 1,
there are no valid combination.

Constraints:
2 <= k <= 9
1 <= n <= 60
'''
from typing import List
class Solution:
    def __init__(self):
        self.result: set[frozenset[int]] = set()

    def backtrack(self, k:int, n: int, acc: set[int]):
        if n < 0:
            return
        if n==0:
            if k == 0:
                self.result.add(frozenset(acc))
            return
        for i in [i for i in range(1,10) if i not in acc]:
            self.backtrack(k-1, n-i, acc | {i})


    # pylint: disable-next=invalid-name
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.backtrack(k,n,set())
        return [list(i) for i in self.result]


def test()->None:
    s=Solution()
    result=s.combinationSum3(3,7)
    print(result)
    assert result == [[1,2,4]]
    s=Solution()
    result=s.combinationSum3(3,9)
    print(result)
    assert result == [[1, 3, 5], [1, 2, 6], [2, 3, 4]]
    s=Solution()
    result=s.combinationSum3(4,1)
    print(result)
    assert result == []


if __name__ == "__main__":
    test()
