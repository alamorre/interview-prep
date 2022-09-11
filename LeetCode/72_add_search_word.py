class Node():

    def __init__(self, val):
        self.val = val
        self.links = {}

class WordDictionary:

    def __init__(self):
        self.root = Node('*')

    def addWord(self, word: str) -> None:
        def recurse(node, s):
            if len(s) == 0:
                node.links['*'] = True
            elif node.links.get(s[0], False):
                recurse(node.links[s[0]], s[1:])
            else:
                node.links[s[0]] = Node(s[0])
                recurse(node.links[s[0]], s[1:])
        recurse(self.root, word)

    def search(self, word: str) -> bool:
        queue = [(self.root, -1)] 
        while len(queue) > 0: # i.e. paths available
            (node, index) = queue.pop()
            if index == len(word)-1:
                if node.links.get('*', False): return True
                continue
            next_char = word[index+1]
            for char in node.links.keys(): # [b,m, *]
                if char == next_char or next_char == '.': # and not *
                    if char != '*':
                        queue.append((node.links[char], index+1))
        return False

wd = WordDictionary()
wd.addWord('a')
wd.addWord('a')
print(wd.search('a'))
print(wd.search('.'))
print(wd.search('aa'))
print(wd.search('a.'))
# print(wd.search('.a'))

"""
Everybody is exceeding the time limit. But the code in LeetCode sol is more eloquent
"""