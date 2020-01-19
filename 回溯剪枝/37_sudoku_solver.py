from pprint import pprint
from typing import List


class Solution:
    def __init__(self):
        self.columns = [[-1] * 9 for _ in range(9)]
        self.block = [[-1] * 9 for _ in range(9)]
        self.rows = [[-1] * 9 for _ in range(9)]

        self.board = None
        self.end = False

    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        count = 0
        self.board = board
        for i, row in enumerate(board):
            for j, v in enumerate(row):
                if v == ".":
                    self.update(count)
                else:
                    self.update(count, v=int(v))
                count += 1
        # 初始化
        self.helper(0)
        # 写入答案
        for i, row in enumerate(board):
            for j, v in enumerate(row):
                board[i][j] = str(self.rows[i][j])

    def check(self, position, v):
        # 检查块,行,列
        return self._check_block(position, v) and self._check_row(position, v) and self._check_column(position, v)

    def get_row_id_by_position(self, position):
        return position // 9, position % 9

    def get_column_id_by_position(self, position):
        return position % 9, position // 9

    def get_block_id_by_position(self, position):
        x = position // 9
        y = position % 9
        return x // 3 * 3 + y // 3, x % 3 * 3 + y % 3

    def _check_row(self, position, v):
        return not any([i == v for i in self.rows[self.get_row_id_by_position(position)[0]]])

    def _check_column(self, position, v):
        return not any([i == v for i in self.columns[self.get_column_id_by_position(position)[0]]])

    def _check_block(self, position, v):
        return not any([i == v for i in self.block[self.get_block_id_by_position(position)[0]]])

    def helper(self, position):
        if position == 81:
            self.end = True  # 找到正确答案
            return

        # 在position位置试一试1-9
        x = position // 9
        y = position % 9
        if self.rows[x][y] == -1:
            for v in range(1, 10):
                if self.check(position, v):
                    self.update(position, v=v)
                    self.helper(position + 1)
                    if not self.end:
                        self.update(position)
        else:
            self.helper(position + 1)

    def update(self, position, v=-1):
        row_x, row_y = self.get_row_id_by_position(position)
        self.rows[row_x][row_y] = v

        column_x, column_y = self.get_column_id_by_position(position)
        self.columns[column_x][column_y] = v

        block_x, block_y = self.get_block_id_by_position(position)
        self.block[block_x][block_y] = v


if __name__ == '__main__':
    nums = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]
    s = Solution()
    s.solveSudoku(nums)
    pprint(nums)
