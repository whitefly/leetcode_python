# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        思入1: 最终目的是为了找到删除点的前一个节点. 由于总长度不知道,所以不知道删除节点是正数第几个.所以先扫一遍来算出个数
        复杂度o(m+m-n)  m为总长度
        """
        first = head
        count = 0
        # 计算节点总个数,得到删除节点的位置
        while head:
            count += 1
            head = head.next

        if n == count:
            return first.next
        index = count - n + 1

        # 找到删除点的前一个位置,进行删除
        head = first
        for i in range(1, index):
            if i == index - 1:
                head.next = head.next.next
                break
            head = head.next
        return first


class Solution1:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        思入2: 最终目的是定位到删除点的前一个节点!
        使用双指针. 右指针先移动n步,然后左右指针开始同时移动.但右指针到底时,左指针恰好到目的节点.
        总结:其实思入1和思入2从走的步数来看,并没有明显区别.但是思入2的代码更加直观
        """
        l, r = head, head
        # 先移动n步
        for i in range(n):
            r = r.next
        # 处理n=size的情况
        if not r:
            return l.next
        # 同时移动,while退出后l恰好到目的节点
        while r.next:
            l = l.next
            r = r.next
        l.next = l.next.next
        return head
