from typing import List


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        # 搜索车的位置
        rook_i, rook_j = 0, 0
        limit_i = len(board)
        limit_j = len(board)
        for i in range(limit_i):
            for j in range(limit_j):
                if board[i][j] == 'R':
                    rook_i, rook_j = i, j
                    break

        # 上下左右搜索
        count = 0
        mapping = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for direction in range(4):
            temp_i, temp_j = rook_i, rook_j
            for offset in range(8):
                temp_i += mapping[direction][0]
                temp_j += mapping[direction][1]
                if temp_i >= limit_i or temp_i < 0 or temp_j < 0 or temp_j >= limit_j or board[temp_i][temp_j] == 'B':
                    break
                if board[temp_i][temp_j] == 'p':
                    count += 1
                    break

        return count


if __name__ == '__main__':
    M = [[".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", "p", ".", ".", ".", "."],
         [".", ".", ".", "p", ".", ".", ".", "."],
         ["p", "p", ".", "R", ".", "p", "B", "."],
         [".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", "B", ".", ".", ".", "."],
         [".", ".", ".", "p", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", "."]]

    solver = Solution()
    rnt = solver.numRookCaptures(M)
    print(rnt)
