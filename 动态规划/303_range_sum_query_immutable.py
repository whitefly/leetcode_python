class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.dp = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.dp[i] = self.dp[i - 1] + nums[i]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        思想: dp+ 对dp的重组来表示另一种数据.即 低维dp组合表示高维dp
        """
        return self.dp[j] - self.dp[i - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
if __name__ == '__main__':
    my_nums = [-2, 0, 3, -5, 2, -1]
    s = NumArray(my_nums)
    print(s.sumRange(2, 5))
