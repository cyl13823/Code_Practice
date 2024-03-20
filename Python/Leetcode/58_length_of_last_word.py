class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()

        if ' ' not in s:
            return len(s)
        else:
            i = -1
            while ' ' != s[i]:
                i -= 1
            else:
                return (-i-1)

# test
s = 'Hello World'
solution = Solution()
result = solution.lengthOfLastWord(s)
print(result)