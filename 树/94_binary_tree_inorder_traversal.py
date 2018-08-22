# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        思入: 中序遍历的套路写法 通过闭包来遍历值.
        待处理:怎么使用非递归栈的写法
        """
        result = []

        def hepler(root):
            if not root:
                return None
            if root.left:
                hepler(root.left)
            result.append(root.val)
            if root.right:
                hepler(root.right)

        hepler(root)
        return result


class Solution1:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        思入:  栈的写法.  中序会一直到底,知道左子不存在. 然后出栈stack. 加入result. 然后右子做同样的事
        """
        result, stack = [], []
        p = root
        while stack or p:
            while p:
                # 有左子,不断压栈,直到左子不存在
                stack.append(p)
                p = p.left
            if stack:
                # 左子不存在了,开始出栈,存入结果
                p = stack.pop()
                result.append(p.val)
                # 对右子做同样的事
                p = p.right
        return result
