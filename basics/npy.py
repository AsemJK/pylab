import numpy as np
from collections import Counter

a = np.array([1, 2, 3, 4, 5])

a_c = Counter(a.tolist())
print(a_c)  # Output: Counter({1: 1, 2:

mask = a % 2 == 0
print(a[mask])  # Output: [2 4]

print(a[a > 2])  # Output: [3 4 5]