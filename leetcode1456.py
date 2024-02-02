'''
1456. Maximum Number of Vowels in a Substring of Given Length
'''
class Solution:
    # pylint: disable-next=invalid-name
    def maxVowels(self, s: str, k: int) -> int:
        if k == 0:
            return 0
        vowels:frozenset[str]=frozenset(('a', 'e', 'i', 'o', 'u'))
        #init counter
        result = seen = sum((int(i in vowels) for i in s[:k]))
        if result ==k:
            return k
        for i,j in zip(s[k:],s[:-k]):
            seen += int(i in vowels) - int(j in vowels)
            if seen == k:
                return k
            result=max(result,seen)
        return result

    # pylint: disable-next=invalid-name
    def maxVowels00(self, s: str, k: int) -> int:
        vowels:frozenset[str]=frozenset(('a', 'e', 'i', 'o', 'u'))
        l=[int(i in vowels) for i in s]
        #init counter
        result = seen = sum(l[:k])
        if result == k:
            return k
        for i,j in zip(l[k:],l[:-k]):
            seen += i-j
            if seen == k:
                return k
            result=max(result,seen)
        return result

def test() -> None:
    s=Solution()
    assert s.maxVowels(s = "abciiidef", k = 3)  == 3
    assert s.maxVowels(s = "aeiou", k = 2) == 2
    assert s.maxVowels(s = "leetcode", k = 3) == 2

if __name__ == "__main__":
    test()
