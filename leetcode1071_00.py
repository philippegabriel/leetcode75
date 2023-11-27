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
from collections import Counter
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1:int=len(str1)
        len2:int=len(str2)
        c1: Counter[str] = Counter(str1)
        c2: Counter[str] = Counter(str2)
        npat1: int=min(*c1.values())
        npat2: int=min(*c2.values())
        patlen1: int = int(len1/npat1)
        patlen2: int = int(len2/npat2)
        totalgcd:int = gcd(npat1,npat2) * patlen1
        print(c1,"\n",c2,"\n",patlen1,patlen2,npat1,npat2,totalgcd)
        #Check same pattern len
        if patlen1 != patlen2:
            return ""
        #Check same pattern
        pattern:str = str1[0:patlen1]
        if str2[0:patlen2] != pattern:
            return ""
        #Check each string is made of same concatenated pattern
        reppat1 = pattern * npat1
        reppat2 = pattern * npat2
        if str2 != reppat2:
            return "fail2"
        if str1 != reppat1:
            return "fail1"
        return str1[0:totalgcd]
if __name__ == "__main__":
    s=Solution()
    #print(f'gcdOfStrings("ABCABC","ABC")=>{s.gcdOfStrings("ABCABC","ABC")}')
    #print(f'gcdOfStrings("ABABAB","ABAB")=>{s.gcdOfStrings("ABABAB","ABAB")}')
    #print(f'gcdOfStrings("ABCBAC","ABC")=>{s.gcdOfStrings("ABCBAC","ABC")}')
    print(s.gcdOfStrings("CDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACA",
                                     "CDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACACDDCADCCDDBABCCCDACA"))

