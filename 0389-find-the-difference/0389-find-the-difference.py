from collections import Counter

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_count = Counter(s)
        t_count = Counter(t)

        for ch in t_count:
            if t_count[ch] > s_count[ch]:
                return ch