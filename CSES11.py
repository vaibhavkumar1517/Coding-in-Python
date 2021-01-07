t = int(input())
while t:
    a,b = list(map(int,input().split()))
    if a==0 or b==0:
        print("NO")
    else:    
        if (a+b)%3!=0 or 2*a<b or 2*b<a:
            print("NO")
        else:
            print("YES")    
    t=t-1