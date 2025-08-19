1. Initiate array: arr = np.array([1,25,8])
2. Mask: 
    ``` python
    import numpy as np
    arr = np.array([1,25,8])
    mask = arr % 2 == 0
    filterred_arr = arr[mask]
    print(filterred_arr)
    ```