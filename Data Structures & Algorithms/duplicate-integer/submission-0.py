class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        k=[]
        for item in nums:
            if item in k:
                
                return True
            k.append(item)
        return False



         