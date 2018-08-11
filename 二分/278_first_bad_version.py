def isBadVersion(version):
    return True


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        思入: 二分找第一个数的水题
        """
        l, r = 1, n
        while l < r:
            mid = (l + r) // 2
            if not isBadVersion(mid):
                l = mid + 1
            else:
                r = mid
        return l
