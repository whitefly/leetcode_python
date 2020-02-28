# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # 子树相同,再考虑本节点
        if not p and not q:
            return True
        if p and q and q.val == p.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False
