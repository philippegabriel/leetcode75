'''
For two strings s and t, we say "t divides s" if and only if s = t + ... + t 
(i.e., t is concatenated with itself one or more times).
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
 

Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.
'''
from math import gcd
import textwrap
class Solution:
    # pylint: disable-next=redefined-outer-name
    def smallest_pattern(self, s: str) -> str:
        len1:int = len(s)
        i:int=1
        nrep:int = 0
        while i < len1:
            nrep:int = int(len1/i)
            # can len(str) divide by i?
            if len1 % i == 0 and s[0:i] * nrep == s:
                break
            i+=1
        # str[0:i] is the smallest repeating pattern
        return s[0:i]

    # pylint: disable-next=invalid-name
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """solution for leetcode 735"""
        # Deal with outliers
        if len(str1) == 0 or len(str2) == 0:
            return ''
        if str1 == str2:
            return str1
        # Find min len string
        len1,len2 = len(str1), len(str2)
        if len1>len2:
            min_str, max_str = str2, str1
            min_len, max_len = len2, len1
        else:
            min_str, max_str = str1, str2
            min_len, max_len = len1, len2
        #Find minimal pattern in minStr
        pattern: str = self.smallest_pattern(min_str)
        patlen = len(pattern)
        # Check maxStr len can be divide by pattern len
        if max_len % patlen != 0:
            return ""
        # Check if maxStr is a repeat of pattern
        max_rep: int = int(max_len / patlen)
        if max_str != pattern * max_rep:
            return ""
        #Find gcd of maxrep, minRep
        min_rep: int = int(min_len / patlen)
        gcd_rep: int = gcd(min_rep, max_rep)
        return pattern * gcd_rep

if __name__ == "__main__":
    s=Solution()
    print(f'gcdOfStrings("ABCABC","ABC")=>{s.gcdOfStrings("ABCABC","ABC")}')
    print(f'gcdOfStrings("ABABAB","ABAB")=>{s.gcdOfStrings("ABABAB","ABAB")}')
    print(f'gcdOfStrings("ABCBAC","ABC")=>{s.gcdOfStrings("ABCBAC","ABC")}')
    with open("./leetcode1071.csv", "r", encoding="utf-8") as f:
        testcases = [line.rstrip() for line in f]
        while testcases:
            INPUT0 = testcases.pop(0)
            INPUT1 = testcases.pop(0)
            INPUTSTR0 = textwrap.shorten(INPUT0, width=30, placeholder="...")
            INPUTSTR1 = textwrap.shorten(INPUT1, width=30, placeholder="...")
            print(f'gcdOfStrings({INPUTSTR0}, {INPUTSTR1})=>{s.gcdOfStrings(INPUT0,INPUT1)}')
