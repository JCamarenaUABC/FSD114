def recursive_count_rest(n):
    print(n)
    if n == 0:
        return n
    return recursive_count(n-1)


def recursive_count_plus(n, count):
    print(count)
    if n == count:
        return count
    return recursive_count_plus(n, count+1)


if __name__ == "__main__":
    # recursive_count(15)
    recursive_count_plus(20, 0)
