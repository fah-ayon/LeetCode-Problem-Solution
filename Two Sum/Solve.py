class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j] 

            
nums = [10, 9, 11, 2]
target = 11
print(Solution().twoSum(nums, target))


