# Question 1
def make_skipper(n):
    """Return a function that takes int x as an input and prints all numbers between 0 and x, skipping every nth number (meaning skip any value that is a multiple of n).
    Args:
        n (int): Multiple that must be skipped when printing
        x (int): Upper limit of numbers that must be printed by the inner function.
    Return:
        function: make_skipper returns a function that prints and has no return.

    >>> a = make_skipper(2)
    >>> a(5)
    1
    3
    5
    """
    def print_range(x, print_this=1):
        if print_this <= x:
            if print_this % n != 0:
                print(print_this)
            print_range(x, print_this+1)
    return print_range

# EXTRA: Question 2
def make_alternator(f, g):
    """Return a function that takes in an int x and prints all the numbers between 1 and x, applying function f to every odd-indexed number and g to every even_indexed number before printing.
    Args:
        x (int): Upper range of index numbers to be printed.
        f (function): Function that is to be applied to every odd-indexed number before printing.
        g (function): Function that is to be applied to every even_indexed number before printing.
    Return:
        function: make_alternator returns a function that prints integers and has no return.
    
    >>> a = make_alternator(lambda x: x * x, lambda x: x + 4)
    >>> a(5)
    1
    6
    9
    8
    25
    >>> b = make_alternator(lambda x: x * 2, lambda x: x + 2)
    >>> b(4)
    2
    4
    6
    6
    """
    def printer(x, index=1):
        if index <= x:
            if index % 2 == 1:
                print(f(index))
            elif index % 2 == 0:
                print(g(index))
            printer(x, index+1)
    return printer

# Recursion

# Question 1a
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# Question 1c
def mystery(n):
    # Recursive summation function
    if n == 0:
        return 0
    else:
        return n + mystery(n-1)

def foo(n):
    # Fake Fibonacci sequence, only return 0
    if n < 0:
        return 0
    return foo(n - 2) + foo(n - 1)

def fooply(n):
    if n < 0:
        return 0
    return foo(n) + fooply(n-1)

