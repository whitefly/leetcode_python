# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        思入: 对其中一个链表进行hash存储.然后对另一个链表进行扫描是否有重复
        问题:set是否可以存储可变对象?
        """
        buf = set()
        while headA:
            buf.add(headA)
            headA = headA.next

        while headB:
            if headB in buf:
                return headB
            headB = headB.next
        return None

    def getIntersectionNode2(self, headA, headB):
        """
        :param headA:
        :param headB:
        :return:
        思入: 先各自扫一遍得到长度,然后将2个链表缩短至等长的,最后同时遍历
        """
        # 得到长度
        size_a, size_b = self.get_size(headA), self.get_size(headB)
        # 缩短链表
        if size_a >= size_b:
            for i in range(size_a - size_b):
                headA = headA.next
        else:
            headA, headB = headB, headA
            return self.getIntersectionNode2(headA, headB)
        # 同时遍历
        while headA:
            if headA is headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None

    def get_size(self, head):
        size = 0
        while head:
            size += 1
            head = head.next
        return size


if __name__ == '__main__':
    temp1 = ListNode(5)
    temp2 = ListNode(5)

    node = ListNode(3)
    # temp1.next = temp2.next = node
    s = Solution()
    print(s.getIntersectionNode(None, temp2))
