# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        思入1: 给每个节点附上特殊值. 若遍历到这个有特殊值,说明之前重复过
        """
        while head:
            if head.val == 99999999:
                return True
            else:
                head.val = 99999999
            head = head.next
        return False


class Solution2(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        思入2: 双指针,一个每次走一个(正常遍历),一个每次走2个.若重合,说明重复.若某个为None,或者没有next(抛错),说明有尽头
        """
        try:
            lower = head
            faster = head.next
            while lower:
                if faster == lower:
                    return True
                faster = faster.next.next
                lower = lower.next
            return False
        except:
            return False


if __name__ == '__main__':
    node = ListNode(0)
    node.next = node
    s = Solution()
    print(s.hasCycle(node))
