# Python Distilled (Book Notes)

## Objects & Classes

### Notes

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
