class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        d=[]
        for i in range(0,len(nums)-1):
            j=i+1
            k=len(nums)-1
            while j < k:
                if nums[i]+nums[j]+nums[k]<0:
                    j=j+1
                elif nums[i]+nums[j]+nums[k]>0:
                    k=k-1
                else:
                    m=[nums[i],nums[j],nums[k]]
                    m.sort()
                    if m not in d:
                        d.append(m)
                        
                    j=j+1
                    k=k-1
        return d
                


