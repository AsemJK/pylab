a = list()
print(a)

a= (5,6)

if isinstance(a, (list,tuple)):
    print("a is a list or tuple")
else:
    print("a is not a list")

print(type(a).__name__)