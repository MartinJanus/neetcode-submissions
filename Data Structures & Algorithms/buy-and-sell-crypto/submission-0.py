class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        #

        # Input: prices = [10,1,5,6,7,1]


        # Left = 10
        # Right = 10

        # Right = 1 

        left = 0 
        right = 0
        maxProfit = 0


        # profit = right - left

        # #10 - 10 = 0 
        # profit = 0 

        # # if right is less than or equal to left, we move right over +1, else we move left
        # # 1 - 10 = -9 
        # move left 
        # # 1 - 1 = 0 
        # move right 
        # 

        # check if profit is greater than previous profit produced by left and right 

        # for i in range(len(prices)):
        while right < len(prices):
                if prices[left] < prices[right]:
                    profit = prices[right] - prices[left]
                    maxProfit = max(maxProfit, profit)
                else:
                    left = right
                
                right+=1

        return maxProfit

