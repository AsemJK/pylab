a = [1,2,3]
b = [1,2,3]
print(a is b)  # Output: False, as they are different objects
print(a == b)  # Output: True, as they have the same content

class baseclass:
    def __init__(self, value):
        self.value = value

    def display(self):
        print(f"Value: {self.value}")

#inheritance
class derivedclass(baseclass):
    def __init__(self, value, extra):
        super().__init__(value)
        self.extra = extra

    def display(self):
        super().display()
        print(f"Extra: {self.extra}")

# Example usage
if __name__ == "__main__":
    obj1 = baseclass(10)
    obj1.display()  # Output: Value: 10

    obj2 = derivedclass(20, "extra info")
    obj2.display()  # Output: Value: 20, Extra: extra info
    #isinstance: is a built-in function that checks if an object is an instance of a class or a subclass thereof
    if isinstance(obj1, baseclass):
        print("obj1 is an instance of baseclass")
    if isinstance(obj2, derivedclass):
        print("obj2 is an instance of derivedclass")
    if isinstance(obj2, baseclass):
        print("obj2 is also an instance of baseclass (due to inheritance)")
#reference count
q = 90
import sys
#print(sys.getrefcount(q))  # Output: 2, as the reference count includes the argument passed to getrefcount
#del q
print(sys.getrefcount(q))  # Output: 2, as the reference count includes the argument passed to getrefcount


import gc
print(gc.get_referrers(q))  # Output: [], as there are no other references to q at this point
gc.collect()  # Force garbage collection

from datetime import date
my_date = date(2023, 10, 1)
print(my_date)  # Output: 2023-10-01
print(repr(my_date))  # Output: datetime.date(2023, 10, 1)


lib = {
    'name': 'example_lib',
    'version': '1.0.0',
}
lib['func'] = lambda x: f"Function called with {x}"
lib['math_func_abs'] = abs
lib['math_func_max'] = max
print(lib['func']("test"))  # Output: Function called with test
if __name__ == "__main__":
    print(lib['math_func_abs'](-10))  # Output: 10
    print(lib['math_func_max'](1, 2, 3))  # Output: 3

##
from fractions import Fraction
print(Fraction(3, 4))  # Output: 3/4

#numpy
import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)  # Output: [5 7 9]
# print(np.add(a, b))  # Output: [5 7 9]

