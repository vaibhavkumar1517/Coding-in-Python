array = [2,3,7,8,10]
sum_ = 10
n = len(array)
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
    return t[n][sum_]
if subsetsum(array) == True:
    print("True")
else:
    print("False")                        