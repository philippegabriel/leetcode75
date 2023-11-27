'''
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size,
and the sign represents its direction (positive meaning right, negative meaning left).
Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions.
If two asteroids meet, the smaller one will explode.
If both are the same size, both will explode.
Two asteroids moving in the same direction will never meet.

Example 1:
Input: asteroids = [5,10,-5]
Output: [5,10]

Input: asteroids = [8,-8]
Output: []

Input: asteroids = [10,2,-5]
Output: [10]
'''
from typing import List, Optional
class Solution:
    def does_collide(self, x:int, y:int)->bool:
        """ tests if collision occurs"""
        return y<0<x
    def collide(self, x:int, y:int) -> Optional[int]:
        """ effects a collision """
        assert y<0<x
        sum_collide = x+y
        if sum_collide == 0:
            return None
        if sum_collide < 0:
            return y
        return x
    # pylint: disable-next=invalid-name
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        found:bool = True
        while found:
            tmp: List[int] = []
            found = False
            i:int = 0
            j:Optional[int]=None
            while i<len(asteroids):
                if i != len(asteroids)-1 and self.does_collide(asteroids[i], asteroids[i+1]):
                    if j:= self.collide(asteroids[i], asteroids[i+1]):
                        tmp.append(j)
                    found = True
                    i+=2
                else:
                    tmp.append(asteroids[i])
                    i+=1
            asteroids = tmp[:]
        return asteroids

if __name__ == "__main__":
    s=Solution()
    assert s.asteroidCollision([5,10,-5]) == [5, 10]
    assert not s.asteroidCollision([8,-8])
    assert s.asteroidCollision([10,2,-5]) == [10]
