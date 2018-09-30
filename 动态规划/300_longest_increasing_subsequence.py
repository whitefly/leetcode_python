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

    def lengthOfLIS(self, nums):
        """
        思入2: 在思入1的基础上,在扫过之后,对前面只是一个搜索过程,而不用管顺序,需要可以在此时写一个二分搜索
        :param nums:
        :return:
        """


if __name__ == '__main__':
    s = Solution()
    my_nums = [10, 9, 2, 5, 3, 7, 101, 18]
    print(s.lengthOfLIS(my_nums))
