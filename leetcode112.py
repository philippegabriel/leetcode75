'''
112. Path Sum
Easy
Given the root of a binary tree and an integer targetSum, 
return true if the tree has a root-to-leaf path such that adding up all the values 
along the path equals targetSum.
A leaf is a node with no children.

 

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown.

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: false
Explanation: There two root-to-leaf paths in the tree:
(1 --> 2): The sum is 3.
(1 --> 3): The sum is 4.
There is no root-to-leaf path with sum = 5.

Example 3:
Input: root = [], targetSum = 0
Output: false
Explanation: Since the tree is empty, there are no root-to-leaf paths.
'''
from typing import Optional
from treenode import TreeNode, build_tree
class Solution:
    # pylint: disable-next=invalid-name
    def hasPathSum(self, root: Optional[TreeNode], target_sum: int) -> bool:
        return self.has_path_sum(root, target_sum)
    # pylint: disable-next=line-too-long
    def has_path_sum(self, root: Optional[TreeNode], target_sum: int, acc: int=0, found:bool=False) -> bool:
        if root is None:
            return False
        if found:
            return True
        newacc:int = acc + root.val
        if root.left is None and root.right is None:
            return newacc == target_sum
        return \
            self.has_path_sum(root.left, target_sum, newacc, found) or \
            self.has_path_sum(root.right, target_sum, newacc, found)

def test() -> None:
    root = None
    s=Solution()
    root = build_tree([1,2,3])
    assert not s.hasPathSum(root, 5)
    #Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
    #Output: true
    root = build_tree([5,4,8,11,None,13,4,7,2,None,None,None,1])
    assert s.hasPathSum(root, 22)
    root = build_tree([])
    assert not s.hasPathSum(root, 0)


if __name__ == "__main__":
    test()
