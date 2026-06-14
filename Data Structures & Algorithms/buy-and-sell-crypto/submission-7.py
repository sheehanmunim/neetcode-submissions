class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #do this by checking first and second and subtract first and sees the best out of them all


        best = 0

        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] - prices[i] >= best:
                    best = (prices[j] - prices[i])

        return best