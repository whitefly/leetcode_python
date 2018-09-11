class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        思想:将链表转为 数组链表.然后进行快速定位
        """
        if not head:
            return head
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        # 重新排序
        size = len(nodes)
        for i in range(size // 2):
            temp = nodes[i]
            temp.next = nodes[size - 1 - i]
            nodes[size - 1 - i].next = nodes[i + 1]
            nodes[i + 1].next = None

    def show(self, head):
        nodes = []
        while head:
            nodes.append(head.val)
            head = head.next
        print(nodes)

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
    my_nodes = s.set_nodes([])
    s.reorderList(my_nodes)
    s.show(my_nodes)
