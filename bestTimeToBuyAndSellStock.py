class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profitSoFar = 0

        #Time complexity: O(|prices|)
        #Memory complexity: O(1)
        
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            profitSoFar = max(profitSoFar, price - lowest)
        return profitSoFar