class ListNode:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

# TRICK IS TO USE A DUMMY VARIABLE SO YOU DONT HAVE TO MANAGE IS-NONE CASES

class LinkedList:

    def __init__(self):
        self.head = ListNode(-1) #dummy node
        self.tail = self.head
        self.size = 0
    
    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        h = self.head.next
        for _ in range(index):
            h = h.next
        return h.val

    def insertHead(self, val: int) -> None:
        new_node = ListNode(val, self.head.next)
        self.head.next = new_node
        if not new_node.next:
            self.tail = new_node
        self.size += 1


    def insertTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next
        self.size += 1

    def remove(self, index: int) -> bool:
        if index >= self.size:
            return False
        h = self.head
        for _ in range(index):
            h = h.next
        if index == self.size - 1:
            self.tail = h
        h.next = h.next.next
        self.size -= 1
        return True

    def getValues(self) -> List[int]:
        ret = []
        h = self.head.next
        while h:
            ret.append(h.val)
            h = h.next
        return ret


""" 
#has so many errors
class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def get(self, index: int) -> int:
        if index >= size:
            return -1
        h = self.head
        for _ in range(index):
            h = h.next
        return h.val

    def insertHead(self, val: int) -> None:
        new_head = ListNode(val, self.head)
        self.head = new_head
        if self.tail is None:
            self.tail = self.head
        self.size += 1

    def insertTail(self, val: int) -> None:
        if self.head is None:
            self.head = ListNode(val)
            self.tail = self.head
        elif self.tail:
            self.tail.next = ListNode(val)
            self.tail = self.tail.next
        else:
            raise Exception("Tail Not Found")
        self.size += 1

    def remove(self, index: int) -> bool:
        if i >= self.size:
            return False
        if i == 0:
            self.head = self.head.next
            return True  
        elif self.size == 1:
            self.head = None
        else:    
            h = self.head
            for _ in range(index-1):
                h = h.next
            h.next = h.next.next
        return True

    def getValues(self) -> List[int]:
        ret = []
        h = self.head
        while h:
            ret.append(h.val)
            h = h.next
        return ret
"""        
