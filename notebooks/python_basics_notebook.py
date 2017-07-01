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
# function arguments
def foo_args(*args):
    print(f"args: {args}")


foo_args(1,2,3)

def foo_kwargs(**kwargs):
    print(f"kwargs: {kwargs}")

foo_kwargs(city="SF", name="Troy", zip=94110)

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
def decorator_with_args(*outer_args):
    def decorator(f):
        print(f"decorator outer_args: {outer_args}")
        def wrapper(*args):
            print(f"wrapper outer_args: {outer_args}, args: {args}")
            return f(*args)
        return wrapper
    return decorator

@decorator_with_args(1,2,3)
def process_args(*args):
    print(f"process_args: {args}")

process_args(4,5,6)

def wraps_decorator_with_args(*outer_args):
    def decorator(f):
        print(f"wraps_decorator outter_args: {outer_args}")
        @wraps(f)
        def wrapper(*args):
            print(f"wraps_wrapper outter_args: {outer_args}, args: {args}")
            return f(*args)
        return wrapper
    return decorator

@wraps_decorator_with_args(7,8,9)
def wraps_process_args(*args):
    print(f"wraps_process_args: {args}")

wraps_process_args(10,11,12)

# %%
# class example
class Thing(object):
    def __init__(self, value):
        self.value = value

thing = Thing(5)
thing.value

# %%
# class decorator
class Pizza(object):
    def __init__(self):
        self.toppings = []
    def __call__(self, topping):
        print("adding topping")
        self.toppings.append(topping())
    def __repr__(self):
        return str(self.toppings)
    def deliver(self, vendor):
        def decorator(f):
            print(f"pizza delivered by: {vendor}")
            @wraps(f)
            def wrapper(*args):
                return f(*args)
            return wrapper
        return decorator


pizza = Pizza()

@pizza
def cheese():
    return 'cheese'

@pizza
def sauce():
    return 'sauce'

print(pizza)

@pizza.deliver('Dominos')
def delivered(*args):
    print(f"delivered: {args}")

delivered(10, 3)
