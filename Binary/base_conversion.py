import math 
# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def baseTwo(self, node) -> str:
        if not node: return '1' * 15
        sign = 1 if node.val < 0 else 0
        num = abs(node.val)
        bits = [sign] + [0] * 14
        exponent = int(math.log2(num)) if num > 0 else 0
        while exponent >= 0:
            base = num // (2**exponent)
            rem = num - (base * (2**exponent))
            bits[exponent+1] = base
            num = rem
            exponent -= 1
        # 10 -> 0,01010000000000 for 10
        ans = ''
        for bit in bits: ans += str(bit)
        return ans

    def baseTen(self, bits: str) -> int:
        if bits == '1' * 15: return None
        sign = -1 if bits[0] == '1' else 1
        ans = 0
        for i in range(1, len(bits)): # assume only 0s and 1s
            bit = int(bits[i])
            if bit == 1:
                ans += (2**(i-1))
        return sign * ans # 01010 -> 10

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return ''
        # Assume this is a valid tree
        ans = ''
        queue = [root]
        while len(queue) > 0:
            node = queue.pop(0)
            # Rep is val, left, right
            ans += self.baseTwo(node) \
                + self.baseTwo(node.left) \
                + self.baseTwo(node.right)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return ans

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) < 15*3: return None
        
        node_strs = [] # [0101..., 0011..., 1011....]
        i = 15*3
        while i <= len(data):
            node_strs.append(data[i-15*3:i])
            i += 15*3
        
        nodes_dict = {} # val: obj lookup
        neighbour_dict = {} # val: neighbour vals lookup
        for node_str in node_strs:
            val = self.baseTen(node_str[0:15])
            left_val = self.baseTen(node_str[15:30])
            right_val = self.baseTen(node_str[30:45])            
            node = TreeNode(val)
            nodes_dict[node.val] = node
            neighbour_dict[node.val] = [left_val, right_val] # {1: [2,3]}
        
        # Build neightbours once DS is complete
        for node in nodes_dict.values():
            [left_val, right_val] = neighbour_dict[node.val]
            if left_val:
                node.left = nodes_dict[left_val] # Return left node Obj
            if right_val:
                node.right = nodes_dict[right_val] # Return right node Obj
        
        # In serialize, we start with root's value (index to 0-13)
        return nodes_dict[self.baseTen(data[0:15])] # Returns root node
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(0)
node4 = TreeNode(4)
node5 = TreeNode(5)

root.left = node2
root.right = node3

string = Codec().serialize(root)
i = 45
print(len(string))
while i <= len(string)+1:
    print(string[i-45:i-30], string[i-30:i-15], string[i-15:i], )
    i += 45
node = Codec().deserialize(string)
print(root.val, root.left.val, root.right.val)

"""
To handle negative representation, just use a sign bit at the front
0 for pos and 1 for neg, add that into base10 logic, then make deserialize by 15 bits
You're done!

This code works on 
"""