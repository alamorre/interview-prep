def weight(num: int) -> int:
    count = 0
    while num > 0:
        if num & 1: count += 1
        num = num >> 1
    return count

print(weight(1))
print(weight(2))
print(weight(3))