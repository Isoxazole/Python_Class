"""
Homework 5, Exercise 1
William Morris
3/04/19
This program has a @slowDown decorator that will sleep a certain
amount of seconds before it calls the decorated function. The decorator
has an optional rate argument that controls how long it sleeps with a
default value of 1 second.
"""
import time

def slowDown(delay =1):
    def decoratorSlowDown(func):
        def wrapper():
            time.sleep(delay)
            func()
        return wrapper
    return decoratorSlowDown

@slowDown(delay=4)
def sayWhatup():
    print("Yo what up yo?")

sayWhatup()
