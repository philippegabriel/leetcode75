'''
2746. Min Cost Climbing Stairs
You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.

Example 1:
Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

Example 2:
Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.
'''
from functools import cache
from typing import List
class Solution:
    # pylint: disable-next=invalid-name
    def minCostClimbingStairs_recurse(self, cost: List[int]) -> int:
        @cache
        def minCost(i:int) -> int:
            nonlocal cost, len_cost
            if i in (0,1):
                return cost[i]
            return min(minCost(i-1),
                        minCost(i-2)) +  (0 if i == len_cost else cost[i])
        len_cost = len(cost)
        return minCost(len_cost)
    #
    #Iterative
    # pylint: disable-next=invalid-name
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        step = len(cost)
        acc = 0
        while step >= 2:
            s1, s2 = cost[step-1], cost[step-2]
            step-=1
            if s1 < s2:
                acc +=s1
            else:
                step-=1
                acc+=s2
        return acc

def test() -> None:
    s = Solution()
    print(s.minCostClimbingStairs([10,15,20]))
    s = Solution()
    print(s.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))
if __name__ == "__main__":
    test()
