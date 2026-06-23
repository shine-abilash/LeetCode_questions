class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        r=[]
        for i in range(len(nums)):
            if nums[i]!=val:
                r.append(nums[i])
        for i in range(len(r)):
            nums[i]=r[i]
        return len(r)