# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        思入: 参考https://www.bbsmax.com/A/D854A2vdEg/
        分3个点,x(开始点),y(环的起始点),z(第一次相遇点). (正常速度和2倍的速断,即lower在1时,faster在2,若不满足,该公式不成立)第一次相遇时->2(a+b) = a+b+c+b ->a=c
        在相遇后,重新设置一个index从x开始走(正常速度),那么走了a步后,一定会在y处相遇

        """
        # 第一次相遇
        if not head or not head.next:
            return None
        lower = faster = head
        flag = True
        while faster != lower or flag:
            flag = False
            if not faster or not faster.next:
                return None
            faster = faster.next.next
            lower = lower.next

        # 此处说明有环,新增一个出发点
        while head != lower:
            head = head.next
            lower = lower.next
        return head

    def set_nodes(self, nodes, index=-1):
        temp, head, first, last = None, None, None, None

        for i, v in enumerate(nodes):
            temp = ListNode(v)
            if i == index and index != -1:
                first = temp
            if i == 0:
                head = last = temp
            else:
                last.next = temp
                last = temp
        last.next = first
        return head


if __name__ == '__main__':
    s = Solution()
    my_head = s.set_nodes([3, 2, 0, -4], index=1)
    print(s.detectCycle(my_head))
