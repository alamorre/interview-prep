class Solution:
    def getSum(self, a: int, b: int) -> int:
        # ensure x >= y
        x, y = abs(a), abs(b)
        if x < y:
            return self.getSum(b, a)  
    
        # magnitude of a is greater
        # if a > 0, guaranteed overall negative
        
        # Handle if a is -neg
        sign = 1 if a > 0 else -1
        
        if a * b >= 0:
            # sum of two positive integers
            while y:
                x, y = x ^ y, (x & y) << 1 # *2
        else:
            # difference of two positive integers
            while y:
                x, y = x ^ y, ((~x) & y) << 1 # *2
        
        return x * sign

