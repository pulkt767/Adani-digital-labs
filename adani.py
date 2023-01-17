

import random
import numpy as np
def no(r,c):
    arr=[random.randint(1,100) for i in range(r) for j in range(c)]
    return np.reshape(arr,(r,c))
    
    
def sort (arr, index):
    return arr[arr[:,index].argsort()]
r=int(input())
c=int(input())
col_idx=int(input())
print(sort(no(r,c),col_idx))