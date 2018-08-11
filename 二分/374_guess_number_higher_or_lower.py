def guess(num):
    target = 7
    if num == target:
        return 0
    return 1 if num > target else -1


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while r - l + 1 >= 1:
            mid = (l + r) // 2
            flag = guess(mid)
            if flag == 0:
                return mid
            elif flag == 1:
                r = mid - 1
            else:
                l = mid + 1


if __name__ == '__main__':
    s = Solution()
    print(s.guessNumber(10))
