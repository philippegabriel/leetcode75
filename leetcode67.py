'''
67. Add Binary
'''
from typing import Literal
from itertools import zip_longest
class Solution:
    # pylint: disable-next=invalid-name
    def addBinaryIter(self, a: str, b: str) -> str:
        result:str=''
        c:int=0
        for i,j in zip_longest(reversed(a),reversed(b),fillvalue='0'):
            s:int=int(i)+int(j)+c
            c = (s & 0b10) >> 1
            s &= 0b01
            result = str(s)+result
        if c:
            result = '1'+result
        return result

    def addBinaryFast(self, a: str, b: str) -> str:
        s=int(a,base=2)+int(b,base=2)
        result:str=''
        while s:
            result = str(s&1) + result
            s >>= 1
        return result if result else '0'

    def addBinary(self, a: str, b: str) -> str:
        return f'{(int(a,base=2)+int(b,base=2)):b}'

def test() -> None:
    s=Solution()
    assert s.addBinary(a = "11", b = "1") == '100'
    assert s.addBinary(a = "1010", b = "1011") == '10101'
    assert s.addBinary(a = "0", b = "0") == '0'

if __name__ == "__main__":
    test()
