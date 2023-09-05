class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right, sol = 0, 0, 0
        counts = {}

        def we_can_add(char: str):
            counts[char] = 1 if char not in counts else counts[char] + 1
            total, max_c = 0, 0
            for value in counts.values():
                total += value 
                max_c = max(max_c, value)
            counts[char] -= 1
            return total - max_c <= k

        while right < len(s):
            l_c, r_c = s[left], s[right]
            if we_can_add(r_c):
                counts[r_c] = 1 if r_c not in counts else counts[r_c] + 1
                sol = max(sol, sum(counts.values()))
                right += 1
            else:
                counts[l_c] = 0 if counts.get(l_c, 0) == 0 else counts[l_c] - 1
                left += 1
        return sol

print(Solution().characterReplacement("AABABBA", 1))