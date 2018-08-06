# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        思入1: 左右互换时+考虑上一个的拼接.否则会断链. 所以需要一个变量来记录上一组节点.
        """
        if not head:
            return None
        new_head = last_i = ListNode(0)
        new_head.next = head
        while head and head.next:
            l, r = head, head.next
            # 左,右互换
            l.next = r.next
            r.next = l

            # 将右边拼接在上一个
            last_i.next = r

            # 指针更新到下一对,并记录临时末尾点
            head = l.next
            last_i = l
        return new_head.next
