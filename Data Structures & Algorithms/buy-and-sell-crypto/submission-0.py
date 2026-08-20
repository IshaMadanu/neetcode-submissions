class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        minimum = prices[0]

        for i in range(len(prices)):
            minimum = min(minimum, prices[i])

            curr = prices[i] - minimum
            maxProfit = max(maxProfit, curr)

        return maxProfit