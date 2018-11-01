import numpy as np
from itertools import permutations
from queue import Queue


class Stutus:
    def __init__(self, a, b1, b2, t):
        self.field = (a, b1, b2)
        self.t = t

    def is_gone(self, my_np):
        return my_np[self.field[0]][self.field[1]][self.field[2]] != 0

    def set_done(self, my_np):
        my_np[self.field[0]][self.field[1]][self.field[2]] = 1

    def is_target(self, my_target):
        return all([self.field[i] == v for i, v in enumerate(my_target)])

    def show(self):
        print("状态:{}-{}-{}".format(*self.field))


class Solution:

    def convert(self, begin: int, end: int, last: Stutus, limit):
        #  begin和end为容器的下标,由C1容器转移到C2,返回转移后的元组状态,
        temp = [0] * 3
        index3 = 3 - begin - end
        c1, c2 = last.field[begin], last.field[end]
        index1_num, index2_num = (0, c1 + c2) if c1 + c2 <= limit[end] else (c1 + c2 - limit[end], limit[end])
        temp[begin], temp[end], temp[index3] = index1_num, index2_num, last.field[index3]
        return temp

    def fenyou(self, bottle, cup1, cup2, endTuple):
        """
        题目:大家一定觉的运动以后喝可乐是一件很惬意的事情，但是seeyou却不这么认为。
        因为每次当seeyou买了可乐以后，阿牛就要求和seeyou一起分享这一瓶可乐，而且一定要喝的和seeyou一样多。但seeyou的手中只有两个杯子，它们的容量分别是N
        毫升和M 毫升 可乐的体积为S （S<101）毫升　(正好装满一瓶) ，它们三个之间可以相互倒可乐 (都是没有刻度的，且
        S==N+M，101＞S＞0，N＞0，M＞0) 。聪明的ACMER你们说他们能平分吗？如果能请输出倒可乐的最少的次数，如果不能输出”NO”。

        思入: 状态的搜索,由于需要最小的次数,所以使用广度搜索.
        状态:3个容器的含水量.  状态转移: A->B1,A->B2;B1->A,B1->B2;B2->A,B2->B1 6种转移方式(可以使用2个for 或者 迭代库来实现)
        每次转移量: 容器1->容器2,要不容器1空,要不容器2满
        """

        self.limit = (bottle, cup1, cup2)  # 最大容量
        self.done = np.empty((101, 101, 101), dtype="int32")  # 状态是否遍历过
        self.endTuple = endTuple
        self.t = 0
        # 广度搜索
        q = Queue()
        first = Stutus(bottle, 0, 0, 0)
        q.put(first)
        first.set_done(self.done)
        return self.BFS(buf=q)

    def BFS(self, buf):
        while not buf.empty():
            now = buf.get()  # type:Stutus
            # 转移的6种状态
            for index1, index2 in permutations((0, 1, 2), 2):
                if now.field[index1] == 0:
                    continue
                temp = self.convert(index1, index2, now, self.limit)
                temp_S = Stutus(*temp, now.t + 1)
                if not temp_S.is_gone(self.done):
                    temp_S.set_done(self.done)
                    # 显示父状态,方便广度遍历的回溯寻找答案
                    now.show()
                    temp_S.show()
                    print()

                    if temp_S.is_target(self.endTuple):
                        return temp_S.t
                    buf.put(temp_S)
        return -1


if __name__ == '__main__':
    S = Solution()
    # 从状态(10,0,0) 转移到 (5,5,0)
    result = S.fenyou(10, 7, 3, (5, 5, 0))
    print(result)
