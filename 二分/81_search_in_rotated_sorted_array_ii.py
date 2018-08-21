class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        思入: 由于出现了重复元素,需要对形状进行拆分. 由于左右点重组,需要先去重. 若r和l相同,默认去掉右边的重复
        待优化: 过程太复杂,看看能不能简化流程
        """
        if not nums:
            return False
        l, r = 0, len(nums) - 1
        while nums[l] == nums[r] and l < r:
            # 去掉重复
            r -= 1
        while l <= r:
            mid = (l + r) // 2
            temp = nums[mid]
            if nums[mid] == target:
                return True
            if nums[l] < nums[r]:
                # 正序形状,普通二分
                if temp < target:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                # 锯齿或者长方形
                if nums[l] <= temp:
                    # mid在左边
                    if temp < target:
                        # mid<target<顶点
                        l = mid + 1
                    else:
                        if nums[l] == target:
                            return True
                        if nums[l] < target:
                            # l<target<mid
                            r = mid - 1
                        else:
                            l = mid + 1
                elif temp <= nums[r]:
                    # mid在右边
                    if target < temp:
                        # 顶<target<mid
                        r = mid - 1
                    else:
                        if target == nums[r]:
                            return True
                        if target < nums[r]:
                            # mid < target<右
                            l = mid + 1
                        else:
                            # 左<target<mid
                            r = mid - 1
        return False


if __name__ == '__main__':
    my_nums = [1]
    my_target = 1
    s = Solution()
    print(s.search(my_nums, my_target))
