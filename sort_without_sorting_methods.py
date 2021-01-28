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
    
    
'''
The Problem statement requires us to sort an array of integers, where integers are in { 0 ,1 , 2 }. But we have a constraint that we cannot use any sorting methods . My approach has been broken down in the following steps:
Example for sample testcase: [ 0 , 1 , 2 , 1 , 0 ]
1. Move all zeroes to end.
Now we have array as [ 1 , 2 , 1 , 0 , 0 ]
2. Segregate even elements to the left and odd elements to the right.
Now we have array as [ 2 , 1 , 1 , 0 , 0 ]
3. Simple reverse the array.
So we get the final desired output as [ 0 , 0 , 1 , 1 , 2 ]
All the above steps take O ( N ) Time Complexity and O ( 1 ) Space Complexity which is actually a constraint in the problem statement .
'''
