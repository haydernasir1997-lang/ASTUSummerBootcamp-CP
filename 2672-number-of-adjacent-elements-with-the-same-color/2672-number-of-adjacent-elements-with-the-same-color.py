class Solution:
    def colorTheArray(self, n: int, queries: list[list[int]]) -> list[int]:
        nums = [0] * n
        ans = []
        count = 0

        for index, color in queries:

            # Remove the old pairs
            if index > 0 and nums[index] != 0:
                if nums[index] == nums[index - 1]:
                    count -= 1

            if index < n - 1 and nums[index] != 0:
                if nums[index] == nums[index + 1]:
                    count -= 1

            # Change the color
            nums[index] = color

            # Add the new pairs
            if index > 0:
                if nums[index] == nums[index - 1]:
                    count += 1

            if index < n - 1:
                if nums[index] == nums[index + 1]:
                    count += 1

            ans.append(count)

        return ans