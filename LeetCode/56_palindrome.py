class Solution:
    def isPalindrome(self, s: str) -> bool:
        ascii_str = ''
        for char in s: # O(n) time and space
            if ord('a') <= ord(char.lower()) <= ord('z') \
                or ord('0') <= ord(char.lower()) <= ord('9'):
                ascii_str = ascii_str + char.lower()

        # O(n/2) time, O(1) space
        for i in range(0, len(ascii_str) // 2): # floor bc middle char doesnt matter
            if ascii_str[i] != ascii_str[len(ascii_str) - 1 - i]:
                return False
        
        return True

print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
print(Solution().isPalindrome("0p"))
