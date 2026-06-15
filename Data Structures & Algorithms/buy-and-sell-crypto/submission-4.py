class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        d = {}
        stocks = [0] * len(prices)
        
        i = 0
        j = i + 1
        while i < len(prices) and j < len(prices):
            if prices[i] >= prices[j]:
                i += 1
                j = i + 1
            else:
                if prices[j] - prices[i] > stocks[i]:
                    stocks[i] = prices[j] - prices[i]
                j += 1
        
        return max(stocks, default = 0)
                    