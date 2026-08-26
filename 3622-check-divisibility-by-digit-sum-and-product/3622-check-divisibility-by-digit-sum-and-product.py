class Solution:
    def checkDivisibility(self, n: int) -> bool:
        lists = list(str(n))
        nums = [int(i) for i in lists]

        sums = sum(nums)

        multples = 1
        for i in nums:
            multples *= i

        if n % (sums + multples) == 0:
            return True
        else:
            return False