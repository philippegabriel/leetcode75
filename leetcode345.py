'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases,
more than once.

Example 1:
Input: s = "hello"
Output: "holle"

Example 2:
Input: s = "leetcode"
Output: "leotcede"
'''
class Solution:
    """solution for leetcode 345"""
    vowelset:set[str] = {'a','e','i','o','u', 'A', 'E', 'I', 'O', 'U'}
    # pylint: disable-next=[invalid-name, redefined-outer-name]
    def reverseVowels(self, s: str) -> str:
        """solution for leetcode 345"""
        lp:int = 0
        rp:int = len(s) -1
        try:
            while rp > lp:
                #find leftmost vowel
                while s[lp] not in self.vowelset:
                    lp += 1
                    if rp <= lp:
                        raise IndexError
                #find rightmost vowel
                while s[rp] not in self.vowelset:
                    rp -= 1
                    if rp <= lp:
                        raise IndexError
                s=s[:lp]+s[rp]+s[lp+1:rp]+s[lp]+s[rp+1:]
                lp +=1
                rp -=1
        except IndexError:
            pass
        return s

if __name__ == "__main__":
    s=Solution()
    print(s.reverseVowels("hello"))
    print(s.reverseVowels("leetcode"))
    print(s.reverseVowels("Yo! Bottoms up, U.S. Motto, boy!"))
