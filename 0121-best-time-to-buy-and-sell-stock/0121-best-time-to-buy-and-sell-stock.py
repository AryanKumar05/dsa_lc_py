class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        buy=prices[0]
        for price in prices:
            buy=min(buy,price)
            max_profit=max(max_profit,price-buy)
        return max_profit






    # /inefficient sol below
        # n = len(prices)
        # if n < 2:
        #     return 0

        # max_profit = 0

        # for j in range(n - 1):
        #     min_buy = prices[j]
        #     for i in range(j + 1, n):
        #         max_profit = max(max_profit, prices[i] - min_buy)

        # return max_profit
