class Solution:
    def threeSumClosest(self, nums: list, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        思入: 3sum和的变种,同样使用二指针.由于说明正确答案只有一个,所以不考虑去重.  用来一个变量来记录最小差距gap即可
        """
        nums.sort()
        gap = 999999
        for i, n1 in enumerate(nums):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            target_2 = target - n1
            l, r = i + 1, len(nums) - 1
            while r - l + 1 > 1:
                my_sum = nums[l] + nums[r]
                if my_sum < target_2:
                    l += 1
                elif my_sum > target_2:
                    r -= 1
                else:
                    return target
                gap = gap if abs(gap) < abs(target_2 - my_sum) else target_2 - my_sum

        return target - gap


if __name__ == '__main__':
    s = Solution()
    my_nums = [-1, 2, 1, -4]
    print(s.threeSumClosest(my_nums, target=1))
