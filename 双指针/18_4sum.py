from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # 思入: 排序+双指针
        nums.sort()
        result = []
        for index1, num1 in enumerate(nums):
            if index1 != 0 and nums[index1 - 1] == nums[index1]:
                continue
            for index2 in range(index1 + 1, len(nums)):
                if index2 != index1 + 1 and nums[index2 - 1] == nums[index2]:
                    continue
                # 前后相碰
                num2 = nums[index2]
                index3 = index2 + 1
                index4 = len(nums) - 1
                while index3 < index4:
                    temp_sum = num1 + num2 + nums[index3] + nums[index4]
                    if temp_sum == target:
                        result.append([num1, num2, nums[index3], nums[index4]])
                        index3 += 1
                        index4 -= 1
                        while index3 < index4 and nums[index3 - 1] == nums[index3]:
                            index3 += 1
                        while index3 < index4 and nums[index4 + 1] == nums[index4]:
                            index4 -= 1
                    elif temp_sum < target:
                        index3 += 1
                    else:
                        index4 -= 1
        return result


if __name__ == '__main__':
    nums = [0, 0, 0, 0, 0, 0]
    target = 00
    solver = Solution()
    rnt = solver.fourSum(nums, target)
    print(rnt)
