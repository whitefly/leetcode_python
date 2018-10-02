# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        思入: 每次遍历到一个新元素node,从head~node之间找到对应的位置(从前往后找)
        难点: 连来连去的看得我的头疼
        """
        index = last = head
        while index.next:
            begin = head
            while begin != index:
                # 插入
                if begin.val < index.val < begin.next.val:
                    temp = index.next
                    index.next = begin.next
                    begin.next = index

                    index = temp
                    break
