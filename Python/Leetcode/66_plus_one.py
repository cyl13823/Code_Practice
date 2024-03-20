class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        digits.insert(0,0)
        digits[len(digits)-1] = digits[len(digits)-1]+1
        for i in range(len(digits)-1,-1,-1):
            if digits[i] >= 10:
                digits[i-1]+=1
                digits[i] -= 10

        if digits[0] == 0:
            digits.pop(0)
        return digits
    
# test
l = [9,9,9]
solution = Solution()
result = solution.plusOne(l)
print(result)