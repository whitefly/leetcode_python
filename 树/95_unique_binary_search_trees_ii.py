# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        思入: 用类似递归的思想,由于是二叉搜索数. 1~~~n的数组中, 如果root为i,那么  1~i-1在左子,i+1:~在右子. 返回一个左子组合和右子组合,然后递归
        """
        return self.helper(1, n) if n else []

    def helper(self, l, r):
        if l > r:
            return [None]
        temp = []
        for i in range(l, r + 1):
            for left in self.helper(l, i - 1):
                for right in self.helper(i + 1, r):
                    p = TreeNode(i)
                    p.left, p.right = left, right
                    temp.append(p)
        return temp


if __name__ == '__main__':
    pass
