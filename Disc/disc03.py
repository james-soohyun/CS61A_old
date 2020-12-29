# Question 1.1
def is_prime(n):
    """Returns a boolean value representing if int n is a prime number. Recursive implementation.
    Args:
        n (int): Number being checked
    Return:
        (bool): True if n is a prime number, False otherwise
    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False
    """
    if n==1:
        return True
    def prime_helper(divisor):
        if divisor == 1:
            return True
        elif n % divisor == 0:
            return False
        else:
            return prime_helper(divisor-1)
    return prime_helper(n//2)

# Question 1.2
def make_func_repeater(f, x):
    """Returns a function which takes an int i as its sole argument, which in turn returns the result of applying function f to int x int i times.
    Args:
        f (func): Function which is applied to int x
        x (int): Argument of function f
        i (int): Number of times f is applied to x
    Return:
        repeat (func): Function that is returned by make_func_repeater
    
    >>> incr_1 = make_func_repeater(lambda x: x + 1, 1)
    >>> incr_1(2) #same as f(f(x))
    3
    >>> incr_1(5)
    6
    """

    def repeat(i, x=x):
        if i == 0:
            return x
        else:
            return repeat(i-1, f(x))
    return repeat