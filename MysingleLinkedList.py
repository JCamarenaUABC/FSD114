from node import Node


class singleLinkedList:

    def __init__(self):
        self.head = None

    def push(self, data):
        pass

    def insert_after(self, data):
        pass

    def append(self, data):
        temp = Node(data)
        current = self.head
        while current:
            if current.next == None:
                break
            current = current.next
        current = temp

    def remove(self, data):
        pass

    def print_list(self, data):
        pass
