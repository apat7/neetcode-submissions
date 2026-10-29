class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_prof = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                max_prof = max(max_prof, prices[j]-prices[i])

        return max_prof