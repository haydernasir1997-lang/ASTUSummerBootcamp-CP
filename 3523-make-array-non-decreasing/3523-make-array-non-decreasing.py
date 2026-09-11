class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        answer = 0
        last = 0

        for x in nums:
            if x >= last:
                answer += 1
                last = x

        return answer