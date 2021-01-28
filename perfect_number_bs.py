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

''' 
The problem statement requires us to find if the given number is a Perfect Number or not. Well the definition of the Perfect Number is as follows: If a given number is a 
square root of a positive INTEGER type number then it is said to be Perfect Number. For example 9 is a perfect number because ( 3 * 3 ) = 9. If the number is not a 
Perfect Number then we have to simply return -1.
My approach is using an array of numbers and performing Binary Search on them to get to the desired result. Well, one might go for the array elements from 1 till N , where 
N is the given number. But my approach is to make sure that the last element in the array I am initializing is minimum as possible which will in turn reduce the number of
comparison in the Binary Search procedure. So to reduce the last number in the array my steps are:
Explaining test cases with number ' 81 ' and ' 169 '.
1. Firstly find the number of digits in the given number.( I found the number of digits using logarithmic approach which takes O(1) Time Complexity. )
So they are, for 81 it is 2 and for 169 it is 3.
2. Now if the number of digits is less than equal to 2 then divide the number by 2 to get the last number in the array. And if the number of digits is greater than 2, then
divide the number by 10 to get the last number in the array.
So, for 81, my array will be from 1 till 40 ( 81//2 ). For 169, my array will be from 1 till 16 ( 169//10 ).
3. Now we perform binary search and compute the result.
The code has been optimized upto some extent as the array has been shortened as earlier it was supposed to be from 1 till N, but now it is from 1 till some modified smaller N.
The GitHub Link for the code I wrote: https://github.com/vaibhavkumar1517/Coding-in-Python/edit/main/perfect_number_bs.py
'''
