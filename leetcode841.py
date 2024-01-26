'''
841. Keys and Rooms
Medium
5.8K
258
Companies
There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0.
Your goal is to visit all the rooms. 
However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it.
Each key has a number on it, denoting which room it unlocks,
and you can take all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain
if you visited room i, return true if you can visit all the rooms, or false otherwise.

Example 1:
Input: rooms = [[1],[2],[3],[]]
Output: true
Explanation: 
We visit room 0 and pick up key 1.
We then visit room 1 and pick up key 2.
We then visit room 2 and pick up key 3.
We then visit room 3.
Since we were able to visit every room, we return true.

Example 2:
Input: rooms = [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can not enter room number 2 since the only key that unlocks it is in that room.
'''
from typing import List, Deque
from collections import deque

class Solution:
    # pylint: disable-next=invalid-name
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited:set[int]=set()
        discovered: Deque[int]=deque([0])
        while discovered:
            next_room:int=discovered.popleft()
            if next_room in visited:
                continue
            visited.add(next_room)
            discovered.extend(rooms[next_room])
        return len(visited) == len(rooms)

    # pylint: disable-next=invalid-name
    def canVisitAllRooms_rec(self, rooms: List[List[int]]) -> bool:
        def visit_rec(indexes:set[int]) -> None:
            nonlocal rooms, unvisited
            for i in indexes:
                if i in unvisited:
                    unvisited.remove(i)
                    visit_rec(set(rooms[i]))
            return
        unvisited=set(range(len(rooms)))
        visit_rec({0})
        return not bool(unvisited)

def test() -> None:
    s=Solution()
    i = [[1],[2],[3],[]]
    assert s.canVisitAllRooms(i)
    assert s.canVisitAllRooms_rec(i)

    i=[[1,3],[3,0,1],[2],[0]]
    assert not s.canVisitAllRooms(i)
    assert not s.canVisitAllRooms_rec(i)
if __name__ == "__main__":
    test()
