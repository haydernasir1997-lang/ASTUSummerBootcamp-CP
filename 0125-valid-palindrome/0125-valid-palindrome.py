class Solution:
    def isPalindrome(self, s: str) -> bool:

        lett = "qwertyuioplkjhgfdsazxcvbnm1234567890"
        palin = ""
        for i in s.lower():
            if i in lett:
                palin += i
        palin.lower()
       
        if palin == palin[::-1]:
            return True
        else:
            return False