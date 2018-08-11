class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        思入:暴力法. 先行验证,再列验证,在3*3验证
        """
        centers = ((1, 1), (1, 4), (1, 7),
                   (4, 1), (4, 4), (4, 7),
                   (7, 1), (7, 4), (7, 7))
        changes = ((0, 0), (0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, 1), (-1, 1), (1, -1))
        # 行验证
        buff = set()
        for sublist in board:
            buff.clear()
            for i in sublist:
                if i in buff:
                    return False
                else:
                    if i != '.':
                        buff.add(i)
        # 列验证
        for index in range(9):
            buff.clear()
            for sublist in board:
                num = sublist[index]
                if num in buff:
                    return False
                else:
                    if num != '.':
                        buff.add(num)
        # 3*3验证
        for x, y in centers:
            buff.clear()
            for c_x, c_y in changes:
                num = board[x + c_x][y + c_y]
                if num in buff:
                    return False
                else:
                    if num != '.':
                        buff.add(num)
        return True


if __name__ == '__main__':
    hehe = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
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
    print(s.isValidSudoku(hehe))
