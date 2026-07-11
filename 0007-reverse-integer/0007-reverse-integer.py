class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        indx = -1
        revers = ""
        for i in range(len(s)):
            if s[indx].isdigit():
                revers += (s[indx])
                indx -= 1
      
        if -2**31 <= int(revers)<= 2**31 - 1:
            if x >= 0:
                return int(revers)
            else:
                return -int(revers ) 
        else:
            return 0 
