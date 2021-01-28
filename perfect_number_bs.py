import math 

def SOLVE( num , LAST_VALUE ):
    temp = [i for i in range(1,LAST_VALUE + 1)]
    start = 0
    end = len(temp) - 1
    while ( start <= end ):
        mid = start + ( end - start ) // 2
        if ( temp[mid] * temp[mid] == num ):
            return temp[mid]
        elif ( temp[mid] * temp[mid] > num ):  
            end = mid - 1
        elif ( temp[mid] * temp[mid] < num ):
            start = mid + 1
    return (-1)              


if __name__ == '__main__' :
    num = int(input())
    NUMBER_OF_DIGITS = math.floor( math.log10(num) + 1 )
    if ( NUMBER_OF_DIGITS <=2 ):
        LAST_VALUE_IN_ARRAY = num // 2
    elif ( NUMBER_OF_DIGITS > 2 ):
        LAST_VALUE_IN_ARRAY = num // 10
    answer = SOLVE( num , LAST_VALUE_IN_ARRAY )
    print(answer)    