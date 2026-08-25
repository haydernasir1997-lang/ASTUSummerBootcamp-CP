class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        left = 0
        maltipls = k
        while left <= len(nums)+1:
            if maltipls in nums:
                maltipls += k
            else:
                return maltipls
                break
