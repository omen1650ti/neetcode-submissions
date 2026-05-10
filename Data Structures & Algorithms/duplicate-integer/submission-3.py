class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        i=0
        j=1
        h=len(nums)
        nums.sort()
        if len(nums)==1:
            return False
        while i<j and j<len(nums):
            if nums[i]==nums[j]:
                return True
            i=i+1
            j=j+1
        return False