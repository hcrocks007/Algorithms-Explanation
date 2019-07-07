# Linear search

def linear_search(arr, target):
    # First define a flag so that it is 0
    # if target is not in the array
    
    flag = 0
    for i in range(0,len(arr)):
        if arr[i] == target:
            flag = 1
            break
        
    # checking whether target is in the arr
    
    if flag == 0:
        return -1
    else:
        return i + 1
    