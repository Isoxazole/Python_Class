"""
Homework 5, Exercise 2
William Morris
3/04/19
This program has a @cache decorator that will save the calculations in a
function attribute dictionary.

Description of difference:
When using the cache for the fibonacci sequence, the function is only
called twice: once at the beginning and once at the end (call 1 and 12)
However when no cache is used, the function is called every time when
recalculating numbers.
"""
import functools

def cacheFunction(func):
    cache = {}
    def cacheWrapper(*args, **kwargs):
        if args not in cache:
            cache[args] = func(*args, **kwargs)
        return cache[args]
    return cacheWrapper


def countCalls(func):
    @functools.wraps(func)
    def wrapperCountCalls(*args, **kwargs):
        wrapperCountCalls.numCalls += 1
        print(f"Call {wrapperCountCalls.numCalls} of {func.__name__!r}")
        return func(*args, **kwargs)
    wrapperCountCalls.numCalls = 0
    return wrapperCountCalls


@countCalls
@cacheFunction
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


noCache = countCalls(fibonacci)
yesCache = countCalls(cacheFunction(fibonacci))
print("No cache: \n")
print(noCache(6))
print("\nYes cache: \n")
print(yesCache(6))
