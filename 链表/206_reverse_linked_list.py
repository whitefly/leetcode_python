# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        思入: 正常扫一遍,然后将箭头转向(需要设置一个last来保存上一个节点).继续下一个.直到最后一个
        """
        if not head:
            return None
        last = None
        while head.next:
            # 先将下个要遍历的元素设置好
            temp = head
            head = head.next
            # 反转
            temp.next = last
            last = temp

        head.next = last
        return head
