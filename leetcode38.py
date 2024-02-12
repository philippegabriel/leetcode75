'''
38. Count and Say
'''
from itertools import groupby
class Solution:
    # pylint: disable-next=invalid-name
    def countAndSay(self, n: int) -> str:
        l:list[int]=[1]
        for _ in range(1,n):
            l=[x for (k,v) in groupby(l) for x in (len(list(v)),k)]
        return ''.join((str(i) for i in l))

    def cs(self,inputlist:list[int])->list[int]:
        if len(inputlist) == 1:
            return [1]+inputlist
        #len(input)>1
        result:list[int]=[]
        prev=inputlist[0]
        i=1
        count=1
        while i< len(inputlist):
            while i<len(inputlist) and inputlist[i] == prev:
                i+=1
                count+=1
            #commit result
            result.extend([count,prev])
            #reset prev and count
            if i==len(inputlist):
                break
            prev=inputlist[i]
            count=0
        return result

    # pylint: disable-next=invalid-name
    def countAndSay_int_list(self, n: int) -> str:
        if n==1:
            return '1'
        else:
            result=[1]
            for _ in range(2,n+1):
                result=self.cs(result)
        return ''.join([str(i) for i in result])

def test() -> None:
    s=Solution()
    sols=['1', '11', '21', '1211', '111221', '312211', '13112221']
    for i, sol in enumerate(sols):
        assert sol == s.countAndSay(i+1)
        #print(f'{i+1=}->{s.countAndSay(i+1)=}')

if __name__ == "__main__":
    test()
