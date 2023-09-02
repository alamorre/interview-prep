class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors

class Solution(object):
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node):
        if not node:
            return node

        new_neighbours = []
        new_node = Node(node.val, new_neighbours)
        self.visited[node.val] = new_node

        for neighbor in node.neighbors:
            if neighbor.val in self.visited:
                new_neighbours.append(self.visited[neighbor.val])
            else:
                new_neighbor = self.cloneGraph(neighbor)
                new_neighbours.append(new_neighbor)

        return new_node
    
n1 = Node(3, [])
n2 = Node(4, [n1])
n3 = Node(5, [n1, n2])

"""
I got this right in one try.
Kinda winged it though. Gotta look for more patterns

Hashmap for unique ID as key and object as value is a good idea
"""