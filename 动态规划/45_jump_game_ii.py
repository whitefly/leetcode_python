class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        思入: 开始以为是贪心,不过才是很需要后面的内容才能确定前面的. 所以采用 dp暴力扫.
        状态量: 到该点所需要的最小步数
        缺点: 有大量无效计算,导致最后一个测试例子超时.提交失败
        """
        if len(nums) == 1:
            return 0
        dp = [0] + [2147483647] * (len(nums) - 1)
        for index1, v1 in enumerate(nums):
            temp = dp[index1] + 1
            for index2 in range(index1 + 1, index1 + v1 + 1):
                dp[index2] = min(temp, dp[index2])
                if index2 == len(nums) - 1:
                    return dp[index2]
        return dp[-1]


class Solution1:
    def jump(self, nums):
        """
        思入2: 在dp的基础上进行优化,对覆盖点选出能跳出最远的(即最优点). 然后直接跳到最优点(减少无效遍历),然后对最优点的覆盖点进行筛选.
        暴力dp转换为贪心
        """
        if len(nums) == 1:
            return 0
        step, most_index = 0, 0
        for index1, v1 in enumerate(nums):
            if index1 < most_index:
                # 跳到最优点
                continue
            most_far = -1
            step += 1
            for index2 in range(index1 + 1, index1 + v1 + 1):
                # 选出覆盖点跳的最远的作为新的最优点
                if index2 == len(nums) - 1:
                    return step

                temp_far = nums[index2] + index2
                if temp_far >= most_far:
                    most_far, most_index = temp_far, index2
        return step


if __name__ == '__main__':
    s = Solution()
    my_nums = [1, 2, 1, 1, 1]
    print(s.jump(my_nums))
