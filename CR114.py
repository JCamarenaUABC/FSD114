import os
def clear(): os.system('clear')  # on Linux System


class NodeDoubleSingle:
    def __init__(self, data):
        self.data = data
        self.next = None


class NodeDouble:
    def __init__(self, data):
        self.item = data
        self.nref = None
        self.pref = None

############################################


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = NodeDoubleSingle(new_data)
        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, prev_node, new_adata):
        if prev_node is None:
            print("The given previous node must inlikedList.")
            return

            new_node = NodeDoubleSingle(new_data)
            new_node.next = prev_node.next

            prev_node.next = new_done

    def append2(self, data):
        temp = NodeDoubleSingle(data)
        current = self.head

        while current:
            if current.next == None:
                break
            current = current.next
        current = temp

    def append(self, new_data):
        new_node = NodeDoubleSingle(new_data)

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

#######################


class DoublyLinkedList:
    def __init__(self):
        self.start_node = None

    def insert_in_emptylist(self, data):
        if self.start_node is None:
            new_node = NodeDouble(data)
            self.start_node = new_node
        else:
            print("list is not empty")

    def insert_at_start(self, data):
        if self.start_node is None:
            new_node = NodeDouble(data)
            self.start_node = new_node
            print("node inserted")
            return

        new_node = NodeDouble(data)
        new_node.nref = self.start_node
        self.start_node.pref = new_node
        self.start_node = new_node

    def insert_at_end(self, data):
        if self.start_node is None:
            new_node = NodeDouble(data)
            self.start_node = new_node
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        new_node = NodeDouble(data)
        n.nref = new_node
        new_node.pref = n

    def insert_after_item(self, x, data):
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            if n is None:
                print("item not in the list")
            else:
                new_node = NodeDouble(data)
                new_node.pref = n
                new_node.nref = n.nref
                if n.nref is not None:
                    n.nref.prev = new_node
                n.nref = new_node

    def insert_before_item(self, x, data):
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            if n is None:
                print("item not in the list")
            else:
                new_node = NodeDouble(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                n.pref = new_node

    def traverse_list(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item, " ")
                n = n.nref

    def delete_at_start(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        if self.start_node.nref is None:
            self.start_node = None
            return
        self.start_node = self.start_node.nref
        self.start_prev = None

    def delete_at_end(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        if self.start_node.nref is None:
            self.start_node = None
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        n.pref.nref = None

    def delete_element_by_value(self, x):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        if self.start_node.nref is None:
            if self.start_node.item == x:
                self.start_node = None
            else:
                print("Item not found")
            return

        if self.start_node.item == x:
            self.start_node = self.start_node.nref
            self.start_node.pref = None
            return

        n = self.start_node
        while n.nref is not None:
            if n.item == x:
                break
            n = n.nref
        if n.nref is not None:
            n.pref.nref = n.nref
            n.nref.pref = n.pref
        else:
            if n.item == x:
                n.pref.nref = None
            else:
                print("Element not found")

    def reverse_linked_list(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        p = self.start_node
        q = p.nref
        p.nref = None
        p.pref = q
        while q is not None:
            q.pref = q.nref
            q.nref = p
            p = q
            q = q.pref
        self.start_node = p

#######################


if __name__ == "__main__":
    opc = 0

    while(opc != 3):
        try:
            clear()

            print(
                "*****************************Menu options*****************************")
            print("1) SingleLink List \n2) DoubleLinkList \n3) Exit")
            opc = int(input())
            print(
                "**********************************************************************")

            if opc == 1:
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
            elif opc == 2:
                new_linked_list = DoublyLinkedList()

                new_linked_list.insert_in_emptylist(50)

                new_linked_list.traverse_list()

                new_linked_list.insert_at_start(10)
                new_linked_list.insert_at_start(5)
                new_linked_list.insert_at_start(18)

                new_linked_list.insert_at_end(29)
                new_linked_list.insert_at_end(39)
                new_linked_list.insert_at_end(49)

                new_linked_list.insert_after_item(50, 65)

                new_linked_list.insert_before_item(29, 100)

                new_linked_list.delete_at_start()

                new_linked_list.delete_at_end()
                new_linked_list.delete_element_by_value(65)
                new_linked_list.reverse_linked_list()
            else:
                print("Hasta la vista Baby!!!!")

        except:
            print("Error!!!!")

        print("Press enter to continue..")
        input()
