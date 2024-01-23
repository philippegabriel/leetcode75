'''
136. Single Number
'''
from typing import List
class Solution:
    # pylint: disable-next=invalid-name
    def singleNumber(self, nums: List[int]) -> int:
        found = bytearray(2**13)
        for i in nums:
            i+=0x8000
            index = i >> 3
            bitset = 1 << (i & 0b111)
            found[index] ^= bitset
        for index,i in enumerate(found):
            if i:
                break
        rank=[1, 2, 4, 8, 16, 32, 64, 128].index(i)
        num = ((index << 3 ) | rank) - 0x8000
        return num

def test() -> None:
    s=Solution()
    print(s.singleNumber([2,2,1]))
    print(s.singleNumber([4,1,2,1,2]))
    print(s.singleNumber([1]))
    print(s.singleNumber([-1]))
if __name__ == "__main__":
    test()
