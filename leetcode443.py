'''
443. String Compression
'''
from typing import List
class Solution:
    def compress(self, chars: List[str]) -> int:
        prev=chars[0]
        nw=0
        ccount=1
        chars.append('')
        for i in chars[1:]:
            if i == prev:
                ccount+=1
                continue
            #write char
            chars[nw]=prev
            nw+=1
            prev=i
            #write count
            if ccount>1:
                scount=str(ccount)
                prevnw,nw=nw,nw+len(scount)
                chars[prevnw:nw] = list(scount)
            ccount=1
        return nw

def test() -> None:
    s=Solution()
    chars=["a","a","b","b","c","c","c"]
    l=s.compress(chars)
    #print(f'{l=}, {chars[:l]=}')
    assert l == 6
    chars=["a"]
    l=s.compress(chars)
    #print(f'{l=}, {chars[:l]=}')
    assert l == 1
    chars=["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    l=s.compress(chars)
    #print(f'{l=}, {chars[:l]=}')
    assert l == 4

if __name__ == "__main__":
    test()
