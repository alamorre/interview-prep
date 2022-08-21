from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        dict_t = Counter(t)
        required = len(dict_t) # number of formed chars needed to be a substr
        l, r = 0, 0 # left and right pointer
        formed = 0 # of chars both in t and with the same count
        window_counts = {} # Dictionary which keeps a count of all the unique characters in the current window.

        # ans tuple of the form (window length, left, right)
        ans = float("inf"), None, None

        while r < len(s):
            # Add one character from the right to the window
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1
            # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1
            # Try and contract the window till the point where it ceases to be 'desirable'.
            while l <= r and formed == required:
                character = s[l]
                if r - l + 1 < ans[0]: # Save the smallest window until now.
                    ans = (r - l + 1, l, r)
                window_counts[character] -= 1 # The character at the position pointed by the `left` pointer is no longer a part of the window.
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1
                l += 1 # Move the left pointer ahead, this would help to look for a new window.

            
            r += 1 # Keep expanding the window once we are done contracting.
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]

print(Solution().minWindow("ADOBECODEBANC", 'ABC'))

"""
Tips: store indexes, not strings to save on string comparisons
Be more careful when assigning Dicts - you had many many syntactical mistakes

The more optimal solution is to not store the values which are not useful. Just the indexes and the useful chars
"""