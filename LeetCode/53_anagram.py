class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        
        ang_s = {}
        for i in range(0, len(s)):
            ang_s[s[i]] = ang_s.get(s[i], 0) + 1
        
        ang_t = {}
        for i in range(0, len(t)):
            ang_t[t[i]] = ang_t.get(t[i], 0) + 1
        
        for char in s:
            if ang_s[char] != ang_t.get(char, -1):
                return False
            
        return True
        
