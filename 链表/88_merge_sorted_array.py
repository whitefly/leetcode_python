class Solution:
    def merge(self, nums1: list, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        思入:2个数组,对应2个指针. 通过比较来确定那个指针进行移动.然后进行插入.最后处理某指针到底的情况
        """
        index1, index2 = 0, 0
        while index1 <= m - 1 and index2 <= n - 1:
            if nums1[index1] < nums2[index2]:
                index1 += 1
            else:
                nums1.insert(index1, nums2[index2])  # 插入一个,从最后减去一个,保持长度不变
                index2 += 1
                m += 1
                nums1.pop()
        if index1 == m:
            # 若num1到低,但是num2还没到底,直接将num2剩余部分拼接到num1上
            for i, v in enumerate(nums2[index2:]):
                nums1[index1 + i] = v


if __name__ == '__main__':
    my_num1 = [1, 2, 3, 0, 0, 0]
    my_num2 = [2, 5, 6]
    s = Solution()
    print(s.merge(my_num1, 3, my_num2, 3))
