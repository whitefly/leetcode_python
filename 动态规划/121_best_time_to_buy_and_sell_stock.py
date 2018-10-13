class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        思想:简单动态规划. 每个位置需要知道的值: 它右边最大的值.
        所以一直从右向左扫,找出每个点的右边最大值
        时间复杂度: O(n)
        """
        max_num, result = 0,0
        for num in prices[::-1]:
            max_num = max(num, max_num)
            result = max(result, max_num - num)
        return result


if __name__ == '__main__':
    my_nums = [7, 6, 4, 3, 1]
    s = Solution()
    print(s.maxProfit(my_nums))
