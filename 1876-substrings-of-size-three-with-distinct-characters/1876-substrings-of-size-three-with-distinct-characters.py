class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        answer = []
        for i in range(len(s)-2):
            answer.append(s[i:i+3])
        
        ans = 0
        for k in range(len(answer)):
            if len(set(answer[k])) == 3:
                ans += 1
        return ans



        return ans


