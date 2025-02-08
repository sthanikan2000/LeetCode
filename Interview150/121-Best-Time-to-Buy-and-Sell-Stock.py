class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left = 0
        for i in range(1,len(prices)):
            if prices[left]<prices[i]:
                max_profit = max( prices[i] - prices[left],max_profit)
            else:
                left = i
        return max_profit

        



        