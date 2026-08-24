# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode, M = float('-inf')) -> int:
        if not root:
            return 0
        m = max(M, root.val)
        ans = self.goodNodes(root.left, m) + self.goodNodes(root.right, m)
        return (root.val >= M) + ans