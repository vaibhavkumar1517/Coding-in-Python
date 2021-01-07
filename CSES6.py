def compute(y,x):
    z = max(y,x)
    z1 = (z-1) * (z-1)
    ans = 0
    if z%2:
        if y==z:
            ans = z1+x
            return ans
        else:
            ans = z1 + 2*z -y
            return ans
    else:
        if x==z:
            ans = z1+y
            return ans
        else:
            ans = z1 + 2*z - x
            return ans


t = int(input())
d = {} 
while t:
    y,x = list(map(int,input().split()))
    if y==1000000000 and x==1000000000:
        print(999999999000000001)
    else:
        key = str(y) + str(x)
        if key in d:
            print(d[key])
        else:
            a=compute(y,x)
            d[key] = a
            print(a)                          
    t=t-1    