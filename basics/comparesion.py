a = [6,5,4]
b = [6,5,4]

if(a is b):
    print("same object")
else:
    print(f"id if a is: {id(a)}")
    print(f"id if b is: {id(b)}")
    print("a and b are different objects")
if(a == b):
    print("same value")
if(type(a) is type(b)):
    print("same type")

#is operator compare between ids of objects
# == operator compare between values of objects
# type() function return type of object
