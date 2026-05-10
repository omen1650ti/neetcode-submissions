class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefi=[]
        re=1
        for i in range(0,len(nums)):
            if i == 0:
                prefi.append(1)
            else:
                re=re*nums[i-1]
                prefi.append(re)
        suffi=[]
        print(prefi)
        me=1
        for j in range(len(nums)-1,-1,-1):
            if j==len(nums)-1:
                suffi.append(1)
            else:
                me=me*nums[j+1]
                suffi.append(me)
        suffi.reverse()
        print(suffi)

        for i in range(0,len(prefi)):
            if prefi[i]==None or suffi[i]==None:
                continue
            else:
                prefi[i]=prefi[i]*suffi[i]
        return prefi


