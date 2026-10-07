class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        a=0
        for i in range(len(nums)):
            if i<len(nums)-1 and nums[i]==nums[i+1]:
                continue
            else:
                nums[a]=nums[i]
                a+=1
        return a

        