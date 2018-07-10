# 150. 买卖股票的最佳时机 II
# 假设有一个数组，它的第i个元素是一个给定的股票在第i天的价格。设计一个算法来找到最大的利润。你可以完成尽可能多的交易(多次买卖股票)。然而,你不能同时参与多个交易(你必须在再次购买前出售股票)。
#
# 样例
# 给出一个数组样例[2,1,2,0,1], 返回 2

class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        if not prices:
            return 0
        min = prices[0]
        max = min
        res = 0

        for i in prices:
            if i < max:
                res = res + max - min
                max = min = i
            else:
                max = i
        res = res + max - min
        return res
        # write your code here
