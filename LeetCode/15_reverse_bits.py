class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        full_bin = '{:032b}'.format(n)
        for i in range(0, 32):
            if full_bin[i] == '1': ans += 2**(i)
            
        return ans

print(43261596)
print(Solution().reverseBits(43261596))