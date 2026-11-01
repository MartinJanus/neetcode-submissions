class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 
        right = 1 
        result = 0

        while right < len(prices):
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                result = max(result, profit)
            else:
                left = right
            
            right+=1

        return result


            # 7-7 = 0
