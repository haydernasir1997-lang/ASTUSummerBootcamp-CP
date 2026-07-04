class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        vowl = "aeiouAEIOU"
        left = 0 
        right = len(s) - 1
        while left < right:
            if s[left] in vowl and s[right] in vowl:
                s[left] , s[right] = s[right] , s[left]
                left +=1
                right -= 1
            elif s[left] in vowl and s[right] not in vowl:
                right -= 1
            elif s[left] not in vowl and s[right] in vowl:
                left +=1
            else:
                left +=1
                right -= 1
        return "".join(s)




                
