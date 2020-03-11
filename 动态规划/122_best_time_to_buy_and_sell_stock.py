class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        思想: 贪心算法,扫过一个点时,可以决定买或不卖. 前提是现在是否持有股票.
        所以设置 boolean变量来表明是否持有股票,price来表达持有股票的价格
        策略: 在持有状态下(决定卖不卖),若nums[i]>=nums[i+1],则卖出. 否则跳过
        在非持有状态下,若nums[i]<=nums[i+1],则买nums[i],否则跳过
        """
        haven, cost, result = False, 0, 0
        size = len(prices)
        for i, price in enumerate(prices):
            if haven:
                if i == size - 1 or price >= prices[i + 1]:
                    result += price - cost
                    haven = False
            else:
                if i < size - 1 and price <= prices[i + 1]:
                    haven = True
                    cost = price

        return result

    def maxProfit2(self, prices):
        # 动态规划法 dp[n][s]表示 第n天结束时,处于s状态(0非持有,1持有)的最大收益
        unhold, hold = 0, -100000
        for price in prices:
            new_hold = max(hold, unhold - price)
            new_unhold = max(unhold, hold + price)
            hold, unhold = new_hold, new_unhold
        return unhold


if __name__ == '__main__':
    my_nums = [7, 6, 4, 3, 1]
    s = Solution()
    print(s.maxProfit(my_nums))
    print(s.maxProfit2(my_nums))
