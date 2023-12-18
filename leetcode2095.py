'''
2095. Delete the Middle Node of a Linked List
Medium
3.8K
69
Companies
You are given the head of a linked list. Delete the middle node,
and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node
from the start using 0-based indexing, where ⌊x⌋ denotes the largest
integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
 

Example 1:
Input: head = [1,3,4,7,1,2,6]
Output: [1,3,4,1,2,6]
Explanation:
The above figure represents the given linked list.
The indices of the nodes are written below.
Since n = 7, node 3 with value 7 is the middle node, which is marked in red.
We return the new list after removing this node. 

Example 2:
Input: head = [1,2,3,4]
Output: [1,2,4]
Explanation:
The above figure represents the given linked list.
For n = 4, node 2 with value 3 is the middle node, which is marked in red.

Example 3:
Input: head = [2,1]
Output: [2]
Explanation:
The above figure represents the given linked list.
For n = 2, node 1 with value 1 is the middle node, which is marked in red.
Node 0 with value 2 is the only node remaining after removing node 1.
'''
from typing import Optional, TYPE_CHECKING
class ListNode:
    def __init__(self, val:int=0, next:Optional['ListNode']=None):
        self.val = val
        self.next:Optional['ListNode'] = next

def build_listnode(a:list[int]) -> Optional[ListNode]:
    if not a:
        return None
    root: ListNode = ListNode(a[0],None)
    cur_node:ListNode = root
    for i in a[1:]:
        cur_node.next = ListNode(i,None)
        cur_node = cur_node.next
    return root

def listnode2list(head:Optional[ListNode])->list[int]:
    cur_node = head
    result:list[int]=[]
    while cur_node:
        result.append(cur_node.val)
        cur_node = cur_node.next
    return result

class Solution:
    # pylint: disable-next=invalid-name
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #Compute list len
        cur_node = head
        len_list=0
        while cur_node:
            len_list += 1
            cur_node = cur_node.next
        #Walk to middle of list
        mid:int = len_list // 2
        if mid < 1:
            return None
        cur_node = head
        for _ in range(1,mid):
            if TYPE_CHECKING:
                assert cur_node and cur_node.next
            cur_node = cur_node.next
        #Patch list
        if TYPE_CHECKING:
            assert cur_node and cur_node.next
        cur_node.next = cur_node.next.next
        return head
        
def test() -> None:
    l = build_listnode([1,3,4,7,1,2,6])
    print(listnode2list(l))
    s=Solution()
    result = s.deleteMiddle(l)
    print(listnode2list(result))
    assert listnode2list(result) == [1,3,4,1,2,6]

    l = build_listnode([1,2,3,4])
    print(listnode2list(l))
    s=Solution()
    result = s.deleteMiddle(l)
    print(listnode2list(result))
    assert listnode2list(result) == [1,2,4]

    l = build_listnode([2,1])
    print(listnode2list(l))
    s=Solution()
    result = s.deleteMiddle(l)
    print(listnode2list(result))
    assert listnode2list(result) == [2]
if __name__ == "__main__":
    test()
