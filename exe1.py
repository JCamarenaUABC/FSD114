# Python program to illustrate string
# with unique characters using
# brute force technique

def uniqueChar(caracter):

    # If at any time we encounter 2
    # same characters, return false
    for i in range(len(caracter)):
        for j in range(i + 1, len(caracter)):
            if(caracter[i] == caracter[j]):
                return False

    # If no duplicate characters
    # encountered, return true
    return True


# Driver Code
caracter = "jesu"

if(uniqueChar(caracter)):
    print("%s has all unique characters" % caracter)
else:
    print("%s has duplicate characters" % caracter)
