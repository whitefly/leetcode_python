from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 存储和扫描指针
        store_index = 0
        count = 0
        for v in nums:
            if v != val:
                nums[store_index] = v
                count += 1
                store_index += 1
        return count


if __name__ == '__main__':
    nums = [3, 2, 2, 3]
    val = 3
    solver = Solution()
    result = solver.removeElement(nums, val)
    print(result)
    print(nums)
