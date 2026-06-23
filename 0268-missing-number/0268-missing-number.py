class Solution(object):
    def missingNumber(self, nums):
        l=len(nums)
        for i in range(l+1):
            if i not in nums:
                return i