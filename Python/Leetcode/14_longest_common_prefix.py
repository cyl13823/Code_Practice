class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
          return ""
        common_prefix = ""
        first_str = strs[0]

        for i in range(len(first_str)):
            char = first_str[i]
            for string in strs[1:]:
                if i >= len(string) or string[i] != char:
                  return common_prefix
            common_prefix += char

        return common_prefix

# test
solution = Solution()
strs = ["flower","flow","flight"]
result = solution.longestCommonPrefix(strs)
print(result)