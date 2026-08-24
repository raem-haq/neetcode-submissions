# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def invert(root):
    if not root:
        return
    invert(root.left)
    invert(root.right)
    root.right, root.left = root.left, root.right

    

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        invert(root)
        return root