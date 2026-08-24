# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_map = {}
        def deep_copy(node: 'Optional[Node]'):
            if node is None:
                return None
            if node in node_map:
                return node_map[node]
            new_node = Node(node.val)
            node_map[node] = new_node
            new_node.next = deep_copy(node.next)
            new_node.random = deep_copy(node.random)
            return new_node
        return deep_copy(head)