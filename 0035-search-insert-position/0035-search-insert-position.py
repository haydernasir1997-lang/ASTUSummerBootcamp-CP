class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            t = nums.index(target)
            return t
        elif nums[-1] < target:
            n = len(nums)
            return n   
        else:
            for i in range(len(nums)):
                if nums[i] > target:
                    m = nums.index(nums[i])
                    return m
                    break

                
            