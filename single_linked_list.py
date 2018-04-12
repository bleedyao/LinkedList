class Node(object):
    def __init__(self, element):
        self.element = element
        self.next = None


class SingleLinkedList(object):
    """单项列表"""

    def __init__(self):
        self.__head = None

    def is_empty(self):
        """是否为空"""
        return self.__head is None

    def length(self):
        """列表长度"""
        cur = self.__head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def append(self, item):
        """从前面添加"""
        node = Node(item)
        if self.__head is None:
            self.__head = node
        else:
            node.next = self.__head
            self.__head = node

    def add(self, item):
        """从后面插入"""
        node = Node(item)
        cur = self.__head
        while cur.next is not None:
            cur = cur.next
        cur.next = node

    def travel(self):
        """遍历"""
        cur = self.__head
        while cur is not None:
            print(cur.element, end=" ")
            cur = cur.next
        print("")

    def insert(self, pos, item):
        """插入"""
        node = Node(item)
        if pos <= 0:
            self.append(item)
        elif pos > self.length():
            self.add(item)
        else:
            cur = self.__head
            count = 0
            while count < pos - 1:
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self, item):
        """移除"""
        cur = self.__head
        pre = None
        while cur is not None:
            if cur.element == item:
                if pre is not None:
                    pre.next = cur.next
                    return "remove %s" % item
            else:
                pre = cur
                cur = cur.next
        return None

    def search(self, item):
        """查询元素"""
        cur = self.__head
        count = 0
        while cur is not None:
            if cur.element == item:
                return count
            else:
                cur = cur.next
                count += 1
        return None

if __name__ == "__main__":
    li = SingleLinkedList()
    print("method is_empty: %s" % li.is_empty())
    print("method length: %s" % li.length())

    li.append(1)
    li.append(2)
    li.append(3)

    print("method length: %s" % li.length())
    li.travel()  # 3 2 1

    li.add(4)
    li.add(5)
    li.add(6)
    li.travel()  # 3 2 1 4 5 6

    li.insert(3, 7)
    li.insert(-1, 8)
    li.insert(20, 9)
    li.insert(6, 10)
    li.travel()  # 8 3 2 1 7 4 10 5 6 9

    print(li.remove(20))
    print(li.remove(6))
    print(li.remove(9))
    print(li.remove(2))
    li.travel()  # 8 3 1 7 4 10 5

    print(li.search(3))
    print(li.search(2))
    print(li.search(5))
