class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def find(s,opn,clo):
            if len(s)==n*2:
                res.append(s)
                return
            if opn<n:
                find(s+'(',opn+1,clo)
            if clo<opn:
                find(s+')',opn,clo+1)

        find('',0,0)
        return res