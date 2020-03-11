# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # 思入: 计算子树的节点高度,max(左子+右子)
        rnt = 0

        def helper(node: TreeNode):
            nonlocal rnt
            if not node:
                return 0
            left = helper(node.left)
            right = helper(node.right)

            if left and right:
                rnt = max(rnt, left + right)
            elif not left and not right:
                return 1
            else:
                rnt = max(max(left, right), rnt)

            return max(left, right) + 1

        helper(root)
        return rnt
