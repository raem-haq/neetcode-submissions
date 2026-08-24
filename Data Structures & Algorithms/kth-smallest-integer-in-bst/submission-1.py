# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stck = [root]
        ans = None
        while stck and n < k:
            curr = stck.pop()
            if curr.left:
                stck.append(curr)
                stck.append(curr.left)
                curr.left = None
            else:
                ans = curr.val
                n += 1
                if curr.right:
                    stck.append(curr.right)
        return ans
