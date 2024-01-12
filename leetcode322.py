'''
322. Coin Change
Medium
You are given an integer array coins representing coins of different denominations
and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0
'''
from typing import List
from functools import cache
MAXAMOUNT=10001
class Solution:
    # pylint: disable-next=invalid-name
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def coin_change_rec(amount:int) -> int:
            nonlocal coins, min_coin
            if amount == 0:
                return 0
            if amount < min_coin:
                return MAXAMOUNT
            if amount in coins:
                return 1
            return 1+min((coin_change_rec(amount-i) for i in coins))
        min_coin = min(coins)
        result = coin_change_rec(amount)
        return -1 if result >= MAXAMOUNT else result

def test() -> None:
    s=Solution()
    assert s.coinChange(coins = [1,2,5], amount = 11) == 3
    assert s.coinChange(coins = [2], amount = 3) == -1
    assert s.coinChange(coins = [1], amount = 0) == 0

if __name__ == "__main__":
    test()
