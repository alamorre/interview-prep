n = 100
rev = ''
while n:
    bit = str(n & 1)
    rev += bit
    n = n >> 1

remainder = 32 - len(rev)
rev += '0'*remainder
print(rev)

sum = 0
for i in range(0, 32):
    bit = int(rev[32-1-i])
    sum += bit * (2**i)
print(sum)