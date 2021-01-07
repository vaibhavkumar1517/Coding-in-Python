from itertools import permutations
s = input()
s = sorted(s)
l = list(s)
p = permutations(l)
ll = []
for i in p:
    if "".join(i) not in ll:
        ll.append("".join(i))
print(len(ll))
for i in ll:
    print(i)    