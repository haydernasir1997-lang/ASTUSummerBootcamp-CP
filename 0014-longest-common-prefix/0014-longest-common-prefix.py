class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        temp = ""
        for i in range(len(min(strs, key=len))):
            for j in range(len(strs)):
                temp += strs[j][i]
            if len(set(temp)) == 1:
                ans += temp[0]
                temp = ""
            else:
                break
        return ans






            