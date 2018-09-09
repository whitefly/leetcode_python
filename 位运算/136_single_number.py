class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        思入: 入门的位运算(异或去重)
        """
        from functools import reduce
        return reduce(lambda x, y: x ^ y, nums)


if __name__ == '__main__':
    s = Solution()
    my_nums = [1, 1, 2, 3, 2]
    print(s.singleNumber(my_nums))
