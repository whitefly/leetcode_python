# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # 不变的情况
        if k == 1 or not head:
            return head
        # 判断是否含有k个
        index = head  # type:ListNode
        for i in range(k):
            if not index:
                return head
            index = index.next
        # 反转
        last = None
        temp = head
        for i in range(k):
            next_node = temp.next

            temp.next = last
            last = temp
            temp = next_node
        # 拼接
        head.next = self.reverseKGroup(index, k)
        return last
