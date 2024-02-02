'''
3. Longest Substring Without Repeating Characters
'''
class Solution:
    # pylint: disable-next=invalid-name
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        maxlen:int=0
        #maxstart:int=0
        #maxend:int=0
        curend=0
        curstart=0
        seen:set[str]=set()
        max_possible = len(set(s))
        for curend,c in enumerate(s):
            if c not in seen:
                seen.add(c)
                if curend-curstart+1 == max_possible:
                    return max_possible
                continue
            #c is in seen
            #check for new max
            if curend-curstart > maxlen:
                #maxstart,maxend=curstart,curend
                maxlen=curend-curstart
            #reset start
            for j in s[curstart:curend]:
                seen.remove(j)
                curstart+=1
                if j==c:
                    break
            seen.add(c)
        curend+=1
        if curend-curstart > maxlen:
            maxlen = curend-curstart
        #print(s,'->',curstart,curend,maxstart,maxend,s[maxstart:maxend])
        return maxlen

def test() -> None:
    s=Solution()
    assert s.lengthOfLongestSubstring(s = "aab") == 2
    assert s.lengthOfLongestSubstring(s = "abcabcbb") ==3
    assert s.lengthOfLongestSubstring(s = "pwwkew") == 3
    assert s.lengthOfLongestSubstring(s = "123456789") == 9
    assert not s.lengthOfLongestSubstring(s = "")
if __name__ == "__main__":
    test()
