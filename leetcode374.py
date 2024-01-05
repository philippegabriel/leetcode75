'''
374. Guess Number Higher or Lower
Easy
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or 
lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.

Example 1:

Input: n = 10, pick = 6
Output: 6
'''
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
pick: int =0
def guess(num: int) -> int:
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:
        return 0


class Solution:
    # pylint: disable-next=invalid-name
    def guessNumber(self, n: int) -> int:
        min_int: int = 1
        max_int: int = n
        while True:
            guess_int:int = min_int + (max_int-min_int) // 2
            #print(f"{min_int=},{max_int=},{guess_int=}")
            result = guess(guess_int)
            if result == 0:
                return guess_int
            elif result == -1:
                max_int = guess_int - 1
            else:
                min_int = guess_int + 1

def test() -> None:
    # pylint: disable-next=global-statement
    global pick
    s=Solution()
    pick = 6
    assert pick == s.guessNumber(10)
    pick = 1
    assert pick == s.guessNumber(1)
    pick = 1
    assert pick == s.guessNumber(2)
    pick = 77
    assert pick == s.guessNumber(100)
    pick = 2
    assert pick == s.guessNumber(2)

if __name__ == "__main__":
    test()
