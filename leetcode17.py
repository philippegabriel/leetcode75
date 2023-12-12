'''
17. Letter Combinations of a Phone Number
Medium
Given a string containing digits from 2-9 inclusive,
return all possible letter combinations that the number could represent.
Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below.
Note that 1 does not map to any letters.

Example 1:
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
Input: digits = ""
Output: []

Example 3:
Input: digits = "2"
Output: ["a","b","c"]
'''
from typing import List
class Solution:

    def __init__(self) -> None:
        self.d2a_map: dict[str,str] = \
        {'2':'abc',
         '3':'def',
         '4':'ghi',
         '5':'jkl',
         '6':'mno',
         '7':'pqrs',
         '8':'tuv',
         '9':'wxyz'}
        self.acc:List[str]=[]

    def backtrack(self, a:list[str], b:str, c:int) -> None:
        #print(a)
        if len(b) == c and c>0:
            self.acc.append(b)
        if not a:
            return
        for i,v in enumerate(a):
            #pick a set
            #pick a str from the set
            for j in v:
                self.backtrack(a[i+1:], b+j,c)

    # pylint: disable-next=[invalid-name]
    def letterCombinations(self, digits: str) -> List[str]:
        init_list = [self.d2a_map[i] for i in digits]
        self.backtrack(init_list,'',len(digits))
        return self.acc

def test()->None:
    s=Solution()
    result=s.letterCombinations("23")
    print(result)
    assert result == ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
    s=Solution()
    result = s.letterCombinations("")
    print(result)
    assert not result

if __name__ == "__main__":
    test()
