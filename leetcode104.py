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
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(tree: list[int], index: int = 0) -> Optional[TreeNode]:
    try:
        val = tree[index]
        if not val:
            return None
    except IndexError:
        return None
    #print(f"TreeNode({val=}, build_tree(tree, {2 * index + 1}), build_tree(tree, {2 * index + 2}))")
    return TreeNode(val, build_tree(tree, 2 * index + 1), build_tree(tree, 2 * index + 2))

class Solution:
    # pylint: disable-next=invalid-name
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        else: return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

def test() -> None:
    root = None
    s=Solution()
    root = build_tree([3,9,20,None,None,15,7])
    assert s.maxDepth(root) == 3
    root = build_tree([1,None,2])
    assert s.maxDepth(root) == 2

if __name__ == "__main__":
    test()
