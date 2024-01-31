'''
8. String to Integer (atoi)
'''
from typing import List
class Solution:
    # pylint: disable-next=invalid-name
    def myAtoi(self, s: str) -> int:
        i=0
        l=len(s)
        #remove leading white space
        while i<l and s[i] == " ":
            i+=1
        sign=1
        if i == l:
            return 0
        #check for a sign
        if s[i] == '+':
            i+=1
        elif s[i] == '-':
            sign = -1
            i+=1
        #unroll the number string
        #strip leading 0s
        while i<l and s[i] == '0':
            i+=1
        if i==l or not s[i].isdigit():
            return 0
        result = int(s[i]) * sign
        i+=1
        if sign ==1:
            limit = (2**31)-1
        else:
            limit = -(2**31)
        while i<l:
            if not s[i].isdigit():
                break
            di=int(s[i]) * sign
            if sign == 1:
                if result >= (limit - di) / 10:
                    return limit
            else:
                if result <= (limit - di) / 10:
                    return limit
            result = (result *10) + di
            i+=1
        return result

def test() -> None:
    s=Solution()
    print(s.myAtoi("000000000000000000000000000011"))
    print(s.myAtoi("+"))
    print(s.myAtoi(""))
    print(s.myAtoi("+-12"))
    print(s.myAtoi("987and"))
    print(s.myAtoi("words and 987"))
    print(s.myAtoi('42'))
    print(s.myAtoi('-42'))
    print(s.myAtoi('2147483646'))
    print(s.myAtoi('2147483647'))
    print(s.myAtoi('2147483648'))
    print(s.myAtoi('-2147483647'))
    print(s.myAtoi('-2147483648'))
    print(s.myAtoi('-2147483649'))

if __name__ == "__main__":
    test()
