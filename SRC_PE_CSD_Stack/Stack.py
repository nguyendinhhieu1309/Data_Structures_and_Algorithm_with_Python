class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def top(self):
        if self.isEmpty():
            return None
        return self.head.data

    def push(self, data):
        node = Node(data)
        if self.isEmpty():
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def pop(self):
        if self.isEmpty():
            return None
        data = self.head.data
        self.head = self.head.next
        return data

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next