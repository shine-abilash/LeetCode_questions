class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        c=0
        for i in range(len(s)-1,-1,-1):
            if s[i]==' ':
                break
            c+=1
        return c