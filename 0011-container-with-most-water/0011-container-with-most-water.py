class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        m=0
        while l<r:
            w=r-l
            v=w*min(height[l],height[r])
            m=max(m,v)
            if height[l]>height[r]:
                r=r-1
            else:
                l=l+1
        return m