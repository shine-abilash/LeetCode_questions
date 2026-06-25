from collections import Counter
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        i=0
        seen = set()
        m=0
        t=0
        for j in range(len(nums)):
            while nums[j] in seen:
                seen.remove(nums[i])
                t=t-nums[i]
                i=i+1
            seen.add(nums[j])
            t=t+nums[j]
            if j-i+1==k:
                m=max(m,t)
                t=t-nums[i]
                seen.remove(nums[i])
                i=i+1
        return m