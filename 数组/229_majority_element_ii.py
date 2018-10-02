class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        思入: 用map来存储count.
        复杂度: 时间复杂度O(n),空间复杂度O(n)
        """
        count = {}
        for i in nums:
            count[i] = count[i] + 1 if (i in count) else 1

        limit = len(nums) // 3
        return [k for k, v in count.items() if v > limit]

    def majorityElement2(self, nums):
        '''
        :param nums:
        :return:
        思入:用摩尔投票法来找出最大的两个.因为大于n/3,至多可能只有2种或1种.
        每次减少一对
        '''
        if not nums:
            return nums
        num1, num2, count1, count2 = 0, 0, 0, 0
        for i in nums:
            # 计数
            if i == num1:
                count1 += 1
            elif i == num2:
                count2 += 1
            # 若将2个调换位置,就通不过
            elif count1 == 0:
                num1 = i
                count1 = 1
            elif count2 == 0:
                num2 = i
                count2 = 1
            else:
                # 为什么要同时减去
                count1 -= 1
                count2 -= 1

        # 验证是否大于n/3
        limit = len(nums) // 3
        check1, check2 = 0, 0
        for i in nums:
            if i == num1:
                check1 += 1
            if i == num2:
                check2 += 1

        # 最后验证
        result = []
        if check1 > limit:
            result.append(num1)
        if check2 > limit and num1 != num2:
            result.append(num2)

        return result


if __name__ == '__main__':
    s = Solution()
my_nums = [1, 2, 2, 3, 2, 1, 1, 3]
print(s.majorityElement2(my_nums))
