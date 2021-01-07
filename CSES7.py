n = int(input())
for k in range(1,n+1):
    totalposition = (k*k) * ((k*k)-1)//2
    attackposition = 4*(k-1)*(k-2)
    print(totalposition - attackposition)
