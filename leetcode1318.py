'''
1318. Minimum Flips to Make a OR b Equal to c
Medium
Given 3 positives numbers a, b and c.
Return the minimum flips required in some bits of a and b to make ( a OR b == c ).
(bitwise OR operation).
Flip operation consists of change any single bit 1 to 0
or change the bit 0 to 1 in their binary representation.
'''
class Solution:
    # pylint: disable-next=invalid-name
    def minFlips_slow(self, a: int, b: int, c: int) -> int:
        result = 0
        aorb = a|b
        bit_mask = aorb ^ c
        while bit_mask:
            if bit_mask & 1:
                result += (1^(aorb & 1)) + (a&1) + (b&1)
            bit_mask >>= 1
            a >>= 1
            b >>= 1
            aorb = a | b
        return result

    # pylint: disable-next=invalid-name
    def minFlips(self, a: int, b: int, c: int) -> int:
        return ((a|b) ^ c).bit_count() + (a&b&~c).bit_count()


def test() -> None:
    s=Solution()
    assert s.minFlips(a = 4, b = 2, c = 7) == 1
    assert s.minFlips(a = 1, b = 2, c = 3) == 0
    assert s.minFlips(a = 8, b = 3, c = 5) ==3
if __name__ == "__main__":
    test()
