class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        思入: 由于数组的形式有2种(正序和2个正序).所以需要写2种二分.普通二分和特殊2分
        """
        l, r = 0, len(nums) - 1
        while r - l + 1 >= 1:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            if nums[l] < nums[r]:
                # 正常二分
                if nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                # 特殊二分
                if target < nums[mid]:
                    # 有3种可能
                    if nums[mid] <= nums[r]:
                        r = mid - 1
                    else:
                        if target >= nums[l]:
                            r = mid - 1
                        else:
                            l = mid + 1
                else:
                    if nums[mid] >= nums[l]:
                        l = mid + 1
                    else:
                        if target <= nums[r]:
                            l = mid + 1
                        else:
                            r = mid - 1

        return -1


if __name__ == '__main__':
    s = Solution()
    my_nums = [3, 1]
    print(s.search(my_nums, 1))
