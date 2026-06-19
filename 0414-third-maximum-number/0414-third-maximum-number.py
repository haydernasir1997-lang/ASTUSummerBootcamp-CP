class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        sett = set(nums)
        if len(sett) >= 3:
            lst = sorted(list(sett))
            return lst[-3]
        else:
            return max(nums)    