# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def level(root, lst=None, i=0):
    if lst is None:
        lst = []
    if not root:
        return []
    if i > len(lst) - 1:
        lst.append([])
    lst[i].append(root.val)
    level(root.left, lst, i+1)
    level(root.right, lst, i+1)
    return lst


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        return level(root)