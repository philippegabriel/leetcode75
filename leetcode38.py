'''
38. Count and Say
'''
class Solution:
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
    def countAndSay(self, n: int) -> str:
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
        #print(f'{i=}->{s.countAndSay(i)=}')

if __name__ == "__main__":
    test()
