class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def dfs(curr,opn,close):
            if len(curr)==n*2:
                res.append(curr)
                return
            if opn<n:
                dfs(curr+'(',opn+1,close)
            if close<opn:
                dfs(curr+')',opn,close+1)
        dfs('',0,0)
        return res