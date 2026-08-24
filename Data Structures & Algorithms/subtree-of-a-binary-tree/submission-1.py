# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isSame(p, q):
    if not p and not q:
        return True

    if not (p and q):
        return False
    
    if p.val != q.val:
        return False
    
    return isSame(p.left, q.left) and isSame(p.right, q.right)


def is_subtree(root, subroot):
    if not subroot:
        return not root
    if not root:
        return False

    if root.val == subroot.val:
        if (isSame(root.left, subroot.left) and 
            isSame(root.right, subroot.right)):
            return True
    
    return is_subtree(root.left, subroot) or is_subtree(root.right, subroot) 


class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return is_subtree(root, subRoot)