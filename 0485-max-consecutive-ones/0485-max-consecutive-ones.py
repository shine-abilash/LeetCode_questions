class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        m=0
        for i in nums:
            if i==1:
                c=c+1
                m=max(c,m)
            else:
                c=0
        return m