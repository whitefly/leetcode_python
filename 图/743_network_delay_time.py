class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        思入:一个点到其他点的最短距离.
        典型的单源最短路Dijkstra.
        要点: 一次一次选择距离原地第1近的点,第2近的点..第n近的点. 但是第2近的路径不一定会经过第1近的点
        """
        limit = 99999999
        # 构造邻接矩阵
        matrix = [[-1] * N for i in range(N)]
        for u, v, w in times:
            matrix[u - 1][v - 1] = w
        # Dijkstra算法
        last_p = (K - 1)
        done = [False] * N
        done[last_p] = True
        # compare_buf[i]表示现阶段原点到i点的最小距离
        compare_buf = [limit] * N
        result_buf = [limit] * N
        front_node = [-1] * N
        result_buf[K - 1] = 0
        # 找离K最近的点
        while True:
            # 对last的邻接进行遍历,更新compare_buf
            for i, v in enumerate(matrix[last_p]):
                if done[i] or v == -1:
                    continue
                value = v + result_buf[last_p]
                if value < compare_buf[i]:
                    compare_buf[i] = value
                    front_node[i] = last_p

            # 对compare_buf区遍历,找到最小的
            temp_min = limit
            temp_node = -1
            for i, value in enumerate(compare_buf):
                if done[i] or value == limit:
                    continue
                if value < temp_min:
                    temp_min = value
                    temp_node = i
            if temp_node == -1:
                break  # 选不出最小值,就退出
            else:
                done[temp_node] = True
                last_p = temp_node
                result_buf[temp_node] = temp_min
        return max(result_buf) if all(done) else -1


if __name__ == '__main__':
    # my_times, n, k = [[3, 5, 78], [2, 1, 1], [1, 3, 0], [4, 3, 59], [5, 3, 85], [5, 2, 22], [2, 4, 23], [1, 4, 43],
    #                   [4, 5, 75], [5, 1, 15], [1, 5, 91], [4, 1, 16], [3, 2, 98], [3, 4, 22], [5, 4, 31], [1, 2, 0],
    #                   [2, 5, 4], [4, 2, 51], [3, 1, 36], [2, 3, 59]], 5, 5
    my_times, n, k = [[1, 2, 1]], 2, 2
    s = Solution()
    r = s.networkDelayTime(my_times, n, k)
    print(r)
