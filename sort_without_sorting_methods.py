def SEGREGATE_EVEN_TO_THE_LEFT_AND_ODD_TO_THE_RIGHT(arr,indx):
    odd = -1
    for i in range(indx):
        if (arr[i] %2 == 0):
            odd = odd + 1
            arr[odd],arr[i] = arr[i],arr[odd]
    return (arr)        


def MOVE_ZEROES_TO_END(arr,n):
    left = 0
    for right in range(n):
        if (arr[right] != 0):
            arr[left],arr[right] = arr[right],arr[left]
            left = left + 1
    return (left)   
         

if __name__=='__main__':
    arr = [0,0,1,2,1,2,2,2,1,0,0]
    n = len(arr)
    FIRST_INDEX_OF_ZERO = MOVE_ZEROES_TO_END(arr,n)
    NEW_ARRAY = SEGREGATE_EVEN_TO_THE_LEFT_AND_ODD_TO_THE_RIGHT(arr,FIRST_INDEX_OF_ZERO)
    # NOW I WILL JUST REVERSE THE ARRAY
    start = 0
    end = len(arr) - 1
    while (start <= end):
        arr[start],arr[end] = arr[end],arr[start]
        start = start + 1
        end = end - 1
    print(*arr)    