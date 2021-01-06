class List:
    def __init__(self, data):
        self.data = data
        self.id = None


def is_polindromo(text):

    tmp = text
    arr = []

    ispalindromo = True

    while tmp != None:
        arr.append(tmp.data)
        tmp = tmp.id

    while text != None:

        i = arr.pop()

        if text.data == i:
            ispalindromo = True
        else:
            ispalindromo = False
            break

        text = text.id

    return ispalindromo


#word = "abdddcba"
word = "jesusddusejff"
#word = "jesususej"

ll = List(word[0])

for char in word[1:]:
    ll.id = List(char)

result = is_polindromo(ll)

print(word, " is Palindrome? ", result)
