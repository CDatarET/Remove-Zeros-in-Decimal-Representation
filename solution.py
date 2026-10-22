class Solution:
    def removeZeros(self, n: int) -> int:
        s = []
        while n > 0:
            if n % 10 > 0:
                s.append(str(n % 10))
            
            n //= 10
        
        return int("".join(s[::-1]))
