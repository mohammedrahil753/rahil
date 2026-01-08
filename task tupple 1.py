n=("1","2","3","4")
m=list(n)
print(m[0])
print(m[-1])
m.append("5")
del m[1]
n=tuple(m)
print(n)
print(len(n))