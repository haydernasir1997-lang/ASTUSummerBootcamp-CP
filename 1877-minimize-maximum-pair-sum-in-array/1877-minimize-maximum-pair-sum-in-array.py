class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        a=0
        b=len(nums)-1
        l=[]
        while a<b:
            l.append(nums[a]+nums[b])
            a+=1
            b-=1
        return(max(l))    