class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # 遍历num2记录
        stack = []
        my_hash = {}
        for i, num in enumerate(nums2):
            while stack and stack[-1] < num:
                my_hash[stack.pop()] = num
            stack.append(num)

        # 遍历num1
        return [my_hash.get(num, -1) for num in nums1]


if __name__ == '__main__':
    my_nums1 = [4, 1, 2]
    my_nums2 = [1, 3, 4, 2]
    s = Solution()
    result = s.nextGreaterElement(my_nums1, my_nums2)
    print(result)
