# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        思入: 使用指针扫2个链表. 创建第三条链,每比较一次,创建一个新节点拼接
        思考:可不可以不使用额外空间,而完成这题?
        """
        result = ListNode(0)
        index3 = result
        while l1 and l2:
            if l1.val < l2.val:
                index3.next = ListNode(l1.val)
                l1 = l1.next
            else:
                index3.next = ListNode(l2.val)
                l2 = l2.next
            index3 = index3.next
        if l1:
            index3.next = l1
        elif l2:
            index3.next = l2
        return result.next


if __name__ == '__main__':
    my_l1 = ListNode()
