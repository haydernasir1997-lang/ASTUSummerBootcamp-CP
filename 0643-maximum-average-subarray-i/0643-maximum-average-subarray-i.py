class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        avg = sum(nums[:k])     
        maximum = avg
        left = 0

        for i in range(k, len(nums)):
            avg = avg - nums[left] + nums[i]
            maximum = max(maximum, avg)
            left += 1
        return maximum /k