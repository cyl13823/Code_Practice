class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a1 = int(a)
        b1 = int(b)
        c = a1+b1
        c = list(str(c))
        c.insert(0,'0')
        c = [int(i) for i in c]
        for i in range(len(c)-1,-1,-1):
            if c[i] ==2:
                c[i-1] += 1
                c[i] = 0
            elif c[i] == 3:
                c[i-1] += 1
                c[i] = 1

        if c[0] == 0:
            c.pop(0)
        c = [str(i) for i in c]
        c = ''.join(c)
        return c
    
# test
sol = Solution()
a = '1111'
b = '1111'
result = sol.addBinary(a,b)
print(result)