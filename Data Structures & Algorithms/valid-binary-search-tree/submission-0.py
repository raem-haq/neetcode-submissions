# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode], m = float('-inf'), M = float('inf')) -> bool:
        if not root:
            return True
        if root.val > m and root.val < M:
            return (self.isValidBST(root.left, m, min(M, root.val)) and
                self.isValidBST(root.right, max(m, root.val), M))
        return False