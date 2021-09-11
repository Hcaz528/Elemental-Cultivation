class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class DNode:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None


class ZList:
    def __init__(self) -> None:
        self.head = None

    def generate(self) -> None:
        if self.head is None:
            return None
        node = self.head
        while node.next is not None:
            yield node.value
            node = node.next
        yield node.value
        return

    def show_list(self) -> list:
        if self.head is None:
            return None
        return [x for x in self.generate()]


class LinkedList(ZList):
    def __init__(self) -> None:
        super().__init__()
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return

        node = self.head
        while node.next is not None:
            node = node.next
        node.next = new_node

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node


class DoubleLinkedList(ZList):
    def __init__(self) -> None:
        super().__init__()
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = DNode(value)
        if self.head is None:
            self.head = self.tail = new_node
            self.head.next = self.tail
            self.tail.prev = self.head
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    def prepend(self, value):
        new_node = DNode(value)
        if self.head is None:
            self.head = self.tail = new_node
            self.head.next = self.tail
            self.tail.prev = self.head
            return
        self.head.prev = new_node
        new_node.next = self.head
        self.head = new_node


class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.node_amount = 0

    def size(self) -> int:
        return self.node_amount

    def enqueue(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = self.tail = new_node
        self.tail.next = self.tail = new_node

        self.node_amount += 1

    def dequeue(self):
        if self.head is None:
            return None
        deque_node_value = self.head.value
        self.head = self.head.next
        self.node_amount -= 1
        return deque_node_value

    def generator(self):
        if self.head is None:
            return None
        node = self.head
        while node.next is not None:
            yield node.value
            node = node.next
        yield node.value

    def show_queue(self):
        if self.head is None:
            return None
        return [x for x in self.generator()]


class Stack(ZList):
    def __init__(self) -> None:
        super().__init__()
        self.head = None
        self.num_nodes = 0

    def push(self, value):
        new_node = Node(value)
        if self.head is not None:
            new_node.next = self.head
        self.head = new_node
        self.num_nodes += 1

    def pop(self):
        if self.head is None:
            return None
        popped_node_value = self.head.value
        self.head = self.head.next
        self.num_nodes -= 1
        return popped_node_value


""" Driver Code 1"""
# llist = LinkedList()
# llist.prepend(4)
# llist.append(1)
# llist.append(2)
# llist.append(3)
# llist.prepend(5)
# print(llist.head.value)
# print(llist.head.next.value)
# print(llist.show_list())

""" Driver Code 2"""
# dlist = DoubleLinkedList()
# dlist.append(1)
# dlist.append(2)
# dlist.prepend(4)
# dlist.append(3)
# print(dlist.head.value)
# print(dlist.head.next.value)
# print(dlist.tail.prev.value)
# print(dlist.tail.value)
# print(dlist.show_list())

""" Driver Code 3"""
# q = Queue()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.enqueue(4)
# print(q.dequeue(), q.dequeue())
# print(q.show_queue())

""" Driver Code 4"""
# s = Stack()
# s.push(0)
# s.push(1)
# s.push(2)
# s.push(3)
# s.push(4)
# s.push(5)
# s.push(6)
# s.push(7)
# s.push(8)
# print(s.pop(), s.pop(), s.pop(), s.pop())
# print(s.show_list())
