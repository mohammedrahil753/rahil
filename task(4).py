# a=(int(input("enter the number")))
# b=(int(input("enter the number")))
# a,b=b,a
# print(a)
# print(b)
# a=(int(input("enter the number")))
# fibnounci=0
# fibnounci1=1
# print("fibnounci=")
# for i in range(a):
#     print(fibnounci,end="")
#     fibnounci2=fibnounci+fibnounci1
#     fibnounci=fibnounci1
#     fibnounci1=fibnounci2
n=str(input("enter the word"))
a=[]
vowels="aeiouAEIOU"
for i in n:
    if i in vowels:
        a.append(i)
print(a)
print(len(a))