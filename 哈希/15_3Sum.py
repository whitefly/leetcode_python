class Solution:
    def threeSum(self, nums: list):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        思想: 先排序(去重),定第一个,在第2,3中寻找.转为2sum. 但是使用hash无法实现去2sum的去重
        """
        nums.sort()
        result = []
        for i, v1 in enumerate(nums):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            else:
                target = -v1
                my_set = set()
                for v in nums[i + 1:]:
                    if v in my_set:
                        result.append([v1, v, target - v])
                        my_set.remove(v)
                    else:
                        my_set.add(target - v)
        return result


if __name__ == '__main__':
    s = Solution()
    my_nums = [0, 2, 2, 3, 0, 1, 2, 3, -1, -4, 2]
    print(s.threeSum(my_nums))
