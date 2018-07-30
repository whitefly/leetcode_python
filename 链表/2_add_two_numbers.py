class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) :
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        思入: 默认l1为长链,若l2比较长,则将l2多出的链转移到l1上去. 然后大数加法的通用代码来完成. 空间复杂度O(1)
        """
        carry = 0
        l1_node, l2_node = l1, l2
        while True:
            l = l1_node.val if l1_node else 0
            r = l2_node.val if l2_node else 0
            my_sum = l + r + carry
            carry = my_sum // 10
            l1_node.val = my_sum % 10
            # 拼接多余的链
            if not l1_node.next and l2_node:
                l1_node.next = l2_node.next
                l2_node.next = None
            if not l1_node.next:
                if carry:
                    l1_node.next = ListNode(carry)
                break
            l1_node, l2_node = l1_node.next, l2_node.next if l2_node else None
        return l1


class Solution1:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        思如: 暴力法,创建第3个链,作为结果链表. 不断添加新节点 空间复杂度O(m+n)
        """
        l1_node, l2_node = l1, l2
        result = ListNode(0)
        my_result = result
        carry = 0
        while l1_node or l2_node:
            l = l1_node.val if l1_node else 0
            r = l2_node.val if l2_node else 0

            my_sum = l + r + carry
            carry = my_sum // 10
            my_result.next = ListNode(my_sum % 10)
            my_result = my_result.next

            l1_node, l2_node = l1_node.next if l1_node else None, l2_node.next if l2_node else None

        if carry != 0:
            my_result.next = ListNode(carry)
        return result.next


if __name__ == '__main__':
    s = Solution()
    my_l1 = ListNode(9)
    my_l1.next = ListNode(1)
    my_l1.next.next = ListNode(6)
    my_l2 = ListNode(0)

    print(s.addTwoNumbers(my_l1, my_l2))
