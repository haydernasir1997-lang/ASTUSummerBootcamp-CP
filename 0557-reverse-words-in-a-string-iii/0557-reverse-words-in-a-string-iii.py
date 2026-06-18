class Solution:
    def reverseWords(self, s: str) -> str:
        num_spaces = 0  
        for i in range(len(s)):
            if s[i] == " ":
                num_spaces += 1
        s = s.split()
        r = []
        for i in range(num_spaces + 1):
            sr = list(s[i])
            sr.reverse()
            sr = "".join(sr)
            r.append(sr)
        r = " ".join(r)
        return r
