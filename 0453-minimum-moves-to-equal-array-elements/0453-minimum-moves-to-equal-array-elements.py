class Solution:
    def minMoves(self, nums: list[int]) -> int:
        m=min(nums)
        d=0
        for i in nums:
            d+=i-m
        return d
        