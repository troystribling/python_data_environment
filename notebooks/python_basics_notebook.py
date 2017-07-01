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
def my_decorator(some_function):
    def wrapper():
        print("Before some function")
        some_function()
        print("After some function")

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
    def wrapper(*args, **kwargs):
        print("wrapper")
        return f(*args, **kwargs)
    return wrapper

@another_decorator
def some_other_function():
    print("some_other_function")

some_other_function()

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
