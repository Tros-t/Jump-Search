from math import sqrt as sqt

def jump_search(arr,x):
    n = len(arr)
    m = sqt(n)
    
    prev = 0
    while arr[int(min(m, n)-1)] < x:
        prev = m
        m += m
        if prev >= n:
            return -1
    
    prev=int(prev)    
    while arr[prev] < x:
        prev += 1
    
        
    return prev, arr[prev]
     

arr = [23, 234, 231, 98, 156, 250, 121, 345, 921, 129]
arr.sort()

print(jump_search(arr, 345))