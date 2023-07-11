class Node:
    def __init__(self, value, next = None):
        self._value = value
        self._next = next

    def value(self):
        return self._value

    def next(self):
        return self._next


class LinkedList():
    def __init__(self, values=[]):
        self.values = []
        self.values.extend(values)
        self._head = None
        for value in values:
            node = Node(value, self._head)
            self._head = node


    def __len__(self):
        return len(self.values)


    def __iter__(self):
        output = []
        node = self._head
        while not node is None:
            output.append(node.value())
            node = node.next()
        return iter(output)
    

    def head(self):
        if not len(self.values) > 0:
            raise EmptyListException("The list is empty.")
        return self._head
    

    def push(self, value):
        self.values.append(value)
        node = Node(value, self._head)
        self._head = node


    def pop(self):
        if not len(self.values) > 0:
            raise EmptyListException("The list is empty.")
        node = self._head
        self._head = self._head.next()
        self.values.pop()
        return node.value()
    

    def reversed(self):
        output = [node for node in self]
        return output[::-1]


class EmptyListException(Exception):
    def __init__(self, message):
        self.message = message
