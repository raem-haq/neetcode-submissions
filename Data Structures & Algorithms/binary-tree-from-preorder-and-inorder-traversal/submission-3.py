from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        d = {}        
        for i, e in enumerate(inorder):
            d[e] = i

        def _constructTree(p_range, i_range):
            p0, pN = p_range
            i0, iN = i_range
            
            if p0 > pN:
                return None
            root = TreeNode(preorder[p0])
            
            index = d[root.val]
            
            left_inorder  = (i0, index - 1)
            right_inorder = (index + 1, iN)

            left_size = index - i0

            left_preorder  = (p0 + 1, p0 + left_size)
            right_preorder = (p0 + left_size + 1, pN)

            root.left = _constructTree(left_preorder, left_inorder)
            root.right = _constructTree(right_preorder, right_inorder)
            return root
        return _constructTree((0, len(preorder)-1), (0, len(inorder)-1))