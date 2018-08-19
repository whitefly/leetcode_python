class Solution:
    change = ((-1, 0), (1, 0), (0, 1), (0, -1))

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        思入: 设置相邻点change. 深度遍历和flag位.
        暴力for,找到第一个.开始上下左右匹配.出现不符合的就下一个. 只知道遍历完都没有返回True.则返回Flase
        """
        m, n = len(board), len(board[0])
        flag = [[False] * n for i in range(m)]

        def find(position, w):
            x, y = position
            for c_x, c_y in self.change:
                new_x = x + c_x
                new_y = y + c_y
                if new_x >= m or new_x < 0 or new_y >= n or new_y < 0 or flag[new_x][new_y]:
                    continue
                if board[new_x][new_y] == w[0]:
                    if len(w) == 1:
                        return True
                    flag[new_x][new_y] = True
                    result = find((new_x, new_y), w[1:])
                    flag[new_x][new_y] = False
                    if result:
                        return result
            return False

        for x, row in enumerate(board):
            for y, char in enumerate(row):
                if char == word[0]:
                    if len(word) == 1:
                        return True
                    flag[x][y] = True
                    if find((x, y), word[1:]):
                        return True
                    flag[x][y] = False
        return False


if __name__ == '__main__':
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    my_str = "A"
    s = Solution()
    print(s.exist(board, my_str))
