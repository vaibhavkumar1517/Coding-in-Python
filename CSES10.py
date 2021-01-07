n = int(input())
if n<=4:
    print(0)
    exit(0)
else:    
    i = 5
    ans = 0
    while i<=n:
        ans = ans + int(n//i)
        i = i*5
    print(ans)

