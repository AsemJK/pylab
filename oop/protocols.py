a = 43
b = 6.7

print(a.__add__(b)) #result is NotImplemented, Why?
                    # because a and b are of different types
print(a.__radd__(b)) #result is 50.7, Why?
                     # because a is int and b is float, so a.__radd__(b) is called
                     # and it is equivalent to b.__add__(a)
print(b.__add__(a)) #result is 50.7, Why?
                     # because b is float and a is int, so b.__add__(a) is called
                     # and it is equivalent to a.__radd__(b)
