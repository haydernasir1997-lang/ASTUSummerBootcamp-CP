class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        nums.sort()
        avg = sum(nums) // len(nums)
        if avg < 0:
            ans = 1
            for i in range(len(nums)):
                if ans not in nums:
                    return ans
                    break
                else:
                    ans += 1

        else:
            count = 1
            for i in range(len(nums)):

                if avg + count not in nums:
                    return  count + avg 
                    break
                else:
                    count += 1 

