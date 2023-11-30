'''
1448. Count Good Nodes in Binary Tree
Medium
Given a binary tree root, a node X in the tree is named good if in the path from root to X
there are no nodes with a value greater than X.
Return the number of good nodes in the binary tree.

Example 1:
Input: root = [3,1,4,3,null,1,5]
Output: 4
Explanation: Nodes in blue are good.
Root Node (3) is always a good node.
Node 4 -> (3,4) is the maximum value in the path starting from the root.
Node 5 -> (3,4,5) is the maximum value in the path
Node 3 -> (3,1,3) is the maximum value in the path.

Example 2:
Input: root = [3,3,null,4,2]
Output: 3
Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.

Example 3:
Input: root = [1]
Output: 1
Explanation: Root is considered as good.
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
    #print(f"TreeNode({val=},
    #   build_tree(tree, {2 * index + 1}),
    #   build_tree(tree, {2 * index + 2}))")
    return TreeNode(val, build_tree(tree, 2 * index + 1), build_tree(tree, 2 * index + 2))

class Solution:
    # pylint: disable-next=invalid-name
    def goodNodes(self, root: TreeNode) -> int:
        return self.good_nodes_max(root)

    def good_nodes_max(self, root: TreeNode, max_node: int=-10001) -> int:
        if not root:
            return 0
        acc = 0
        new_max = max_node
        if root.val >= max_node:
            acc = 1
            new_max = root.val
        return  acc \
            + self.good_nodes_max(root.left, new_max) \
            + self.good_nodes_max(root.right, new_max)

def test() -> None:
    root = None
    s=Solution()
    root = build_tree([3,1,4,3,None,1,5])
    print(s.goodNodes(root))
    root = build_tree([3,3,None,4,2])
    print(s.goodNodes(root))
    root = build_tree([1])
    print(s.goodNodes(root))
    root = build_tree([-1,5,-2,4,4,2,-2,None,None,-4,None,-2,3,None,-2,0,None,-1,None,-3,None,-4,-3,3,None,None,None,None,None,None,None,3,-3])
    print(s.goodNodes(root))
    
if __name__ == "__main__":
    test()
