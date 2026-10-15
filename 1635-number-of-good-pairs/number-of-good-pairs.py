class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        count=0
        seen={}
        for num in nums:
            if num in seen:
                count+=seen[num]
                seen[num]+=1
            else:
                seen[num]=1
        return count
        