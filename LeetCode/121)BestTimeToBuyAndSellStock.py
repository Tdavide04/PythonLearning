'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104
'''

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        for e in range(len(prices)):
            min_num = min(prices)
            if min_num == prices[-1] and len(prices) > 1:
                min_num = min(prices[:-1])
            index_num = prices.index(min_num)
            max_num = max(prices[index_num::])
            max_profit = max_num - min_num
        return max_profit
    

if __name__ == "__main__":
    
    sos = Solution()
    print(sos.maxProfit([2,4,1]))
    