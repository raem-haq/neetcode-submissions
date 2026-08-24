# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        def rsv(root, d, max_seen_depth):
            if root is None:
                return max_seen_depth
            if d > max_seen_depth:
                max_seen_depth = d
                out.append(root.val)
            max_seen_depth = rsv(root.right, d + 1, max_seen_depth)
            return rsv(root.left, d+1, max_seen_depth)

        _ = rsv(root, 1, 0)
        return out