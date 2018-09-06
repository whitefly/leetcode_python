from functools import cmp_to_key


def cmp(s1, s2):
    return -1 if (int(s1 + s2)) > int((s2 + s1)) else 1


class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        按从左到右排序,然后进行组合join后成为数字
        """
        nums = list(map(str, nums))
        nums = sorted(nums, key=cmp_to_key(cmp))
        a = ''.join(nums)
        return '0' if int(a) == 0 else a


if __name__ == '__main__':
    s = Solution()
    my_nums = [121, 12]
    print(s.largestNumber(my_nums))
