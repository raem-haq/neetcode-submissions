"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        node_map = {}
        def copy_graph(node):
            if not node:
                return None
            if node in node_map:
                return node_map[node]
            new_node = Node(node.val)
            node_map[node] = new_node
            for n in node.neighbors:
                new_node.neighbors.append(copy_graph(n))
            return new_node
        return copy_graph(node)