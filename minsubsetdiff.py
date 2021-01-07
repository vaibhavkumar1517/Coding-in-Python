array = [1,2,7]
sum_ = sum(array)
n = len(array)
l = []
t = [[None for i in range(sum_ +1 )] for j in range(n + 1)]
for i in range(n+1):
    for j in range(sum_ + 1):
        if i == 0:
            t[i][j] = False
        if j == 0:
            t[i][j] = True

def subsetsum(array):
    for i in range(1,n+1):
        for j in range(1,sum_ + 1 ):
            if array[i-1] <= j :
                t[i][j] = (t[i-1][j - array[i-1]]) or (t[i-1][j])
            else:
                t[i][j] = t[i-1][j]               
    for j in range(0,int(sum_ // 2 )+1):
        if t[n][j] == True:
            l.append(j)
    min_ = float("inf")
    for i in range(len(l)):
        min_ = min( min_ , sum_ - (2 * l[i]))
    return (min_)    

print("Minimum Subset Sum Difference is : ", subsetsum(array))                    