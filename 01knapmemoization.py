wt = [1,3,4,5]
val = [1,4,5,7]
w = 7
global t
t = [[-1]*10]*10
def knapsackmemoization(wt,val,w,n):
    if n==0 or w==0:
        return 0
    if t[n][w] != -1 :
        return t[n][w]
    if wt[n-1]<=w:
        t[n][w] = max(val[n-1]+knapsackmemoization(wt,val,w-wt[n-1],n-1) , knapsackmemoization(wt,val,w,n-1))
        return t[n][w]
    elif wt[n-1]>w:
        t[n][w] = knapsackmemoization(wt,val,w,n-1)
        return t[n][w]
print("Maximum Profit is : ",knapsackmemoization(wt,val,w,len(wt)))                    