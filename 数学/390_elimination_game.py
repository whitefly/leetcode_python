class Solution:
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        思入: 先通过暴力法来求出最后剩下的数. 然后找规则得出 数学公式
        """
        nums = list(range(1, n + 1))
        direction = 0  # 控制方向, 左为0,右为1
        while len(nums) != 1:
            if direction == 0:
                nums = nums[1::2]
                direction = 1
            else:
                nums = nums[-2:-1:2]
                direction = 0
        return nums[0]


if __name__ == '__main__':
    s = Solution()
    print(s.lastRemaining(20))
