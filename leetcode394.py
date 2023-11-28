'''
394. Decode String
s
Given an encoded string, return its decoded string.
The encoding rule is: k[encoded_string], where
the encoded_string inside the square brackets is being repeated exactly k times.
Note that k is guaranteed to be a positive integer.
You may assume that the input string is always valid;
there are no extra white spaces, square brackets are well-formed, etc.
Furthermore, you may assume that the original data does not contain any digits and
that digits are only for those repeat numbers, k.
For example, there will not be input like 3a or 2[4].
The test cases are generated so that the length of the output will never exceed 105.

Example 1:
Input: s = "3[a]2[bc]"
Output: "aaabcbc"

Example 2:
Input: s = "3[a2[c]]"
Output: "accaccacc"

Example 3:
Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
'''
from typing import Any
class Solution:
    # pylint: disable-next=invalid-name
    def decodeString(self, s: str) -> str:
        stack:list[Any] = []
        cd:int=0
        for i in s:
            if i.isdigit():
                cd = cd * 10 + int(i)
            elif i == '[':
                stack.append(cd)
                cd = 0
            elif i == ']':
                #pop until I hit a number
                cs:str = ""
                while True:
                    c = stack.pop()
                    if isinstance(c, int):
                        break
                    cs = c + cs
                stack.append(cs * c)
            else:
                # i is a letter
                stack.append(i)
            #print(stack,cd)
        return ''.join(stack)

def test() -> None:
    s=Solution()
    assert s.decodeString("3[a]2[bc]") == "aaabcbc"
    assert s.decodeString("3[a2[c]]") == "accaccacc"
    assert s.decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef"
    assert s.decodeString("12[a]") == "aaaaaaaaaaaa"

if __name__ == "__main__":
    test()
