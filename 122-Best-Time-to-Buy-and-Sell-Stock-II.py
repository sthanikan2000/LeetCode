class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left = 0
        for i in range(1,len(prices)):
            if prices[left]<prices[i]:
                profit += prices[i] - prices[left]
            left = i
            
        return profit