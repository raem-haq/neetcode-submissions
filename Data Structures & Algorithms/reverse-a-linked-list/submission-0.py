# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rvs = None
        while head:
            rvs = ListNode(head.val, rvs)
            head = head.next
        return rvs    