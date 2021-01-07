n = int(input())
totalsum = int(n*(n+1) // 2)
if totalsum % 2 !=0:
    print("NO")
else:
    print("YES")
    l1,l2=[],[]
    if n%4:
        j=3
    else:
        j=4
    for i in range(0,int((n-1)//4)):
        l1.append(4*i +1 + j)
        l1.append(4*i + 4 +j)
        l2.append(4*i + 2 +j)
        l2.append(4*i + 3 +j)
    if n%4:
        l1.append(1)
        l1.append(2)
        l2.append(3)
    else:
        l1.append(1)
        l1.append(4)
        l2.append(3)
        l2.append(2)
    print(len(l1))
    print(*l1)
    print(len(l2))
    print(*l2)    


