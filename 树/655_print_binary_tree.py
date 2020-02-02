from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        # 思入: 树递归,遍历一遍,得到高度,然后再遍历一遍,得到root节点的所在位置,和应该有的范围,对中间赋值即可
        # 获取高度
        height = self.get_height(root)
        col_count = 2 ** height - 1
        rnt = [[""] * col_count for _ in range(height)]

        def helper(index, l, r, row):
            if not index:
                return
            mid = (l + r) // 2
            rnt[row][mid] = str(index.val)
            helper(index.left, l, mid - 1, row + 1)
            helper(index.right, mid + 1, r, row + 1)

        helper(root, 0, col_count - 1, 0)
        return rnt

    def get_height(self, root):
        if not root:
            return 0

        left = self.get_height(root.left)
        right = self.get_height(root.right)
        return max(left, right) + 1


if __name__ == '__main__':
    s = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    print(s.printTree(root))
