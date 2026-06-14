class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        new_arr = [0]*n
        for i in range(n):
            new_arr[(i + 3) % n] = nums[i]

        if target in nums:
            return nums.index(target)
        else:
            for i in range(n):
                if nums[i] > target:
                    return nums.index(nums[i]) - 1
                    break
                else:
                    return -1
                    break    
                
