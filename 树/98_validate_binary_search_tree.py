class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        思入: 给一个root(可能为空) 验证左子是否小于自身 验证右子大于自身.  核心:
        要防止出现这样的情况
                10
            5        20
          1  11    19   21
                  9
        """
        return self.helper(root, 0, 0)

    def helper(self, root, limit_l, limit_r, status):  # limit_l表示爷爷节点最小的  limit_r表示爷爷节点最大的
        if not root:
            return True
        l, r = True, True
        if root.left:
            l = root.left.val < root.val
            if status == 1:
                l &= (limit_l < root.left.val < limit_r)
        if root.right:
            r = root.val < root.right.val
            if status == -1:
                r &= (limit_l < root.left.val < limit_r)
        if not (l and r):
            return False
        limit_l
        sub_l = self.helper(root.left, root.val, -1)
        sub_r = self.helper(root.right, root.val, 1)
        return sub_l and sub_r
