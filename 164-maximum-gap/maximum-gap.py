class Solution:
    def maximumGap(self, nums):
        nums.sort()
        return max([nums[i+1]-nums[i] for i in range(len(nums)-1)] or [0])
        