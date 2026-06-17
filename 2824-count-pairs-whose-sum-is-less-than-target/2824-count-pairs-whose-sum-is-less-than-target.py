class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        srt = sorted(nums)

        left = 0
        right = len(nums) - 1
        count = 0

        while left < right:
            if srt[left] + srt[right] < target:
                count += right - left
                left += 1
            else:
                right -= 1

        return count