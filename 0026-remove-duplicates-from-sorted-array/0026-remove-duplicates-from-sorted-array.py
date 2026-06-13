class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = sorted(list(set(nums)))
        size = len(s)

        for i in range(size):
            nums[i] = s[i]

        return size