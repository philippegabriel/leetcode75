'''
1431. Kids With the Greatest Number of Candies
Easy
There are n kids with candies.
You are given an integer array candies, where each candies[i] represents
the number of candies the ith kid has,
and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if,
after giving the ith kid all the extraCandies,
they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.

Example 1:
Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true] 
'''
from typing import List

class Solution:
    # pylint: disable-next=[invalid-name, redefined-outer-name]
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies:int = max(candies)
        return [bool(i+extraCandies >= max_candies) for i in candies]

def test() -> None:
    s=Solution()
    result:List[bool] = s.kidsWithCandies(candies=[4,2,1,1,2], extraCandies = 1)
    print(result)
    assert result == [True, False, False, False, False]

    s=Solution()
    result:List[bool] = s.kidsWithCandies(candies=[12,1,12], extraCandies = 10)
    print(result)
    assert result == [True, False, True]

if __name__ == "__main__":
    test()
