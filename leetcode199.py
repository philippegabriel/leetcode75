'''
199. Binary Tree Right Side View
Medium
Given the root of a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,null,3]
Output: [1,3]

Example 3:
Input: root = []
Output: []
'''
from typing import List, Optional
from treenode import TreeNode, build_tree

class Solution:
    def __init__(self) -> None:
        self.ledger:set[int]=set()

    # pylint: disable-next=[invalid-name, redefined-outer-name]
    def rightSideView(self, root: Optional[TreeNode], level:int=0) -> List[int]:
        if not root:
            return []
        result:List[int]=[]
        if level not in self.ledger:
            result.append(root.val)
            self.ledger.add(level)
        return result + self.rightSideView(root.right,level+1) + \
            self.rightSideView(root.left, level+1)

def test() -> None:
    s=Solution()
    t:Optional[TreeNode] = build_tree([1,2,3,None,5,None,4])
    result = s.rightSideView(t)
    print(result)
    assert result == [1,3,4]

    s=Solution()
    t = build_tree([1,None,3])
    result = s.rightSideView(t)
    print(result)
    assert result == [1,3]

    s=Solution()
    t = build_tree([])
    result = s.rightSideView(t)
    print(result)
    assert not result

    s=Solution()
    t = build_tree([1,2])
    result = s.rightSideView(t)
    print(result)
    assert result == [1,2]

    s=Solution()
    t = build_tree([1,2,3,None,5,6,None,None,None,4])
    #print_tree(t)
    result = s.rightSideView(t)
    print(result)
    assert result == [1,3,6,4]

if __name__ == "__main__":
    test()
