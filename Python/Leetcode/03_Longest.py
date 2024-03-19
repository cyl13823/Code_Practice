class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = {}
        length = 0
        for r in range(len(s)):
            char = s[r]
            if char in seen and l <= seen[char]:
                l = seen[char]+1
            else:
                length = max(length,r-l+1)
            seen[char] = r
        return length