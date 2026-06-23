class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k=k%len(nums)
        print(k)
        nums[:] = nums[-k:]+nums[:-k]
        