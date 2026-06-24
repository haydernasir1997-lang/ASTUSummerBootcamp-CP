class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        low = []
        high = []
        mid = []
        for i in nums:

            if i < pivot:
                low.append(i)
            elif i == pivot:
                mid.append(i)
            elif i > pivot:
                high.append(i)

        srt = sorted(low)
        result = low + mid + high
         
        return result
