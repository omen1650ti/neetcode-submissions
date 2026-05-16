class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        j=i+1
        max1 = 0
        while j>i and j<len(prices):

            if prices[j] > prices[i]:
                k=prices[j] - prices[i]
                max1 = max(max1,k)
                j=j+1
            else:
                j=j+1
            if j==len(prices)-1:
                k=prices[j] - prices[i]
                max1 = max(max1,k)
                i=i+1
                j=i+1
        return max1





            
        
        