# Definition for a binary tree node.
from collections import deque
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if root:
            Q = deque()
            Q.append(root)
            while Q:
                size = len(Q)
                level = []
                for _ in range(size):
                    node = Q.popleft()  # type:TreeNode
                    level.append(node.val)
                    if node.left:
                        Q.append(node.left)
                    if node.right:
                        Q.append(node.right)
                result.append(level)
        return result


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    s = Solution()
    rnt = s.levelOrder(root)
    print(rnt)
