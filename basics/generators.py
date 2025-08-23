nums = [1,2,3,4]

squares = (x*x for x in nums)
#total without generator
total = sum(x*x for x in nums)
print(total)

#total using generator
total = sum(i for i in squares)
print(total)


squares = (x*x for x in nums)

x = next(squares)
print(x) # 1
x = next(squares)
print(x) # 4
x = next(squares)
print(x) # 9
x = next(squares)
print(x) # 16

print(squares)
print(type(squares)) # <class 'generator'>
for i in squares:
    print(i)

