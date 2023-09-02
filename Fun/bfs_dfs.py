class Node():
    def __init__(self, val: str, children: list) -> None:
        self.val = val
        self.children = children 

e = Node('e', [])
d = Node('d', [])
c = Node('c', [])
b = Node('b', [d, e])
a = Node('a', [b, c])

def dfs_rec(node: Node):
    visited = set()
    def helper(node: Node):
        if node.val in visited:
            return 
        print(node.val)
        visited.add(node.val)
        for child in node.children:
            helper(child)
    helper(node)
dfs_rec(a) # a b d e c

def bfs_rec(node: Node):
    visited = set()
    queue = [node]
    while len(queue) > 0:
        node = queue.pop(0)
        print(node.val)
        visited.add(node.val)
        for child in node.children:
            if child.val not in visited:
                queue.append(child)
bfs_rec(a) # a b c d e

# Bidirectional graphs
a_edges = [('a', 'b'), ('a', 'c')]
b_edges = [('b', 'a'), ('b', 'c')]
c_edges = [('c', 'a'), ('c', 'b')]

n1, n2 = a_edges[0]
print(n1, n2)