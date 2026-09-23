class Solution:
    def stoneGameIX(self, stones: list[int]) -> bool:

        count = [0, 0, 0]

        for stone in stones:
            count[stone % 3] += 1

        def check(count):
            if count[1] == 0:
                return False

            count[1] -= 1

            turns = 1 + min(count[1], count[2]) * 2

            if count[1] > count[2]:
                count[1] -= 1
                turns += 1

            turns += count[0]

            return turns % 2 == 1 and count[1] != count[2]

        first = count[:]
        second = [count[0], count[2], count[1]]

        return check(first) or check(second)