class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ""
        group = ""

        for i in range(len(s)):
            if s[i] != " ":
                group += s[i]

            elif group != "":
                ans = group + " " + ans
                group = ""

        if group != "":
            ans = group + " " + ans

        return ans[:-1]