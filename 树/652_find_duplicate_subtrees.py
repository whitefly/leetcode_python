# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    null_tag = "X"

    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        # 每个节点记录位置,确定序列化后的字符串范围
        container = {}

        def helper(index: TreeNode):
            if not index:
                return Solution.null_tag

            left = helper(index.left)
            right = helper(index.right)

            fingerprint = str(index.val) + " " + left + " " + right

            if fingerprint in container:
                container[fingerprint].append(index)
            else:
                container[fingerprint] = [index]

            return fingerprint

        helper(root)
        return [v[0] for k, v in container.items() if len(v) > 1]


if __name__ == '__main__':
    solver = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)

    root.right = TreeNode(2)
    root.right.left = TreeNode(4)
    # root = TreeNode(1)
    # root.left = TreeNode(2)
    # root.left.left = TreeNode(3)
    # root.left.right = TreeNode(4)

    rnt = solver.findDuplicateSubtrees(root)
    print(rnt)
