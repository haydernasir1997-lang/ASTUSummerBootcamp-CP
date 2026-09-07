class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        nums = []
        for i in range(len(str(x))):
            nums.append(int(str(x)[i]))
        
        if x % sum(nums) == 0:
            return sum(nums)
        else:
            return -1