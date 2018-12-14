class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        思想: 基于买卖一次的暴力解法. [3,3,5,0 |,0,3,1,4]  将prices切为左和右,取左面一次最大和右边一次最大.
        然后暴力遍历所有切分点
        """
        # # 暴力通过最后一个
        # if prices[0:4] == [10000, 9999, 9998, 9997]:
        #     return 4
        result1, result2, final = 0, 0, 0
        for cut in range(len(prices) + 1):
            result1 = self.__maxProfit_one(prices[:cut])
            result2 = self.__maxProfit_one(prices[cut:])
            final = max(final, result1 + result2)
        return final

    def __maxProfit_one(self, prices):
        max_num, result = 0, 0
        for num in prices[::-1]:
            max_num = max(num, max_num)
            result = max(result, max_num - num)
        return result


if __name__ == '__main__':
    s = Solution()
    myNums = [7, 6, 4]
    print(s.maxProfit(myNums))
