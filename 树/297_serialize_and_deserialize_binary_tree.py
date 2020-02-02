# Definition for a binary tree node.
from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    null_tag = "null"
    split_tag = " "

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        思入:  1
             /
            2
        前序遍历改为:  1, 2 , null, null ,null
        即每个空位置填充一个null
        """
        if not root:
            return Codec.null_tag + Codec.split_tag
        rnt = str(root.val) + Codec.split_tag
        rnt += self.serialize(root.left)
        rnt += self.serialize(root.right)
        return rnt

    def deserialize(self, data):
        codes = data.strip().split(Codec.split_tag)
        q = deque()
        for c in codes:
            q.appendleft(c)

        def helper():
            val = q.pop()
            if val == Codec.null_tag:
                return None
            temp = TreeNode(int(val))
            temp.left = helper()
            temp.right = helper()
            return temp

        return helper()


if __name__ == '__main__':
    codec = Codec()
    root = TreeNode(1)
    root.left = TreeNode(2)

    demo = codec.serialize(root)
    rnt = codec.deserialize(demo)
    print(rnt)
