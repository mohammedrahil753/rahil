# n=["a","b","c"]
# print(n)
# or
# n=["a","b","c"]
# for x in n:
#     print(x)
#     or
# n=list(("a","b","c"))
# print(n)
# or
### acess loop
# n=["a","b","c"]
# print(n[1])
# or
###negative acess
# n=list(("a","b","c"))
# print(n[-1])
# or
### range loops
# n=["a","b","c","d","e","f"]
# print(n[2:5])
# or
# n=["a","b","c","d","e","f"]
# print(n[-4:-1])
# or
### change loop
# n=["a","b","c","d","e","f"]
# n[1]="B"
# print(n)
# or
### chane loop index
# n=["a","b","c","d","e","f"]
# n[2:3]=["C","D"]
# print(n)
# or
### insert
# n=["a","b","c","d","e","f"]
# n.insert(2,"water")
# print(n)
# or
###append loop
# n=["a","b","c","d","e","f"]
# n.append("g")
# print(n)
# or
### extend loop
# n=["a","b","c","d","e","f"]
# y=["a","b","c","d","e","f"]
# n.extend(y)
# print(n)
#or
### remove loop
# n=["a","b","c","d","e","f"]
# n.remove("b")
# print(n)
# or
### delete loop
# n=["a","b","c","d","e","f"]
# del n[0]
# print(n)
# or
# n=["a","b","c","d","e","f"]
# n.pop(0)
# print(n)
### or
### delete completly
# n=["a","b","c","d","e","f"]
# del n
# print(n)
### or
# n=["a","b","c","d","e","f"]
# n.clear()
# print(n)
### or
###list loop
# n=["a","b","c","d","e","f"]
# for x in n:
#     print(x)
#     or
# n=["a","b","c","d","e","f"]
# i=0
# while i <len(n):
#     print(n[i]);
#     i+=1
#or
### sort(assending)
# n=["22","3","11","99","54","22"]
# n.sort()
# print(n)
# or
###sort(dessending)
n=["22","3","11","99","54","22"]
n.sort(reverse=True)
print(n)