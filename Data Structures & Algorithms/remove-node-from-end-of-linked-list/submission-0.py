# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        h = head
        l = 0
        while h:
            l += 1
            h = h.next
        
        h = ListNode()
        t = h
        i = 0
        while head:
            if i == l - n:
                t.next = head.next
                head = head.next
            else:
                t.next = head
            if head:
                head = head.next
            t = t.next
            i += 1
        return h.next
