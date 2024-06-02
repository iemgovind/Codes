# Approach 1 : using two for loops
# will give TLE
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > maxProfit:
                    maxProfit = profit
        return maxProfit
# Version 2 : 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                maxProfit = max(maxProfit, prices[j] - prices[i])
        return maxProfit
    
# Approach 2: Using min Price so far
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0
        for price in prices:
            if price < minPrice:
                minPrice = price
            profit = price - minPrice
            if profit > maxProfit:
                maxProfit = profit
        return maxProfit
#version : 1.1:
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < minPrice:
                minPrice = prices[i]
            profit = prices[i] - minPrice
            if profit > maxProfit:
                maxProfit = profit
        return maxProfit
# Version 2 : using built-in min an dmax
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = prices[0]
        for i in range(1, len(prices)):
            minPrice = min(minPrice, prices[i])
            profit = prices[i] - minPrice
            maxProfit = max(maxProfit, profit)
        return maxProfit