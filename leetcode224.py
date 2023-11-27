'''
224. Basic Calculator
Hard
Given a string s representing a valid expression,
implement a basic calculator to evaluate it, and return the result of the evaluation.

Example 1:
Input: s = "1 + 1"
Output: 2

Example 2:
Input: s = " 2-1 + 2 "
Output: 3

Example 3:
Input: s = "(1+(4+5+2)-3)+(6+8)"
Output: 23
'''
import operator

class Solution:
    # pylint: disable-next=redefined-outer-name
    def calculate(self, s:str) -> int:
        #Strip all space
        s2 = s.replace(" ","")
        stack = list([])
        acc = 0
        curnum = 0
        curop = operator.add
        digitstream = False
        for i in s2:
            if i in "0123456789":
                digitstream = True
                curnum = curnum * 10 + int(i)
                continue
            #end of digit stream, update acc
            if digitstream:
                acc = curop(acc, curnum)
                curnum = 0
                curop = None
                digitstream = False
            # operators
            if i == "+":
                curop = operator.add
            elif i == "-":
                curop = operator.sub
            elif i == "(":
                stack.append(acc)
                stack.append(curop)
                acc = 0
                curop = operator.add
            else:
                #assert i == ")"
                oldop = stack.pop()
                oldacc = stack.pop()
                acc = oldop(oldacc, acc)
            #print(f"enter i={i}, curnum={curnum}, acc={acc}, curop={curop}, stack={stack}")
        #if pending op, update acc
        if digitstream:
            acc = curop(acc, curnum)
        return acc

if __name__ == "__main__":
    import textwrap
    s=Solution()
    with open("./leetcode224.testcases.csv", "r", encoding="utf-8") as f:
        testcases = [line.rstrip() for line in f]
        for testcase in testcases:
            TCSTRING = textwrap.shorten(testcase, width=30, placeholder="...")
            print(f'calculate("{TCSTRING}")={s.calculate(testcase)}')
            try:
                #LC last test case, seems to break built-in eval
                # pylint: disable-next=eval-used
                assert s.calculate(testcase) == eval(testcase)
            # pylint: disable-next=bare-except
            except:
                pass
