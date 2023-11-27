'''
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

Example 1:
Input: asteroids = [5,10,-5]
Output: [5,10]

Input: asteroids = [8,-8]
Output: []

Input: asteroids = [10,2,-5]
Output: [10]
'''
class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack: list[int] = []

        for asteroid in asteroids:
            # Keep checking for collisions until the stack is empty or no collision occurs
            while stack and asteroid < 0 and stack[-1] > 0:
                if stack[-1] < abs(asteroid):
                    # The current asteroid exploded the smaller one on top of the stack
                    stack.pop()
                elif stack[-1] == abs(asteroid):
                    # Both asteroids explode
                    stack.pop()
                    break
                else:
                    # The current asteroid is exploded by the one on top of the stack
                    break
            else:
                # No collision occurred, or the stack is empty
                stack.append(asteroid)

        return stack    
if __name__ == "__main__":
    s=Solution()
    print(s.asteroidCollision([5,10,-5]))
    print(s.asteroidCollision([8,-8]))
    print(s.asteroidCollision([10,2,-5]))
    print(s.asteroidCollision([5,-5,-4,8,-9]))
