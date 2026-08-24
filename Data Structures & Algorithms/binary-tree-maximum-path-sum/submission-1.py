# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def ans(root: Optional[TreeNode]) -> int:
        if not root:
            return (-float('inf'), -float('inf'))
        l, L = ans(root.left)
        r, R = ans(root.right)
        root_max = max(
            root.val,
            root.val + l,
            root.val + r
        )
        M = max(root_max, root.val + l + r, L, R)
        return (root_max, M)

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return ans(root)[1]