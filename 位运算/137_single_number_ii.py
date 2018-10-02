class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        思入: 之前是出现2个还原.可以出位进行异或计算来完成
        现在需要出现3次再还原.需要需要2bit来表示对应的状态. 然后画出真值表,得出A,B的逻辑表达式
        """
        A, B = 0, 0
        for C in nums:
            tempA = ((~A) & B & C) | (A & (~B) & (~C))
            B = (~A & ~B & C) | (~A & B & ~C)
            A = tempA
        return B


if __name__ == '__main__':
    s = Solution()
    my_nums = [0, 1, 0, 1, 0, 1, 99]
    print(s.singleNumber(my_nums))
