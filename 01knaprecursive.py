wt = [1,3,4,5]
val = [1,4,5,7]
w = 7
def knapsack(wt,val,w,n):
    if n==0 or w==0:
        return 0
    if wt[n-1] <= w :
        return max(val[n-1]+knapsack(wt,val,w-wt[n-1],n-1) , knapsack(wt,val,w,n-1)) 
    elif wt[n-1]>w:
        return knapsack(wt,val,w,n-1)
print("Max Profit is : ",knapsack(wt,val,w,len(wt)))               