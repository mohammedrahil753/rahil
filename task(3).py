# a=["a","g","d","c",'b','h',"k"]
# b=["a","d","h","f","j","l","n","p"]
# c=set(a)
# d=set(b)
# e=c&d
# f=list(e)
# print(f)
# n=int(input("enter the number"))
# c=1
# for i in range(1,n+1):
#     c*=i
# print (c)
n=int(input("enter the number"))
if n<2:
    print("it is not a prime number")
else:
    for i in range(2,n):
        if n%i==0:
            print(n,"it is not a prime number")
            break
    else:
        print(n,"it is a prime number")        