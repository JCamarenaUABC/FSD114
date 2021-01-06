class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        return self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

    def getvalues(self):
        size = self.size()

        print("List Values: %s" % size)

        for x in range(size):
            print("- %s" % self.items[x])

        print("--------------------------------------------------------------")


class Queur2Stacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, element):
        self.stack1.append(element)
        pass

    def dequeue(self):
        #self.stack2[:0] = self.stack1.pop(0)

        while self.stack1:
            self.stack2.append(self.stack1.pop())

        return self.stack2.pop()
        # pass


def test():
    q = Queur2Stacks()

    for i in range(5):
        q.enqueue(i)

    for i in range(5):
        print(q.dequeue())


def balance_check(s):
    if len(s) % 2 != 0:
        return False

    opening = set('([{')
    matches = set([('(', ')'), ('[', ']'), ('{', '}')])

    stack = []

    for paren in s:
        print("paren: %s" % paren)

        if paren is opening:
            stack.append(paren)
            print ("parent is fonund in opening; stack: %s" % stack)
        else:
            if len(stack) == 0:
                print("The stack's lenght is 0, so this is a fail condition.")
                return False
            last_open = stack.pop()
            print("Last open (last item from stack): %s" % last_open)
            temp_tuple = (last_open, paren)

            if temp_tuple not in matches:
                print("Incorrect tuple match: %s" % str(temp_tuple))
                return False
            else:
                print("The tuple was found in matches %s" % str(temp_tuple))

    print("Length of stack: %s" % len(stack))
    return len(stack) == 0


if __name__ == "__main__":

    c = Stack()

    valempty = c.is_empty()
    print("Is empty: %s " % str(valempty))

    print("Add item")
    c.push("Historia de un amor")
    c.push("La negra tomasa")
    c.push("Mandinga")
    c.push("Lagrimas negras")
    c.push("ToroMoro")

    valempty = c.is_empty()
    print("Is empty: %s " % str(valempty))

    size = c.size()
    print("--------------------------------------------------------------")
    c.getvalues()

    peek = c.peek()
    print("Peek: %s" % peek)
    print("--------------------------------------------------------------")

    print("Pop values")
    c.pop()

    c.getvalues()

    print("Balance Check")
    print("--------------------------------------------------------------")

    print(balance_check("{[({})]}"))
    # print(balance_check("{[({])]}"))

    print("-----------Enqueue-Dequeue------------")
    test()
