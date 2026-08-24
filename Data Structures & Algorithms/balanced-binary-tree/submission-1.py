# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def is_balanced_depth(root):
    if not root:
        return (True, 0)
    b1, l = is_balanced_depth(root.left)
    if not b1:
        return (False, 0) #depth doesn't matter
    b2, r = is_balanced_depth(root.right)
    if not b2:
        return (False, 0) #depth doesn't matter
    return (abs(l - r) <= 1, max(l,r) + 1)

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return is_balanced_depth(root)[0] 