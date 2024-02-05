'''
1679. Max Number of K-Sum Pairs
'''
from typing import List
from collections import defaultdict
class Solution:
    # pylint: disable-next=invalid-name
    def maxOperations(self, nums: List[int], k: int) -> int:
        d:defaultdict[int,set[int]]=defaultdict(set)
        result = 0
        for i,v in enumerate(nums):
            if v<k:
                d[v].add(i)
        if k/2 in d:
            result += len(d[k//2]) // 2
            del d[k//2]
        for i,v in enumerate(nums):
            if v>=k:
                continue
            j = k-v
            if j in d and d[j]:
                result += 1
                index = d[j].pop()
                nums[index] = 0 # possibly redudant
                d[v].remove(i)
        return result

def test() -> None:
    s=Solution()
    print(s.maxOperations(nums = [1,2,3,4], k = 5))
    print(s.maxOperations(nums = [3,1,3,4,3], k = 6))
if __name__ == "__main__":
    test()
