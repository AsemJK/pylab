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

