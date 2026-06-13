class Solution:
    def maxDistinct(self, s: str) -> int:
        st = ""
        for i in s:
            if i not in st:
                st += i
        return len(st)        