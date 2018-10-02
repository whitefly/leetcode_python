class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        思入: 单个数组i的升级版,需要找个2个数.然后2个数分别在2个分组,然后对不同分组进行异或可以得到结果
        核心:怎么将2个数分出来?  整体异或的结果就是得到A^B. 找到A^B中从右数数第一个不为0的位.就是A和B的第一个差异位.
        然后根据这个差异位,对数进行分组
        """
        C = 0
        for num in nums:
            C ^= num

        # 得到差异位的下标
        index = self.get_index(C)

        A, B = 0, 0
        for num in nums:
            if self.isTrueOfIndex(index, num):
                A ^= num
            else:
                B ^= num
        return A, B

    def isTrueOfIndex(self, index, num):
        temp = num >> index & 1
        return temp == 1

    def get_index(self, num):
        index = 0
        while num:
            temp = num & 1
            if temp == 1:
                return index
            else:
                index += 1
                num >>= 1
        return index


if __name__ == '__main__':
    s = Solution()
    my_num = [1, 2, 1, 3, 2, 5]
    print(s.singleNumber(my_num))
