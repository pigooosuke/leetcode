from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        max_len = len(prices)
        for i in range(len(prices)):
            head = i
            tail = max_len - 1
            if head+1 < max_len and prices[head] >= prices[head+1]:
                continue
            if profit != 0 and profit < prices[head]:
                continue
            while head < tail:
                if profit > prices[tail]:
                    tail -= 1
                    continue
                if head < tail and prices[tail-1] >= prices[tail]:
                    tail -= 1
                    continue
                profit = max(profit, prices[tail]-prices[head])
                tail -= 1
        return profit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float(inf)
        profit = 0
        for n in range(len(prices)):
            if prices[n] < min_price:
                min_price = prices[n]
            elif prices[n] - min_price > profit:
                profit = prices[n] - min_price

        return profit


solution = Solution()
ans = solution.maxProfit(prices=[7, 1, 5, 3, 6, 4])
print(f"{ans=}")
