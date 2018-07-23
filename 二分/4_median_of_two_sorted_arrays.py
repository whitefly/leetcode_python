class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        思想: 在数组1上任意切一刀作为左1和右1, 由于是中位数,数组2上的一刀是根据数组1的一刀切(原理:保证2个左边的数量 == 2个右边的数量.所以可以算出出来)
        所以: 只要保证第一个数组上的一刀正确即可. 核心: 怎么保证这一刀是正确的? 所有的左边 <= 所有的右边 即  max(L1,L2)<=min(R1,R2).
        一旦出现其他情况,就要大小来调整切的位置(二分)
        复杂度: 只在最小数组上进行二分--->O(log(min(m+n)))
        """
        # 确定最小数组
        left, right, nums_small, nums_big = (0, len(nums1), nums1, nums2) if len(nums1) <= len(nums2) else (
            0, len(nums2), nums2, nums1)
        size = len(nums1) + len(nums2)
        while left <= right:
            cut1 = (left + right) // 2
            cut2 = size // 2 - cut1  # 算出第2刀位置

            # 为什么切在2端时,要选择赋值最小 or 最大值? 并不影响. 因为最后有一个min和max操作. 极值是不会被取到的
            L1 = -99999999 if cut1 == 0 else nums_small[cut1 - 1]
            R1 = 99999999 if cut1 == len(nums_small) else nums_small[cut1]
            L2 = -99999999 if cut2 == 0 else nums_big[cut2 - 1]
            R2 = 99999999 if cut2 == len(nums_big) else nums_big[cut2]
            # 二分来求出正确切点
            if L1 > R2:
                right = cut1 - 1
            elif L2 > R1:
                left = cut1 + 1
            else:
                if size % 2 == 0:
                    return (max(L1, L2) + min(R1, R2)) / 2
                else:
                    return min(R1, R2)  # 为什么是R1和R2进行比较,而不是L1,L2比较? youtube上讲解时并没有解释


class Solution1:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        暴力写法: 直接合并+排序,然后根据奇偶取出中位数
        :param nums1:
        :param nums2:
        :return:
        复杂度: O((m+n)log(m+n))
        """
        nums1 = nums1 + nums2  # type:list
        nums1.sort()
        median_i = len(nums1) // 2
        return (nums1[median_i - 1] + nums1[median_i]) / 2 if len(nums1) % 2 == 0 else nums1[median_i]


if __name__ == '__main__':
    nums_1 = [1, 3]
    nums_2 = [2]
    s = Solution()
    print(s.findMedianSortedArrays(nums_1, nums_2))
