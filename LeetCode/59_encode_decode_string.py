from typing import List 

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        ans = ''
        for string in strs:
            length = len(string) # 8
            str_len = str(length) # 8
            if length < 10:
                str_len = '00' + str_len # 008
            elif length < 100:
                str_len = '0' + str_len
            ans = ans + str_len + string # 008 + snowcone
        return ans 

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        ans = []
        while len(s) > 0:
            delim, s = int(s[0:3]), s[3:]
            ans.append(s[0:delim])
            s = s[delim:]
        return ans

coder = Codec()
for_wire = coder.encode(['bob', 'bill'])
print(for_wire)
normal = coder.decode(for_wire)
print(normal)