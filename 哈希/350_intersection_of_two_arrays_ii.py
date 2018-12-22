class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        思入: dict的范围不会操作num1的范围,每次相同的num出现一个,就在结果res中加一次.若加到恰好抵消,就从map中删除该key
        """
        num_map = dict()
        res = []
        for i in nums1:
            num_map[i] = (num_map[i] + 1 if i in num_map else 1)
        # 模拟从磁盘中一个一个读取数据
        for i in nums2:
            if i in num_map:
                num_map[i] -= 1
                res.append(i)
                if num_map[i] == 0:
                    num_map.pop(i)

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.intersect([4, 9, 5], [9, 4, 9, 8, 4]))
