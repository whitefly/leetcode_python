class Solution1:
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


class Solution:
    def threeSum(self, nums: list):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        思想: 先排序(第一个数去重),转为2sum(使用2指针来,左指针为数2,右指针为数3. 若符合条件,开始去重.始终保持 数1<=数2<=数3)
        """
        nums.sort()
        result = []
        for i, v1 in enumerate(nums):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            target = -v1
            left, right = i + 1, len(nums)-1
            while left < right:
                if nums[left] + nums[right] == target:
                    result.append((v1, nums[left], nums[right]))
                    # 数2和数3去重
                    while left < right and nums[left + 1] == nums[left]:
                        left += 1
                    while left < right and nums[right - 1] == nums[right]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
        return result


if __name__ == '__main__':
    s = Solution()
    my_nums = [-1,0,1,2,-1,-4]
    print(s.threeSum(my_nums))
