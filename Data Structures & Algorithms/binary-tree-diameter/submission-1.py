# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def depth_diameter(root, depth = 0):
    if not root:
        return (0, 0)
    l, d1 = depth_diameter(root.left)
    r, d2 = depth_diameter(root.right)
    return (max(l, r) + 1, max(d1, d2, l + r))

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return depth_diameter(root)[1]