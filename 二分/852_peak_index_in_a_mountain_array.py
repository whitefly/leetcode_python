class Solution:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        思入: 利用二分,根据循环不变式来缩小范围.
        """
        l, r = 0, len(A) - 1
        mid = 0
        while r - l + 1 >= 1:
            mid = (r + l) // 2
            if A[mid] < A[mid + 1]:
                l = mid + 1
            elif A[mid] < A[mid - 1]:
                r = mid - 1
            else:
                return mid
        return mid


class Solution1:
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        思入: 利用python自带的优化过的max和index来得到索引. 虽然复杂度高比二分高,但是优化过,速度一般
        """
        return A.index(max(A))
