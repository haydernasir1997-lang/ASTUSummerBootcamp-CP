class Solution:
    def compressedString(self, word: str) -> str:
        ans = ""
        count = 1
        for i in range(1,len(word)):
             
            if word[i] == word[i-1] and count < 9:
                if count < 9:
                    count += 1
                else:
                    ans += f"{count}{word[i-1]}"
                    count = 1
            else:
                ans += f"{count}{word[i-1]}"
                count = 1
        ans += f"{count}{word[-1]}"
        return ans


