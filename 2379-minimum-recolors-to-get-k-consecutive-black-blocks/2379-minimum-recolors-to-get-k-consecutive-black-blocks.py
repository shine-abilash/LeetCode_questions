class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        b=[]
        for i in range(len(blocks)-k+1):
            a=blocks[i:i+k].count('W')
            b.append(a)
        return min(b)