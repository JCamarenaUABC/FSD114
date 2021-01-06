import sys


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


"""def fact(n):
    if n == 0:
        return 1
    return n*fact(n-1)
"""


def fact(n):
    return 1 if not n else n*fact(n-1)


def factloop(n):
    fact = 1
    x = 1

    while x <= n:
        fact = fact * x
        x = x + 1

    return fact


def fib(n):
    if n < 2:
        return n

    return fib(n-1) + fib(n-2)


"""
def fibonacci():
    variable1 = 0
    variable2 = 1

    print("%s" % str(variable1))
    for x in range(0, 21):
        print("%s" % str(variable2))
        variable1 = variable2
        variable2 += variable1
"""

if __name__ == "__main__":
    # test()
    #numero = sys.argv[1]
    # print(factloop(90000))

    for i in range(10):
        print(fib(i))

    # print(fib(5))
