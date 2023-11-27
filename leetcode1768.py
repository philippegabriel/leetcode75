'''
You are given two strings word1 and word2.
Merge the strings by adding letters in alternating order, starting with word1.
If a string is longer than the other, 
append the additional letters onto the end of the merged string.
Return the merged string.
'''
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result: str = ''
        i:int =0
        len1: int = len(word1)
        len2: int = len(word2)
        while i < len1 or i < len2:
            if i < len1:
                result+=word1[i]
            if i < len2:
                result+=word2[i]
            i+=1
        return result

if __name__ == "__main__":
    s=Solution()
    print(f'1:{s.mergeAlternately(word1 = "abc", word2 = "pqr")}')
    print(f'2:{s.mergeAlternately(word1 = "abc", word2 = "")}')
    print(f'3:{s.mergeAlternately(word1 = "", word2 = "pqr")}')
    print(f'4:{s.mergeAlternately(word1 = "abc", word2 = "pqr012")}')
