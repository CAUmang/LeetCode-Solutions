class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) <= 1:
            return 0
        buy_idx, sell_idx, min_idx, ans = 0, 1, 0, 0
        while sell_idx < len(prices):
            if prices[buy_idx] > prices[min_idx]:
                buy_idx = min_idx
            ans = max(ans, prices[sell_idx]-prices[buy_idx])
            if prices[min_idx] > prices[sell_idx]:
                min_idx = sell_idx
            sell_idx += 1
        return ans
        
        
        
#         j = 0
#         max_profit = float("-inf")
#         for i in range(len(prices)):
#             if prices[i] < prices[j]:
#                 curr_profit = prices[j] - prices[i]
#                 max_profit = max(max_profit, curr_profit)
#                 j += 1
#             else:
#                 j += 1
                
#         if max_profit > 0:
#             return max_profit
#         else:
#             return 0