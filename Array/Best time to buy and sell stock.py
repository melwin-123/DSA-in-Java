# Soution 1

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        for i in prices[1:]:
            if buy > i:
                buy = i
            profit = max(profit,i-buy)
        return profit

# Second solution with less time complexity
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = sell = prices[0]
        oldprofit = 0

        for i in prices[1:]:
            if i < buy :
                buy = i
                sell = i
    
            if i > sell:
                 sell = i
                 newprofit = sell - buy
                 if newprofit > oldprofit:
                    oldprofit = newprofit
        return oldprofit

        
