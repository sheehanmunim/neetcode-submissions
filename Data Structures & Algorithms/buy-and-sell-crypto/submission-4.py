class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #look at second and subtract from first and see if its larget than best

        best = 0
        
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[j] - prices[i] > best:
                    best = prices[j] - prices[i]
        return best