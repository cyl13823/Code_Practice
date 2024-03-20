class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        dic = {}
        for index, element in enumerate(nums):
            dic[element] = index
        if target in dic:
            return dic[target]
        else:
            if target > max(nums):
                return len(nums)
            else:
                i = 0
                while target > nums[i]:
                    i += 1
                else:
                    return i
                
# test
solution = Solution()
nums = [1,3,5,6]
target = 7
results = solution.searchInsert(nums,target)
print(results)