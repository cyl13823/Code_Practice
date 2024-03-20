class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        a = []
        l = list(s)
        for i in range(len(l)):
            a.append(dic[l[i]])
        
        for i in range(0,len(l)-1):
            if a[i] < a[i+1]:
                a.append(-2*a[i])

        return sum(a)

# test
solution = Solution()
roman_numeral = "MCMXCIV"
result = solution.romanToInt(roman_numeral)
print(result)