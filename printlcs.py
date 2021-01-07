a = "acbcf"
b = "abcdaf"
m = len(a)
n = len(b)
temp_string = ""
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
i=m
j=n
while i>0 and j>0 :
    if a[i-1] == b[j-1] :
        temp_string = a[i-1] + temp_string
        i = i-1
        j = j-1
    else:
        if t[i-1][j] > t[i][j-1] :
            i = i - 1
        else:
            j = j - 1
print("LCS is : ",temp_string)                                        