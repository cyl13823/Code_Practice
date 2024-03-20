class Solution:
    def isValid(self, s: str) -> bool:
        dic = {')':'(', ']':'[','}':'{'}
        car = []
        for i in s:
            if i in '([{':
                car.append(i)
            elif i in ')]}':
                if not car or car[-1] != dic[i]:
                    return False
                car.pop()
        return not car
    
# test
solution = Solution()
s = '{[]}'
result = solution.isValid(s)
print(result)