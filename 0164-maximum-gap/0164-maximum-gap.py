class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        maxs = 0
        nums.sort()
        for i in range(len(nums)-1):
            maxs = max(maxs , nums[i+1] - nums[i])
        return maxs