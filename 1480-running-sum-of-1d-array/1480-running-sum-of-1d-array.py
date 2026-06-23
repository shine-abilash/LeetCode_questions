class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s=0
        a=[]
        for i in range(len(nums)):
            s=s+nums[i]
            a.append(s)
        return a