class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:    
        ans = ""
        count = 0
        for i in range(len(t)):
            if count != len(s) and s[count] == t[i]:
                ans += t[i]
                
                if count == len(s)-1:
                    break
                else:
                    count += 1
            
        if ans == s:
            return True
        else:
            return False
                


        if s == ans:
            return True
        else:
            return False
