class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        思入: 和 26:删除排序数组中的重复项 的思入一样
        但是本题要求每个元素最多出现两次.所以用一个状态来表示这个货出现了几次,然后在考虑是否放在index的坑
        """
        if len(nums) <= 1:
            return len(nums)
        index, count = 0, 0
        for i, v in enumerate(nums):
            if i == 0 or v != nums[index - 1]:
                # 不同的元素,直接加入
                count = 1
                nums[index] = v
                index += 1
            else:
                if count == 1:
                    # 相同元素,之前只有1个才加
                    nums[index] = v
                    index += 1
                    count += 1
        return index


if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 2, 3, 3, 3]
    print(s.removeDuplicates(nums))
    print(nums)
