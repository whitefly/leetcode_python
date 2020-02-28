# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Soltion:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        # 扫2遍,层次遍历得到最
        deepest = 0
        if root:
            Q = deque()
            Q.append(root)
            while Q:
                level = 0
                deepest += 1
                size = len(Q)
                for _ in range(size):
                    node = Q.popleft()  # type:TreeNode
                    level += 1
                    if node.left:
                        Q.append(node.left)
                    if node.right:
                        Q.append(node.right)

        target = root
        flag = False

        def helper(temp: TreeNode, deep):
            nonlocal target
            nonlocal flag
            if flag:
                return 0
            if not temp:
                return 0

            left = helper(temp.left, deep + 1)
            right = helper(temp.right, deep + 1)
            count = left + right
            if deep == deepest:
                count += 1

            if count == level and not flag:
                target = temp
                flag = True
            return count

        helper(root, 1)

        return target


if __name__ == '__main__':
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.left.left = TreeNode(3)
    s = Soltion()
    rnt = s.subtreeWithAllDeepest(None)
    print(rnt)
