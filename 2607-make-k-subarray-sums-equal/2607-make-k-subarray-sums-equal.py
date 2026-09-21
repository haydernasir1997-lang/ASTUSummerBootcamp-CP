from math import gcd

class Solution:
    def makeSubKSumEqual(self, arr: list[int], k: int) -> int:
        n = len(arr)
        g = gcd(n, k)

        answer = 0

        for start in range(g):
            group = []

            i = start

            while i < n:
                group.append(arr[i])
                i += g

            group.sort()

            median = group[len(group) // 2]

            for x in group:
                answer += abs(x - median)

        return answer