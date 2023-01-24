"""
간단하게 Linked List의 operations 를 구현 하면서 자료 구조를 학습
"""
class Node :
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next
class LinkedList(object):
    def __init__(self):
        self.head = None
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while(current.next):
                current = current.next
            current.next = new_node
    def insert(self, idx, value):
        prev = self.head
        new_node = Node(value)

        if idx == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            for _ in range(idx - 1):
                prev = prev.next
            new_node.next = prev.next
            prev.next = new_node
    def get(self, idx):
        current = self.head
        for _ in range(idx):
            current = current.next
        return current.value



linkedList = LinkedList()

linkedList.append(1)
linkedList.append(2)
linkedList.append(3)
linkedList.append(4)
linkedList.insert(0,11)
print(linkedList.get(0))
print(linkedList.get(1))
print(linkedList.get(2))
print(linkedList.get(3))

