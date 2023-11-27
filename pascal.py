from typing import List
class Solution:
    def generate(self, row: List[int]) -> List[int]:
        result = []
        pred = 0
        for i in row:
            result.append(i+pred)
            pred = i
            print(i)


if __name__ == "__main__":
    mysolution = Solution()
    mysolution.generate([1,2])
