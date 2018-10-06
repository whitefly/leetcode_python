class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        思入:二分搜索变种, 循环不变式:切片在0~len()中扫,若h=len-cut: 若满足num[cut-1]<=h<=num[cut],则cut一定在[0:mid]
        """
        l, r, size = 0, len(citations), len(citations)
        while l < r:
            mid = (l + r) // 2
            h = size - mid
            if citations[mid - 1] <= h <= citations[mid]:  # mid为什么不会越界? 因为退出时,[l,r]总是有2个,mid会取小的数,所以到不了边界
                r = mid
            elif h > citations[mid]:
                # 右移
                l = mid + 1
            else:
                r = mid - 1

        # 剩下2个
        return size - l


if __name__ == '__main__':
    my_nums = [1, 1]
    s = Solution()
    print(s.hIndex(my_nums))
