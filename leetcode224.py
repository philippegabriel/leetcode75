#224. Basic Calculator
#Hard
#Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.
#Example 1:
#Input: s = "1 + 1"
#Output: 2

#Example 2:
#Input: s = " 2-1 + 2 "
#Output: 3

#Example 3:
#Input: s = "(1+(4+5+2)-3)+(6+8)"
#Output: 23

import operator

class Solution:
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
                #print(f"enter i={i}, curnum={curnum}, acc={acc}, curop={curop}, stack={stack}")
                continue
            #end of digit stream, update acc
            if digitstream:
                acc = curop(acc, curnum)
                curnum = 0
                curop = None
                digitstream = False
                #print(f"leave digistream i={i}, curnum={curnum}, acc={acc}, curop={curop}, stack={stack}")
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
    f = open("./leetcode224.testcases.csv", "r")
    #testcases = ["1 + 1", " 2-1 + 2 ", "(1+(4+5+2)-3)+(6+8)", "1-(     -2)"]
    testcases = [line.rstrip() for line in f]
    for testcase in testcases:
        tcstring = textwrap.shorten(testcase, width=30, placeholder="...")
        #print(f'calculate("{tcstring}")')
        print(f'calculate("{tcstring}")={s.calculate(testcase)}')
        try:
            #LC last test case, seems to break built-in eval
            print(f'eval("{tcstring}")={eval(testcase)}')
        except:
            pass
