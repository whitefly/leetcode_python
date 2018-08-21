# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        思入: 设置index的坑,后面可能会有重复的.需要保留上一个节点
        """
        begin = ListNode(999999)
        begin.next = head
        last = begin
        count = 0
        while head:
            if head.val == last.next.val:
                if count == 0:
                    last.next = head
                count += 1
            else:
                if count == 1:
                    last = last.next
                    last.next = head
                else:
                    last.next = head
                    count = 1

            head = head.next
        if count != 1:
            last.next = None
        return begin.next
