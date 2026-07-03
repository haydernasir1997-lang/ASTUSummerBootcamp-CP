class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
                if d[i] == 2:
                    return i
                    break
            else:
                d[i] = 1
                