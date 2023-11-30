'''
437. Path Sum III
Medium
Given the root of a binary tree and an integer targetSum,
return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf,
but it must go downwards (i.e., traveling only from parent nodes to child nodes).

Example 1:
Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.

Example 2:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3
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
        if val is None:
            return None
    except IndexError:
        return None
    #print(f"TreeNode({val=}, build_tree({2*index+1}), build_tree({2*index+2}))")
    return TreeNode(val, build_tree(tree, 2 * index + 1), build_tree(tree, 2 * index + 2))

class Solution:
    # pylint: disable-next=invalid-name
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        path_set:set[tuple[TreeNode, TreeNode]]=set({})
        path_seen:set[tuple[TreeNode, TreeNode]]=set({})
        self.path_sum_acc(root, targetSum, path_set, path_seen)
        return len(path_set)

    def path_sum_acc(self, root: Optional[TreeNode], target_sum: int, path_set:set[tuple[TreeNode, TreeNode]], path_seen:set[tuple[TreeNode, TreeNode]], valroot:int = None, acc:int =0) -> None:
        if root is None:
            return
        if valroot is None:
            valroot = root
        path=tuple((valroot, root))
        if path in path_seen:
            return
        path_seen.add(path)
        newacc = acc + root.val
        #print(f'{root.val=}, {acc=}')
        if newacc == target_sum:
            #print('...target')
            path_set.add(path)
        self.path_sum_acc(root.left, target_sum, path_set, path_seen, valroot, newacc)
        self.path_sum_acc(root.right, target_sum, path_set, path_seen, valroot, newacc)
        self.path_sum_acc(root.left, target_sum, path_set, path_seen)
        self.path_sum_acc(root.right, target_sum, path_set, path_seen)

def test() -> None:
    root = None
    s=Solution()
    root = build_tree([10,5,-3,3,2,None,11,3,-2,None,1])
    assert s.pathSum(root, 8) == 3
    root = build_tree([5,4,8,11,None,13,4,7,2,None,None,5,1])
    assert s.pathSum(root, 22) == 3
    root = build_tree([1,None,2,None,None,None,3,None,None,None,None,None,None,None,4,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,5])
    assert s.pathSum(root, 3) == 2
    root = build_tree([0,1,1])
    assert s.pathSum(root, 1) == 4

if __name__ == "__main__":
    test()
