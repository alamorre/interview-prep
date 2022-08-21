from typing import List 

class Node():
    def __init__(self, value, children) -> None:
        self.value: int = value
        self.children: List[Node] = children

child_1 = Node(1, [])
child_2 = Node(2, [])
child_3 = Node(3, [])
child_4 = Node(4, [])
parent_1 = Node(5, [child_1, child_2])
parent_2 = Node(6, [child_3, child_4])
root = Node(7, [parent_1, parent_2])

def dfs(node):
    for child in node.children:
        dfs(child)
    print(node.value)
dfs(root)
