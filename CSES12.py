s = input()
d = {}
for i in s:
    if i not in d:
        d[i] = 1
    else:
        d[i] = d[i] + 1
oddcount = 0
oddchar = None
for key,value in d.items():
    if (value % 2) !=0:
        oddcount = oddcount + 1
        oddchar = key
if oddcount>1 or (oddcount==1 and len(s)%2==0):
    print("NO SOLUTION")
else:
    first = ""
    last = ""
    for key,value in d.items():
        temp = key*int(value//2)
        first = first + temp
        last = temp + last
    if oddcount==1:
        print(first+oddchar+last)
    else:
        print(first+last)
