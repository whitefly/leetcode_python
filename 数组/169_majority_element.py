class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        思入: 最小抽屉原理+摩尔投票法.
        由于题目明确说明 次数>(n/2)的数一定存在,
        每次消除一对不同的,最后剩下的,一定就是超过一半的那个数
        """
        major, count = None, 0
        for i in nums:
            if major == i:
                count += 1
            elif count == 0:
                major, count = i, 1
            else:
                count -= 1
        return major


if __name__ == '__main__':
    my_nums = [2, 2, 1, 1, 1, 2, 2]
    s = Solution()
    print(s.majorityElement(my_nums))
