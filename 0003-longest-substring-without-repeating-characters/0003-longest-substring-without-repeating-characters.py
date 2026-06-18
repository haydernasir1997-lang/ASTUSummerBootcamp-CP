class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maximum = 0
        left = 0
        sett = set()

        for i in range(len(s)):
            while s[i] in sett:
                sett.remove(s[left])
                left += 1
                
            m = (i - left) + 1
            maximum = max(maximum,m)
            sett.add(s[i])
        return maximum
            

