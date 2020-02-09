from typing import List


class Solution:

    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        # 思入: 暴力扫所有的组合,判断中点是否存在. 若存在,就出现了一对,结果+2
        count = 0
        for p1 in points:
            frequency_map = {}
            for p2 in points:
                distance = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
                if distance in frequency_map:
                    frequency_map[distance] += 1
                else:
                    frequency_map[distance] = 1

            for k, v in frequency_map.items():
                if v > 1:
                    count += v * (v - 1)
        return count


if __name__ == '__main__':
    points = [[0, 0], [1, 0], [-1, 0], [0, 1], [0, -1]]
    solver = Solution()
    rnt = solver.numberOfBoomerangs(points)
    print(rnt)
    k = 1
