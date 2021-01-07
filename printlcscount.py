a = "acbcf"
b = "abcdaf"
m = len(a)
n = len(b)
t = [[None for i in range(n+1)] for j in range(m+1)]
for i in range(m+1):
    for j in range(n+1):
        if i==0 or j==0:
            t[i][j] = 0   
for i in range(1,m+1):
    for j in range(1,n+1):
        if a[i-1] == b[j-1] :
            t[i][j] = 1 + t[i-1][j-1]
        else:
            t[i][j] = max( t[i-1][j] , t[i][j-1] )
print(t[m][n])                      