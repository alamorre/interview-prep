class Solution:
    def longestPalindrome(self, s: str) -> str:
        lenth = len(s)
        ans = [0, 0] # base case indexes
        
        for c in range(0, lenth):
            i = j = c
            is_palin = True
            while is_palin:
                j -= 1
                i += 1
                if (0 <= j and i < lenth) and s[j] == s[i]:
                    ans = [j, i] if (i-j) > (ans[1] - ans[0]) else ans
                else:
                    is_palin = False
            
            i = c
            j = c - 1
            is_palin = (0 <= j) and s[j] == s[i] 
            while is_palin:
                if (0 <= j and i < lenth) and s[j] == s[i]:
                    ans = [j, i] if (i-j) > (ans[1] - ans[0]) else ans
                else:
                    is_palin = False
                j -= 1
                i += 1
                
        return s[ans[0]:ans[1]+1]

print(Solution().longestPalindrome("bb"))

"""
Performance is great. Got to think a bit more about palindromic string properties.
Palindromic strings can be built middle out in O(n/2) time with O(1) space.
Again, geek out about the nature of the problem and properties of what youre given.

How does palindromicity work? Do we know the char range? How do anagrams work?

Why can we not do sliding window here? Because the right answer could involve sliding left back down.
It's not left and right move up every time. This requires donward moves sometimes.
"""