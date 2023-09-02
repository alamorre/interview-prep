class Node:
    def __init__(self, val: int, children: list) -> None:
        self.val = val
        self.children = children

# Assumes all node values are unique.. maybe use reference if needed

def clone(node: Node):
    clones = {}

    # 1. tally all nodes
    visited = set()
    def dfs_tally(node: Node):
        if node.val in visited: return
        visited.add(node.val)
        clones[node.val] = Node(node.val, [])
        for child in node.children:
            dfs_tally(child)
    dfs_tally(node)

    # 2. map all connections
    visited = set()
    def dfs_connections(node: Node):
        if node.val in visited: return 
        visited.add(node.val)
        clone = clones[node.val]
        for child in node.children:
            clone.children.append(clones[child.value])
        for child in node.children:
            dfs_connections(child)
    dfs_connections(node)

    return clones[node.val]


        




n1 = Node(3, [])
n2 = Node(4, [n1])
n3 = Node(5, [n1, n2])