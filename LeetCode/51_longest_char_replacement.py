class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        counts = {}
        global_max = 0
        
        def over_k():
            total = 0
            max_char = 0
            for key in counts.keys():
                total += counts[key]
                max_char = max(max_char, counts[key])
            return (total - max_char) > k
        
        while right < len(s):
            if not over_k():
                char = s[right]
                counts[char] = counts[char]+1 if counts.get(char, False) else 1
                right += 1
            else:
                char = s[left]
                counts[char] = counts[char]-1 if counts.get(char, 0) > 0 else 0
                left += 1
            count = sum(counts.values())-1 if over_k() else sum(counts.values())
            global_max = max(global_max, count)
        return global_max

print(Solution().characterReplacement("AABABBA", 1))