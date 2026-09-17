class Solution:
    def maxDistance(self, arrays: list[list[int]]) -> int:
        answer = 0

        minimum = arrays[0][0]
        maximum = arrays[0][-1]

        for i in range(1, len(arrays)):
            current_min = arrays[i][0]
            current_max = arrays[i][-1]

            answer = max(answer, current_max - minimum)
            answer = max(answer, maximum - current_min)

            minimum = min(minimum, current_min)
            maximum = max(maximum, current_max)

        return answer