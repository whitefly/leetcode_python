class Solution:
    def partition(self, nums: list, low, high):
        """
        思想: 本质是交换, low为最后要确定位置的元素.
        快速的思想不是找到2个可以交换的元素,而是确保l的左边都<=key(不包括l),key<=r的右边(不包括r)
        :param nums:
        :return:
        """
        l, r = low, high
        key = nums[low]
        while True:
            while key <= nums[r]:  # 为了防止越界,l<r?
                r -= 1
                if r == low:
                    break
            while nums[l] <= key:
                l += 1
                if l == high:
                    break

            if l >= r:
                nums[low], nums[r] = nums[r], nums[low]
                return r
            else:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

    def __sort(self, nums, low, high):
        if low >= high:
            return
        index = self.partition(nums, low, high)
        print(index)
        self.__sort(nums, low, index - 1)
        self.__sort(nums, index + 1, high)

    def sort(self, nums):
        self.__sort(nums, 0, len(nums) - 1)


if __name__ == '__main__':
    s = Solution()
    my_nums = [6, 7, 4, 2, 9, 3, 5, 8, 1, 2]
    # my_nums = [2, 1]
    print(my_nums)
    s.sort(my_nums)
    print(my_nums)
