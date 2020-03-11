from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 快慢指针来寻找环   下标为node, 值为next节点的下标. 一定会有环
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow1 = 0
        while True:
            slow = nums[slow]
            slow1 = nums[slow1]
            if slow == slow1:
                return slow1


if __name__ == '__main__':
    nums = [3, 1, 3, 4, 2]
    s = Solution()
    rnt = s.findDuplicate(nums)
    print(rnt)
