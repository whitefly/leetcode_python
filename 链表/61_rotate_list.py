# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        思入: 当做一个循环链表.右移动相当逆时针转.需要追溯到上一个.不方便.
        考虑为顺时针转,需要找到下一个.方便操作.  逆时针转k 相当于 顺时针转size-k
        """
        if not head:
            return head
        # 构造单循环列表,计算size
        temp = head
        count = 1
        while temp.next:
            count += 1
            temp = temp.next
        temp.next = head

        k = count - k % count
        # 顺时针转k,相当于左移动 index
        for i in range(k):
            head = head.next
        result = head.next
        head.next = None
        return result


if __name__ == '__main__':
    s = Solution()
    my_head = ListNode(1)
    my_head.next = ListNode(2)
    s.rotateRight(my_head, 0)
