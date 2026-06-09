class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #buy one day and sell the next day
        #brute force method take the first and then see if large and set a target

        best = 0


        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if (prices[j] - prices[i]) > best:
                    best = (prices[j] - prices[i])
        return best