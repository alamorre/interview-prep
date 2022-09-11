class Node:
    def __init__(self, val):
        self.val: str = val
        self.children = {} # { str: Node } pairing
    
class Trie:
    def __init__(self):
        self.root = Node('*')

    def insert(self, word: str) -> None:
        # Use string internally ya GOOF!
        def recurse(node, string):
            # string end. Mark end and return
            if len(string) == 0: 
                node.children['*'] = True
            # If char exists, move to next char
            elif node.children.get(string[0], False):
                recurse(node.children[string[0]], string[1:])
            # If char is new, add and move to next char
            else:
                node.children[string[0]] = Node(string[0])
                recurse(node.children[string[0]], string[1:])
        recurse(self.root, word)

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if node.children.get(char, False):
                node = node.children[char]
            else:
                return False
        return node.children.get('*', False)

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if node.children.get(char, False):
                node = node.children[char]
            else:
                return False
        return True # Misinterpreted prefix requirement (much simpler!)

trie = Trie()
trie.insert('apple')

"""
I mean you actually got it. Slipped 1 variable and misunderstood the prefix-requirements.
One would have got you on interview and the other you would have caught!
"""