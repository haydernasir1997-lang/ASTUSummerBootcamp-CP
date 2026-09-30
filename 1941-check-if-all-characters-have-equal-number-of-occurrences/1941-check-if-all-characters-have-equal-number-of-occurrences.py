class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = {}

        for ch in s:
            if ch not in count:
                count[ch] = 1
            else:
                count[ch] += 1

        values = list(count.values())

        for i in range(1, len(values)):
            if values[i] != values[0]:
                return False

        return True