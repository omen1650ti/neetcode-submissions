class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        k=len(nums)
        print(k)

        su=(k*(k+1) ) // 2
        ku=sum(nums)

        return su - ku
        