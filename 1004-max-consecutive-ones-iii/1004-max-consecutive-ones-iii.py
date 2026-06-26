class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        z=0
        m=0
        l=0
        for i in range(len(nums)):
            if nums[i]==0:
                z=z+1
            while z>k:
                if nums[l]==0:
                    z=z-1
                l=l+1
            m=max(m,i-l+1)
        return m