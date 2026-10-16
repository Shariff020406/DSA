class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        ans=max(accounts,key=sum)
        return sum(ans)

        