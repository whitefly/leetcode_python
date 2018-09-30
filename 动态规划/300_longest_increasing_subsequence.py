class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        思入1:动态规划, 状态量: 包含该点的最长上升子序列的长度。
        复杂度: 时间O(n^2)
        """
        result = 0
        dp = [0] * len(nums)
        for i, v2 in enumerate(nums):
            if i == 0:
                dp[i] = 1
            else:
                # 找到最大的且可以跟的,拼接在后面
                max_count = 0
                for j, v1 in enumerate(nums[:i]):
                    if v1 < v2 and max_count < dp[j]:
                        max_count = dp[j]
                    dp[i] = max_count + 1 if max_count else 1
            result = max(result, dp[i])
        return result

    def lengthOfLIS2(self, nums):
        """
        思入2: 贪心+二分搜索
        定义d[k]:长度为k的上升子序列的最末元素，若有多个长度为k的上升子序列，则记录最小的那个最末元素.
        核心:维护一个递增的dp,二分搜索后可能出现替换
        :param nums:
        :return:
        """
        import bisect
        dp = [0] * (len(nums) + 1)
        size = 0
        for i, v in enumerate(nums):
            index = bisect.bisect_left(dp, v, 1, size + 1)
            size = size + 1 if index == size + 1 else size
            dp[index] = v
        return size


if __name__ == '__main__':
    s = Solution()
    my_nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(s.lengthOfLIS2(my_nums))
