class Solution:
    def lengthOfLastWord(self, s: str) -> int:
            s1 = s.strip()
            count = 0
            indx = -1
            for i in range(len(s1)):
                if s1[indx] != " ":
                    count += 1
                    indx -= 1
                else:
                    break
            return count