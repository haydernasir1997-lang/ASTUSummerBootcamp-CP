class Solution:
    def hammingWeight(self, n: int) -> int:
        digit = []
        while n != 0:
            digit.append(n % 2)
            n//= 2
        return digit.count(1)

