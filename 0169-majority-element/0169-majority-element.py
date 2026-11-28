from collections import Counter
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        c=Counter(nums)
        n=len(nums)//2
        for i,j in c.items():
            if j>n:
                return i
            