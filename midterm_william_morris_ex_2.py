def integers():
    i = 1
    while True:

        yield i
        i = i + 1


even = (x for x in integers() if x % 2 == 0)
odd = (x for x in integers() if x % 2 == 1)


def take(n, seq):
    seq = iter(seq)

    result = []

    try:
        for i in range(n):
            result.append(next(seq))
    except StopIteration:
        pass
    return result


print(take(10, even))
print(take(10, odd))
