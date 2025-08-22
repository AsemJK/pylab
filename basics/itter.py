#set
l = [34,(4,6),'me']
st = {1,2,3,*l}
print(st)
print(type(st)) # <class 'set'>

'''

import array as arry
t = (2,3,4)
print(type(t)) # <class 'tuple'>

list = [1,2,3]
print(type(list)) # <class 'list'>

arr = arry.array('i',[1,2,3]) #i is for integer
print(arr[1])
print(type(arr)) # <class 'array.array'>


#seperator
print('-----------')


from numpy import array
x = array([1,2,3])
y = array([4,5,6])
z = 9
print(x @ y)
print(x | y)
print(x & y)
print(z << 2) # this is left shift, equivalent to x * 2**2 ,explain: 
print(z >> 2) # this is right shift, equivalent to x // 2**2
print(z ^ 2) # this is XOR, equivalent to x ^ 2
print(z & 2) # this is AND, equivalent to x & 2
print(z | 2) # this is OR, equivalent to x | 2

print(2^2) # this is XOR (exclusive OR) - returns 1 if bits are different, 0 if same. Here 2 (10) XOR 2 (10) = 0

a = 8
b = 9
c = a if a <=b else b
print(c) # 8








print('-----------')
import math
f = math.sqrt(4)
print(f)  # Output: 2.0

a=[1,2,3]
# b = a
b = [1,2,3]
print(id(a) == id(b))
print(a is b)
print(a == b)


'''