# 1. Python Distilled (Book Notes)

## 1.1. Objects & Classes

### 1.1.1. Notes

- install numpy: for python 3 use "pip3 install numpy"

1.  [Numpy](https://github.com/AsemJK/pylab/blob/main/NUMPY.md)
2.  Counter: is from collections package
    Played as aggregate function
    example:

```python
from collections import counter
my_list = ['a','v','a','d','r']
counter: Counter[str] = Counter(my_list)
print(counter)#Output: Counter({'a': 2, 'v': 1, 'd': 1, 'r': 1})
#Beauty the output
for key, value in counter.items():
    print(f"{key} : {value}")
```

3. Single underscore (_) used as a virtual seperator to make big numbers readable, example: 236_254_120 is equal to 236254120
4.  (1, 2, 3) # tuple
    [1, 2, 3] # list
    {1, 2, 3} # set
    {'x':1, 'y':2, 'z':3} # dict
5. Unpacking
    - Unpacking is a way to assign multiple values to multiple variables in a single line
    - example:

```python
a, b, c = (1, 2, 3)
print(a) # 1
print(b) # 2
print(c) # 3
```

- example 2:

```python
a, b, *c = (1, 2, 3, 4, 5)
print(a) # 1
print(b) # 2
print(c) # [3, 4, 5]
```

- example 3:

```python
a, b, *c, d = (1, 2, 3, 4, 5)
print(a) # 1
print(b) # 2
print(c) # [3, 4]
print(d) # 5
```
6. **Control Flow**
- if
- elif
- else
- try
- except
- finally
- raise
- assert
- pass
- break
- continue
- for
- while
- match
- case

7. **Iterations**

```Python
for i in "asem":#i here is named iteration variable
    print(i)
```



The scope of the iteration variable ("i" in our example) is
not **private** to the for statement. If a previously defined variable has the same name, that
value will be overwritten. Moreover, the iteration variable retains

8. **For Loop**

```python
s=[(1,2),(3,4)]
for a,b in s:#Unpacking
    print(a,b) 
    #output: 
    1 2 
    3 4
for x,y in enumerate(s):
    print(x,y)
    #output:
    0 (1, 2)
    1 (3, 4)
```
9. **While Loop**
Executed until condition became false, example:
```python
i=0
while i<5:
    print(i)
    i+=1
```
10. **Break**
Used to exit the loop, example:
```python
i=0
while i<5:
    print(i)
    i+=1
    if i==3:
        break
```
11. **Continue**
Used to skip the rest of the code inside the loop for the current iteration, example:
```python
i=0
while i<5:
    i+=1
    if i==3:#skip the lines of "make some calculations & print"
        continue
    #make some calculations
    print(i)
```
12. **Pass**
Used to do nothing, example:
```python
i=0
while i<5:
    i+=1
    if i==3:
        pass
    print(i)
```
13. **Dictionary vs List**
    - Dictionary: is a collection of key-value pairs , keys must be unique, values can be duplicated , Mutability: Mutable
    - List: is a collection of values with an index , values can be duplicated, Mutability: Mutable
- **examples**:
```python
my_list = [1, 2, 3, 4, 5]
```
- Dictionary:
```python
my_dict = {'a': 1, 'b': 2, 'c': 3}
```
- Accessing values:
```python
print(my_dict['a']) # 1
```
- Adding a new key-value pair:
```python
my_dict['d'] = 4
```
- Removing a key-value pair:
```python
del my_dict['b']
```
- Iterating over keys:
```python
for key in my_dict:
    print(key)
```
- Iterating over values:
```python
for value in my_dict.values():
    print(value)
```
- Iterating over key-value pairs:
```python
for key, value in my_dict.items():
    print(key, value)
```
14. a = ['a','b','c','d','e']
    print(a[2:4]) # ['c','d'] note that the rang start from position 2 and take item at index = 2 but the end not included
                  # so it will take item at index = 3
                  # start <= range < end
                  # if start is not specified it will start from index = 0
                  # if end is not specified it will take all items from start to the end of the list
                  # if start is greater than end it will return empty list
                  # if start is negative it will start from the end of the list
                  # if end is negative it will end at the end of the list
15. **Random**
    To generate random numbers we use "randint" function, example
    ```python
    import random
    r = random.randint(1, 10000)  # Returns a random integer between 1 and 10
    print(r)
    ```
    To generate random float numbers we use "uniform" function, example
    ```python
    import random
    r = random.uniform(1, 10000)  # Returns a random float number between 1 and 10
    print(r)
    ```
    To generate random string we use "choice" function, example
    ```python
    import random
    import string
    r = random.choice(string.ascii_letters)  # Returns a random string
    print(r)
    ```
16. **Class Name Convention**
    - Class names should be in Pascal Case
    - example:
    ```python
    class MyClass:
        pass
    ```