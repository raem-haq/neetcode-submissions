# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        t = ans
        carry = 0
        while carry or l1 or l2:
            summ = carry
            if l1:
                summ += l1.val
                l1 = l1.next
            if l2:
                summ += l2.val
                l2 = l2.next
            carry = summ // 10
            summ %= 10
            t.next = ListNode(summ)
            t = t.next
        return ans.next
