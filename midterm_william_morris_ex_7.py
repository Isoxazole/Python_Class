"""Right now, this only works to get the first perfect number,
Not sure why it's not getting the rest"""



def integers():
    i = 1
    while True:

        yield i
        i = i + 1

perfectNumbers = (i for i in integers() if sum(x for x in range(1,i) if i % x == 0) == i)



def take(n, seq):
    seq = iter(seq)

    result = []

    try:
        for i in range(n):
            result.append(next(seq))
    except StopIteration:
        pass
    return result


print(take(4, perfectNumbers))