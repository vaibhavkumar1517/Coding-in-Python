n = int(input())
arr = [i for i in range(1,n+1)]
if n==1:
    print(1)
    exit(0)
if n==3 or n==2:
    print("NO SOLUTION")
    exit(0)
odd = -1    
for i in range(n):
    if arr[i]%2==0:
        odd = odd + 1
        arr[odd],arr[i] = arr[i],arr[odd]
arr = arr[:odd+1] + sorted(arr[odd+1:])
print(*arr)            