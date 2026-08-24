# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:



        rvs = None
        h = head
        l = 0
        while h:
            rvs = ListNode(h.val, rvs)
            h = h.next
            l += 1
        
        rord = ListNode()
        tmp = rord
        i = 0

        while True:
            if i == l:
                break
            tmp.next = head
            tmp = tmp.next
            head = head.next
            i += 1

            if i == l:
                break
            tmp.next = rvs
            tmp = tmp.next
            rvs = rvs.next
            i += 1
        
        tmp.next = None
        head = rord.next
        
          