class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        remaining=0
        for n in data:
            if remaining>0:
                if (n>>6)!=0b10:
                    return False
                remaining-=1
            elif (n>>7)==0:
                remaining=0
            elif (n>>5)==0b110:
                remaining=1
            elif (n>>4)==0b1110:
                remaining=2
            elif (n>>3)==0b11110:
                remaining=3
            else:
                return False
        return remaining==0