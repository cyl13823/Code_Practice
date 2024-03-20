class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        char_count_s = {}
        char_count_t = {}

        for char in s:
            char_count_s[char] = char_count_s.get(char, 0) + 1

        for char in t:
            char_count_t[char] = char_count_t.get(char, 0) + 1

        for char, count_t in char_count_t.items():
            count_s = char_count_s.get(char, 0)
            if count_t != count_s:
                return char

        return ""

# test
s = 'abc'
t = 'abcd'
solution = Solution()
result = solution.findTheDifference(s,t)
print(result)