class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()

        sign = 1
        if s and s[0] == '-':
            sign = -1
            s = s[1:]
        elif s and s[0] == '+':
            s = s[1:]

        num = 0

        for ch in s:
            if not ch.isdigit():
                break

            num = num * 10 + int(ch)

        num *= sign

        if num < -2147483648:
            return -2147483648

        if num > 2147483647:
            return 2147483647

        return num
