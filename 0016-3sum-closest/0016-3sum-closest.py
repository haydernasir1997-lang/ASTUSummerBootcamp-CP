class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        close = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):
            left = i + 1
            right =len(nums) - 1
            while left < right:
                guess = nums[i] + nums[left] + nums[right] 
                if abs(guess - target) < abs(close - target):
                    close = guess

                if target > guess:
                    left += 1 
                elif target < guess:
                    right -= 1
                else:
                    return guess
        return close


