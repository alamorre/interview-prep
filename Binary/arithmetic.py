def addSub(a, b):
    x, y = abs(a), abs(b)

    # Now we know |a| is greater    
    if y > x: return addSub(b, a)

    sign = -1 if a < 0 else 1

    while y:
        answer = x ^ y 
        carry = (~x & y) << 1 if a * b < 0 \
            else (x & y) << 1
        x, y = answer, carry # Don't forget about assignment cascading

    return sign * x

print(addSub(1, 2))
print(addSub(-1, 2))
print(addSub(1, -2))
print(addSub(-1, -2))
