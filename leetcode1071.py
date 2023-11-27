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
class Solution:
    def smallestPattern(self, str: str) -> str:
        #Find the smallest repeating pattern
        len1:int = len(str)
        i:int=1
        nrep:int = 0
        while i < len1:
            nrep:int = int(len1/i)
            # can len(str) divide by i?
            if len1 % i == 0 and str[0:i] * nrep == str:
                break
            i+=1
        # str[0:i] is the smallest repeating pattern
        return str[0:i]

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Deal with outliers
        if len(str1) == 0 or len(str2) == 0:
            return ''
        if str1 == str2:
            return str1
        # Find min len string
        len1,len2 = len(str1), len(str2)
        if len1>len2:
            minStr, maxStr = str2, str1
            minLen, maxLen = len2, len1
        else:
            minStr, maxStr = str1, str2
            minLen, maxLen = len1, len2
        #Find minimal pattern in minStr
        pattern: str = self.smallestPattern(minStr)
        patlen = len(pattern)
        # Check maxStr len can be divide by pattern len
        if maxLen % patlen != 0:
            return ""
        # Check if maxStr is a repeat of pattern
        maxRep: int = int(maxLen / patlen)
        if maxStr != pattern * maxRep:
            return ""
        #Find gcd of maxrep, minRep
        minRep: int = int(minLen / patlen)
        gcdRep: int = gcd(minRep, maxRep) 
        return pattern * gcdRep

if __name__ == "__main__":
    s=Solution()
    print(f'gcdOfStrings("ABCABC","ABC")=>{s.gcdOfStrings("ABCABC","ABC")}')
    print(f'gcdOfStrings("ABABAB","ABAB")=>{s.gcdOfStrings("ABABAB","ABAB")}')
    print(f'gcdOfStrings("ABCBAC","ABC")=>{s.gcdOfStrings("ABCBAC","ABC")}')
    print(s.gcdOfStrings("CDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACA",
                                     "CDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACA"))

