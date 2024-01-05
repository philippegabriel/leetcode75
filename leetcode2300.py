'''
2300. Successful Pairs of Spells and Potions
Medium
You are given two positive integer arrays spells and potions, of length n and m respectively,
where spells[i] represents the strength of the ith spell and potions[j]
represents the strength of the jth potion.

You are also given an integer success.
A spell and potion pair is considered successful if the product of their strengths
is at least success.

Return an integer array pairs of length n where pairs[i] is the number of potions
that will form a successful pair with the ith spell.

Example 1:
Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
Output: [4,0,3]
Explanation:
- 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25]. 4 pairs are successful.
- 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
- 2nd spell: 3 * [1,2,3,4,5] = [3,6,9,12,15]. 3 pairs are successful.
Thus, [4,0,3] is returned.
'''
from typing import List
from bisect import bisect_left
from functools import cache
from math import ceil
class Solution:
    # pylint: disable-next=invalid-name
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        @cache
        def process_row(threshold:int) -> int:
            nonlocal potions, potion_len
            return potion_len - bisect_left(potions,threshold)
        potion_len = len(potions)
        potions.sort()
        #self.sorted_potions:tuple[int,...] = tuple(sorted(potions))
        result:List[int] = []
        for i in spells:
            threshold = ceil (success/i)
            n = process_row(threshold)
            result.append(n)
        return result

def test() -> None:
    s = Solution()
    spells = [5,1,3]
    potions = [1,2,3,4,5]
    success = 7
    output = [4,0,3]
    #print(s.successfulPairs(spells, potions, success))
    assert s.successfulPairs(spells, potions, success) == output
    s = Solution()
    spells = [3,1,2]
    potions = [8,5,8]
    success = 16
    output = [2,0,2]
    #print(s.successfulPairs(spells, potions, success))
    assert s.successfulPairs(spells, potions, success) == output

if __name__ == "__main__":
    test()
