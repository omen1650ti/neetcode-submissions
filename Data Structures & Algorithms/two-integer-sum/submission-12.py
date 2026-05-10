class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        k=[]
        m=[]
        for i,val in enumerate(nums):
            k.append([val,i])
        k.sort()
        i=0
        j=len(nums)-1
        while i<j:
            su = k[i][0] + k[j][0]
            if su == target:
                return [min(k[i][1],k[j][1]) , max(k[i][1],k[j][1])]
            elif su > target:
                j=j-1
            else:
                i=i+1
        return []


        