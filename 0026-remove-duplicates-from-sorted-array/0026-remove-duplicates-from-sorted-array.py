from collections import Counter
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a=Counter(nums)
        r=[]
        for i in a.keys():
            r.append(i)
        for i in range(len(r)):
            nums[i]=r[i]
        return len(r)