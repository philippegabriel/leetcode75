'''
Helper module for TreeNode base problems
'''
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self,
                 val:int,
                 left:Optional['TreeNode']=None,
                 right:Optional['TreeNode']=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(tree: list[Optional[int]], index: int = 0) -> Optional[TreeNode]:
    try:
        val = tree[index]
        if val is None:
            return None
    except IndexError:
        return None
    #print(f"TreeNode({val=}, build_tree(tree, {2 * index + 1}),\
    # build_tree(tree, {2 * index + 2}))")
    return TreeNode(val, build_tree(tree, 2 * index + 1), build_tree(tree, 2 * index + 2))

def print_tree(root: Optional[TreeNode], indent:int=0) -> None:
    if not root:
        print('_'*indent,None)
        return
    print('_'*indent,root.val)
    print_tree(root.left, indent+3)
    print_tree(root.right, indent+3)
