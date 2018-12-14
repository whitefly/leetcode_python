"""
思想:
1.get(key),由于需要在O(1)的时间范围内根据key得到value,所以必须使用hashmap. 而get后,需要调整这个key到最新的位置.所以也需要使用链表
2.put(key, value),由于在容量满的情况下,需要在O(1)时间内找到要删除的元素,所以必须这个最少使用的元素必须在每次get后,转移到特定的删除位置.
综合: 双向链表(不用循环)+map(字典)来完成
"""


class Node:
    def __init__(self, key, v, front):
        # 头结点没有front
        self.front = front  # type:Node
        self.next = None  # type:Node
        self.v = v
        self.key = key


class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.map = {}  # value为双向链表的节点元素
        self.haven = 0
        self.old_index = None  # type:Node  #特定删除位置的节点(最有可能删除)
        self.new_index = None  # type:Node #最新使用结果

    def get(self, key):
        """
        思入: 在字典中找到该元素,并调整双线链表中的次序
        :type key: int
        :rtype: int
        """
        if key not in self.map:
            return -1

        # 改变链表次序 裂开+插入到首位(new_index)
        now_node = self.map[key]  # type: Node
        if now_node is self.new_index:
            return now_node.v
        # 裂开
        front = now_node.front
        next1 = now_node.next
        front.next = next1
        next1.front = front
        # 插入
        if self.new_index:
            last_new = self.new_index
            last_new.next = now_node
            now_node.front = last_new
        self.new_index = now_node
        return now_node.v

    def put(self, key, value):
        """
        在字典中插入新的元素,并双线链表中的次序,可能删除最少使用的节点
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.haven == 0:
            now_node = Node(value, None, key)
            self.map[key] = now_node
            self.new_index = now_node
            self.old_index = now_node
            self.haven += 1
            return

        # 先添加
        last_new = self.new_index
        now_node = Node(value, last_new, key)
        self.map[key] = now_node
        self.new_index = now_node

        # 超载的情况下,删除(map和链表中同时删)
        if self.haven == self.capacity:
            last_new = self.old_index
            self.old_index = last_new.next
            self.map.pop(last_new.key)
            del last_new
        else:
            self.haven += 1


cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
cache.get(1)
cache.put(3, 3)
cache.get(2)
cache.put(4, 4)
cache.get(1)
cache.get(3)
cache.get(4)
