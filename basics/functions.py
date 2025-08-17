'''d = ['x','y','z']
#test = d.pop(1,'default_value')
test = d.pop(1)
print(test)  # Output: y
'''

#finction hints
def some_func(arg1: int, arg2: str, / ,*args,**kwargs):
    """
    This function takes an integer and a string as positional-only arguments,
    and accepts additional keyword arguments.
    """
    return None  # This function does not return anything
#example usage
some_func(42, "example", key1="value1", key2="value2")
# Output: None, as the function does not return anything


def factorial(n):
    '''Calculate the factorial of a non-negative integer n.
    Args:
        n (int): A non-negative integer for which to calculate the factorial.'''
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)
    #usage example
print(factorial(5))  # Output: 120

