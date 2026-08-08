class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxp = 0
        l = 0
        r = 1
        while r<n:
            if prices[l]<prices[r]:
                p = prices[r]-prices[l]
                maxp = max(maxp, p)
            else:
                l = r
            r+=1    
        return maxp