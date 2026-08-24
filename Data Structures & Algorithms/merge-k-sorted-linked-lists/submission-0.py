import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, ll in enumerate(lists):
            heapq.heappush(heap, (ll.val, i))
        done = 0
        sort_ll = ListNode()
        t = sort_ll
        while done < len(lists):
            v, i = heapq.heappop(heap)
            if lists[i].next:
                lists[i] = lists[i].next
                heapq.heappush(heap, (lists[i].val, i))
            else:
                done += 1
            t.next = ListNode(v)
            t = t.next
        return sort_ll.next
