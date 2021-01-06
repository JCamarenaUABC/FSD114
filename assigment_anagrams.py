
def isAnagram(word1, word2):
    list1 = list(word1)
    list1.sort()
    list2 = list(word2)
    list2.sort()

    return (list1 == list2)


if __name__ == "__main__":
    word1 = "Jesus"
    word2 = "suseJ"
    valAnagram = isAnagram(word1, word2)

    print("%s | %s | Are anagrams? [ %s ]" % (word1, word2, valAnagram))
