import math
class Solution:
    def smallestNumber(self, n: int, t: int) -> int:

        while True:
            nums = list(map(int,str(n)))
            product = math.prod(nums)
            if product % t == 0:
                break
            else:
                n += 1
        
        return n
