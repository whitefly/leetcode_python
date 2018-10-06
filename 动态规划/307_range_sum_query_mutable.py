class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        思入:二维dp降为一维dp表示. 状态量为dp[1]表示 下标为[0,1]数字的和 dp[3]表示下标[0,3]数字的和
        修改某个下标为i的值,将改变dp[i:]的值.同时增加or减少
        缺点: 在更新时会比较慢,最坏达到O(n). 在更新比较多个时候会超时(leetcode上最后一个案例无法通过)
        """
        self._nums = nums
        self._dp = [0] * len(nums)
        for i, num in enumerate(nums):
            self._dp[i] = self._dp[i - 1] + num if i > 0 else num

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        gap = val - self._nums[i]
        self._nums[i] = val
        for j in range(i, len(self._nums)):
            self._dp[j] += gap

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self._dp[j] - self._dp[i] + self._nums[i]


if __name__ == '__main__':
    mynums = [1, 3, 5]
    A = NumArray(mynums)
    print(A.sumRange(0, 2))
    A.update(1, 2)
    print(A.sumRange(0, 2))
