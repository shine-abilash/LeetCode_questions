from collections import Counter
import heapq

class Solution(object):
    def majorityElement(self, nums):
        count = Counter(nums)
        a=heapq.nlargest(1, count.keys(), key=count.get)
        return (a[0])