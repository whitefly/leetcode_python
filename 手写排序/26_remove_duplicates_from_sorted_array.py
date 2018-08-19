class Solution:
    def removeDuplicates(self, nums: list):
        """
        :type nums: List[int]
        :rtype: int
        思入: 一旦发现有重复,使用自带pop来删除该元素.指针不前进.  若该元素不重复,指针继续向前扫
        复杂度: 时间O(n^2),空间O(1)
        待优化:能不能不使用list.pop()来删除,从而优化时间时间复杂度?
        """
        i = 0
        while i < len(nums):
            if i != 0 and nums[i] == nums[i - 1]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)


class Solution1:
    def removeDuplicates(self, nums: list):
        """
        :type nums: List[int]
        :rtype: int
        思入: 若不使用pop,那就只能对符合条件的元素换位置(换到正确的位置).所以需要最后结果指针变量(作为不重复元素正确的坑位置)
        复杂度: 时间O(n),空间O(1)
        """
        last_index = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                nums[last_index] = nums[i]
                last_index += 1
        return last_index


if __name__ == '__main__':
    my_nums = [1, 1, 2, 3, 3, 4]
    s = Solution1()
    print(s.removeDuplicates(my_nums))
