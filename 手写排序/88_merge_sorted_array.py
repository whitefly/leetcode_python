class Solution:
    def merge(self, nums1: list, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        思入:2个数组,对应2个指针. 通过比较来确定那个指针进行移动.然后进行插入.最后处理某指针到底的情况
        复杂度:  时间最坏O(N^2) 空间O(n)
        待优化: 能不被不进行插入. 即优化到O(m+n)
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


class Solution1:
    def merge(self, nums1: list, m, nums2, n):
        """
        难点:要扫一遍就排到正确的位置,肯定是一个index的坑.但是如果从左向右填坑的,会影响num1中index后的元素.
        但此时num1最后的位置恰好没有使用,所以用index从右向左填坑. 设置up,down2个指针作为上下的扫描指针
        复杂度: 时间O(m+n) 空间O(1)
        """
        up, down = m - 1, n - 1
        index = m + n - 1
        while up >= 0 or down >= 0:
            # 处理某一个条链已经遍历完的情况
            if down >= 0 and (nums1[up] <= nums2[down] or up < 0):
                nums1[index] = nums2[down]
                down -= 1
            else:
                nums1[index] = nums1[up]
                up -= 1
            index -= 1
        return nums1


if __name__ == '__main__':
    my_num1 = [1]
    my_num2 = []
    s = Solution1()
    print(s.merge(my_num1, 1, my_num2, 0))
