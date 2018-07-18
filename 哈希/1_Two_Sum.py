class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        my_map = dict()
        for i, v in enumerate(nums):
            if target - v in my_map:
                return i, my_map[target - v]
            else:
                my_map[v] = i


if __name__ == '__main__':
    #测试
    my_nums = [2, 7, 11, 15]
    my_target = 9
    s = Solution()
    print(s.twoSum(my_nums, my_target))
