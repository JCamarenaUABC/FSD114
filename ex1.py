def is_unique(word):
    seen = set()
    for letter in word:
        if letter in seen:
            return False
        seen.add(letter)
    return True


if __name__ == "__main__":
    word_list = ["abcc", "abcde", "abbcde"]
for word in word_list:
    print("%s is unique? -> %s" % (word, is_unique(word)))
