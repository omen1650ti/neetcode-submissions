class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=1
        p=[]
        suffix=1
        s=[]
        for i in range(0,len(nums)):
            if i==0:
                prefix=1
            else:

                prefix = prefix * nums[i-1]
            p.append(prefix)
        for j in range(len(nums)-1,-1,-1):
            if j==len(nums)-1:
                suffix=1
            else:
                suffix = suffix * nums[j+1]
            s.append(suffix)
        s.reverse()
        print(s)
        print(p)
        for k in range(0,len(s)):
            nums.append(s[k] * p[k])
        return nums[len(s):]
        

         

            