# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        out = []
        def rightSideView(root, d, depth):
            if root is None:
                return depth
            if d > depth:
                depth = d
                out.append(root.val)
            depth = rightSideView(root.right, d + 1, depth)
            return rightSideView(root.left, d+1, depth)

        _ = rightSideView(root, 1, 0)
        return out