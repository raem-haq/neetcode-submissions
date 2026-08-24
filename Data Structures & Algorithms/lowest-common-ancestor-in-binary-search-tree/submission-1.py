# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right 

def lca(root, p, q):
    if not root:
        return None
    
    if p.val == root.val:
        return p
    elif q.val == root.val:
        return q

    if p.val < root.val:
        if q.val > root.val:
            return root
        else:
            return lca(root.left, p, q)
    else:
        if q.val < root.val:
            return root
        else:
            return lca(root.right, p, q)

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        return lca(root, p, q)