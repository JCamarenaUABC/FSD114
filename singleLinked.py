
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, prev_node, new_adata):
        if prev_node is None:
            print("The given previous node must inlikedList.")
            return

            new_node = Node(new_data)
            new_node.next = prev_node.next

            prev_node.next = new_done

    def append2(self, data):
        temp = Node(data)
        current = self.head

        while current:
            if current.next == None:
                break
            current = current.next
        current = temp

    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while(last.next):
            last = last.next

        last.next = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print("%d" % (temp.data))
            temp = temp.next

    def deleteNode(self, key):
        temp = self.head

        if (temp is not None):
            if(temp.data == key):
                self.head = temp.next
                temp = NotImplemented
                return

        while(temp is not None):
            if temp.data == key:
                break

            prev = temp
            temp = temp.next

        if(temp == None):
            return

        prev.next = temp.next

        temp = None


if __name__ == '__main__':

    llist = LinkedList()
    llist.append(6)
    llist.push(7)
    llist.push(1)
    llist.push(3)
    llist.push(2)

    #llist.insertAfter(llist.head.next, 8)

    #print 'Created linked list is:',
    print('Created linked list:')
    llist.printList()
    llist.deleteNode(1)

    print('\nLinked List after Deletion of 1:')
    llist.printList()
