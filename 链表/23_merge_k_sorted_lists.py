# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        node = None
        start = None
        while not (l1 is None and l2 is None):
            if l1 is None:
                next = l2
                l2 = l2.next
            elif l2 is None:
                next = l1
                l1 = l1.next
            else:
                if l1.val < l2.val:
                    next = l1
                    l1 = l1.next
                else:
                    next = l2
                    l2 = l2.next
            if node is None:
                node = next
                start = node
            else:
                node.next = next
                node = node.next
        return start

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        思入: 从合并2个有序链表,使用reduce来合并k个. 但是131个例子,最后一个检测案例链表太长,导致无限超时. 故这个方法不可取
        """
        from functools import reduce
        return reduce(self.mergeTwoLists, lists)
