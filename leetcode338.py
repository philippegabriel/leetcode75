'''
338. Counting Bits
Easy
Given an integer n, return an array ans of length n + 1 such that
for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
See: https://oeis.org/A000120
'''
from typing import List
from functools import lru_cache
class Solution:
    # pylint: disable-next=invalid-name
    def countBits(self, n: int) -> List[int]:
        result: List[int] = [0] * (n+1)
        po2s:set[int] = {1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536}
        for i in range(n+1):
            s=sum(int(bool(i & j)) for j in po2s)
            result[i] = s
        return result

    def count_bits_fast(self, n: int) -> List[int]:
        result: List[int] = [0] * (n+2)
        i=0
        end=n//2
        while True:
            t=i<<1
            r=result[i]
            result[t]=r
            result[t+1]=r+1
            if i >= end:
                break
            i+=1
        return result[:n+1]

    def count_ones(self,n:int)-> List[int]:
        if n == 0:
            return [0]
        result: List[int] = [0] * (n+1)
        prev=0
        for i in range(1,n+1):
            result[i] = 1 + result[i & prev]
            prev=i
        return result

    def count_ones_lru(self,n:int)-> List[int]:
        @lru_cache(10)
        def count_ones_cache(n:int) -> int:
            # Base case
            if n == 0:
                return 0
            else:
                # Remove the rightmost 1 and make a recursive call
                return count_ones_cache(n & (n - 1)) + 1
        return [count_ones_cache(i) for i in range(n+1)]

def test() -> None:
    s=Solution()
    print(s.countBits(0))
    print(s.count_ones(0))
    print(s.countBits(1))
    print(s.count_ones(1))
    print(s.countBits(2))
    print(s.count_ones(2))
    print(s.countBits(5))
    print(s.count_ones(5))
    print(s.countBits(16))
    print(s.count_bits_fast(16))
    print(s.count_ones_lru(16))

if __name__ == "__main__":
    test()
