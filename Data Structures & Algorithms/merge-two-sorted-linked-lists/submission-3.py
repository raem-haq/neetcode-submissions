# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 and list2:
            if list1.val <= list2.val:
                mge = list1
                list1 = list1.next
            else:
                mge = list2
                list2 = list2.next
        elif list1:
            return list1
        elif list2:
            return list2
        else:
            return None
        
        tmp = mge

        while list1 and list2:
            if list1.val <= list2.val:
                tmp.next = list1
                list1 = list1.next
            else:
                tmp.next = list2
                list2 = list2.next
            tmp = tmp.next
        
        if list1:
            tmp.next = list1
        elif list2:
            tmp.next = list2
        
        return mge