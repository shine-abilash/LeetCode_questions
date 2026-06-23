class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        c=0
        for i in range(len(nums)):
            s=str(nums[i])
            if len(s)%2==0:
                c=c+1
        return c