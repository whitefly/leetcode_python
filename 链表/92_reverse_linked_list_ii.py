class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        思入: 和反转链表差不多, 在反转链表的基础上要进行收尾连接.
        先到需要反转的首节点上,反转完成后,进行首位拼接. l为反转节点第一个的上一个. 由于
        """
        first = ListNode(0)
        first.next = head
        head = first
        for i in range(0, m - 1):
            head = head.next

        l = head
        node1 = head = l.next

        count = 0
        end = n - m
        if not end:
            return first.next
        last = None
        # 开始反转
        while count <= end:
            temp = head
            head = head.next

            temp.next = last
            last = temp
            count += 1

        # 拼接首位(反转最后一个节点)和head(反转最后节点的下一个)
        node1.next = head
        l.next = last

        return first.next


if __name__ == '__main__':
    s = Solution()
    demo = ListNode(5)
    m = 1
    n = 1
    result = s.reverseBetween(demo, m, n)
    print(1)
