class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        if len(nums)<=1:
            return False
        i=0
        j=1
        while j<len(nums):
            if nums[i] != nums[j]:
                i=i+1
                j=j+1
            else:
                return True
        return False

      