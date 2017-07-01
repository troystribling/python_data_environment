# %%
from functools import wraps

# %%
# functions as objects
def foo(bar):
    return bar + 1

print(foo)

def call_foo(foofoo, arg):
    return foofoo(arg)

call_foo(foo, 3)

# %%
# returning a function

def parent(num):
    def first():
        return "first"
    def second():
        return "second"
    if num == 10:
        return first
    else:
        return second

parent(1)()
parent(10)()

# %%
# decorator pattern example
def my_decorator(f):
    def wrapper():
        print("Before function")
        f()
        print("After function")

    return wrapper

def a_function():
    print("a function")

decorated = my_decorator(a_function)
decorated()

@my_decorator
def another_function():
    print("another_function")

another_function()

# %%
# @wraps decorator example
def another_decorator(f):
    @wraps(f)
    def wrapper(*args):
        print("wrapper")
        return f(*args)
    return wrapper

@another_decorator
def some_other_function():
    print("some_other_function")

some_other_function()

# %%
# decorator with arguments
def deorator_with_args(arg):
    def decorator(f):
        print("arg: %(arg)" % locals())
        
# %%
# class example
class Thing(object):
    def __init__(self, value):
        self.value = value

thing = Thing(5)
thing.value

# %%
# simple class decorator
class Pizza(object):
    def __init__(self):
        self.toppings = []
    def __call__(self, topping):
        print("adding topping")
        self.toppings.append(topping())
    def __repr__(self):
        return str(self.toppings)

pizza = Pizza()

@pizza
def cheese():
    return 'cheese'

@pizza
def sauce():
    return 'sauce'

print(pizza)
