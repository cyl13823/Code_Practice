class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        x = []
        for i in nums:
            if i%2 !=0:
                x.append(i)
            else:
                x.insert(0,i)
        return x

# test
sol = Solution()
nums = [1,2,3,4]
result = sol.sortArrayByParity(nums)
print(result)