class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        思入1: 暴力排序 o(nlogn)
        带优化: 有木有线性的方法
        """
        nums.sort()


class Solution1:
    def sortColors(self, nums):
        """
        思入1:  由于要使用线性的方法,所以不能排序.
        由于元素种类有限,直接计算count,然后重写数组
        待优化:有木有只扫一遍的方法?
        """
        counter = [0, 0, 0]
        for i in nums:
            counter[i] += 1
        # 重写数组
        nums[:counter[0]] = [0] * counter[0]
        nums[counter[0]:counter[0] + counter[1]] = [1] * counter[1]
        nums[counter[0] + counter[1]:] = [2] * counter[2]


class Solution2:
    def sortColors(self, nums):
        """
        思入2: 由于只扫一遍,故一遍就需要将位置摆放正确. 就需要交换2个位置,所以需要2个指针. 自然想到双指针
        双指针变动: 0,2时缩小范围. 当都扫到1时,使用第三个指针. 左指针用来存0的坑,右指针用来存2的坑
        """
        l, r = 0, len(nums) - 1
        index = 0
        while l <= r and index < r + 1:
            if nums[index] == 0:
                nums[index], nums[l] = nums[l], nums[index]
                l += 1
                index += 1
            elif nums[index] == 2:
                nums[index], nums[r] = nums[r], nums[index]
                r -= 1
            else:
                index += 1


if __name__ == '__main__':
    my_nums = [1, 2, 0]
    s = Solution2()
    s.sortColors(my_nums)
    print(my_nums)
