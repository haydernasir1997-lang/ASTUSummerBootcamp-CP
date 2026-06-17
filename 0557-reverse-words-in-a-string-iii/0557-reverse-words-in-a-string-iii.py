class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        string = ""

        for i in s:
            if i != " ":
                string += i
            elif i == " ":
                words.append(string)
                string = ""

        if string != "":
            words.append(string) 

        revers = ""        
        for k in range(len(words)):
            revers += words[k][::-1]
            revers += " "
        return revers.strip()   
