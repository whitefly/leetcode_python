class Solution:
    def nextPermutation(self, nums: list):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        思入:  1,3,2的下一个大点数为 2,1,3
        首先从右向左找到第一个逆序数.即1. 然后已经扫过的从大到小的数中(3,2),找到比一个逆序数大点的数(即2),然后交换到逆序数(2,3,1). 此时右边还是正序(3,1),变为最小(即反向为1,3). 所以最后结果为 2,1,3
        """
        # 从右向左找到异常点last
        last = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i != len(nums) - 1 and nums[i] < nums[i + 1]:
                last = i
                break
        else:
            nums.reverse()
            return

        # 找出比nums[last]大一点的数,并替换
        for i in range(len(nums) - 1, last, -1):
            if nums[i] > nums[last]:
                # 换位
                nums[i], nums[last] = nums[last], nums[i]
                break

        # 将剩下部分变为最小
        nums[last + 1:] = reversed(nums[last + 1:])


if __name__ == '__main__':
    my_a = [1, 3, 2]
    s = Solution()
    print(s.nextPermutation(my_a))
