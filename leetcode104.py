'''
104. Maximum Depth of Binary Tree
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along
the longest path from the root node down to the farthest leaf node.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2
'''
from typing import Optional
from treenode import TreeNode, build_tree

class Solution:
    # pylint: disable-next=invalid-name
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

def test() -> None:
    root = None
    s=Solution()
    root:Optional[TreeNode] = build_tree([3,9,20,None,None,15,7])
    assert s.maxDepth(root) == 3
    root = build_tree([1,None,2])
    assert s.maxDepth(root) == 2

if __name__ == "__main__":
    test()
