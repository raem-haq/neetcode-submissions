from collections import defaultdict

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        d = defaultdict(bool)
        while head:
            if d[head]:
                return True
            d[head] = True
            head = head.next
        return False

