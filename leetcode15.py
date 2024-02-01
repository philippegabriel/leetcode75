'''
15. 3Sum
'''
from typing import List
from collections import Counter
class Solution:
    # pylint: disable-next=invalid-name
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result:set[tuple[int,...]]=set()
        pset:set[int]=set()
        nset:set[int]=set()
        counter:Counter[int]=Counter(nums)
        for i in counter:
            if not i:
                continue
            if i>0:
                pset.add(i)
            else:
                nset.add(-i)
        #check for triple 0
        if counter[0]>=3:
            result.add((0,0,0))
        #find all x-x+0
        if 0 in counter:
            for i in  pset & nset:
                result.add((i,-i,0))
        #find all x+y-z
        for i in pset:
            for j in pset:
                if i == j and counter[i] == 1:
                    continue
                if i+j in nset:
                    result.add((-(i+j),min(i,j),max(i,j)))
        #find all -x-y+z
        for i in nset:
            for j in nset:
                if i == j and counter[-i] == 1:
                    continue
                if i+j in pset:
                    result.add((min(-i,-j),max(-i,-j),i+j))
        #convert result to list
        return [list(i) for i in result]

def test() -> None:
    s=Solution()
    assert s.threeSum(nums = [-1,0,1,2,-1,-4]) == [[1, -1, 0], [-1, -1, 2]]
    assert s.threeSum(nums = [0,1,1]) == []
    assert s.threeSum(nums = [0,0,0]) == [[0,0,0]]

if __name__ == "__main__":
    test()
