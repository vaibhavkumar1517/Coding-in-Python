wt = [1,3,4,5]
val = [1,4,5,7]
w = 7
n = len(wt)
t = [[None for i in range(w+1)] for j in range(n+1)]
for i in range(n+1):
    for j in range(w+1):
        if i==0 or j==0:
            t[i][j] = 0
def knapsacktopdownapproach(wt,val,w,n):
    for i in range(1,n+1):
        for j in range(1,w+1):
            if wt[i-1] <= j :
                t[i][j] = max(val[i-1] + t[i-1][j-wt[i-1]] , t[i-1][j])
            else:
                t[i][j] = t[i-1][j]
    return t[n][w]
print("Maximum Profit is : ",knapsacktopdownapproach(wt,val,w,n))                                