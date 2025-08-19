from collections import Counter
my_list = ['a','v','a','d','r']
counter: Counter[str] = Counter(my_list)
print(counter)#Output: Counter({'a': 2, 'v': 1, 'd': 1, 'r': 1})
#Beauty the output
for key, value in counter.items():
    print(f"{key} : {value}")