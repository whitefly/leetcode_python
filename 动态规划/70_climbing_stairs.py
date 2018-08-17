class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        思入: 入门dp题. 使用递归
        缺点: 超过30后需要时间增加.
        """
        if n == 1:
            return 1
        elif n == 2:
            return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)


class Solution1:
    def __init__(self):
        self.buff = [-1, 1, 2]
        self.last = 2

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        思入1: 入门dp题上的优化.和求前2数之和的递推式一样. 使用dp数组来存储
        """
        if n <= self.last:
            return self.buff[n]
        else:
            while self.last < n:
                self.buff.append(self.buff[-1] + self.buff[-2])
                self.last += 1
        return self.buff[n]


if __name__ == '__main__':
    s = Solution1()
    print(s.climbStairs(35))
