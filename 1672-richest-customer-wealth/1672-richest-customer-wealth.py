class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m=0
        for i in range(len(accounts)):
            a=sum(accounts[i])
            if m<a:
                m=a
        return m