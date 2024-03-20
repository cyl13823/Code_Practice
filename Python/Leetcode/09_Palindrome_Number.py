class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return print('False')
        
        if str(x) == (str(x)[::-1]):
            return print('True')

# test
solution = Solution()
x = -121
solution.isPalindrome(x)
print(solution)