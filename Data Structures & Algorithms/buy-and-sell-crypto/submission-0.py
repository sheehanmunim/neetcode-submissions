class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        valMain = 0
        val = 0
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                val = prices[j] - prices[i]
                if valMain < val:
                    valMain = val
        return valMain

