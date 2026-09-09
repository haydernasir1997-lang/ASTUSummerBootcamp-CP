class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        maximum = max(len(word1) ,len(word2))
        minimum = min(len(word1) ,len(word2))
        s = ""
        for i in range(minimum):
            s += word1[i]
            s += word2[i]

        if len(word1) == maximum:
            s += word1[minimum:]
            return s
        elif len(word2) == maximum:
            s += word2[minimum:]
            return s
        else:
            return s
        
            