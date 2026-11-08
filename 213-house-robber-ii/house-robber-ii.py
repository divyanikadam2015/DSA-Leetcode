class Solution:
    def rob(self, nums: list[int]) -> int:
        def helper(arr):
            prev = curr = 0
            for x in arr:
                prev, curr = curr, max(curr, prev + x)
            return curr
        if len(nums) == 1:
            return nums[0]
        return max(helper(nums[:-1]), helper(nums[1:]))                    