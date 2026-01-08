##Q1)
# list=[]
# evenlist=[]
# oddlist=[]
# n=int(input("enter the elments"))
# for i in range (n):
#     user_input=int(input("enter the number"))
#     list.append(user_input)
#     print(list)
# for i in list:
#     if i%2==0:
#         evenlist.append(i)
#     else:
#         oddlist.append(i)
# print("evenlist=",evenlist)
# print("oddlist=",oddlist) 
##Q2)   
# list=[]
# unique=[]
# n=int(input("enter the elements"))
# for i in range(n):
#     user_input=int(input("enter the number"))
#     list.append(user_input)
#     print(list)
# for i in list:
#     if list.count(i)==1:
#         unique.append(i)  
# print(unique)
# print(len(unique))  
##Q3)
# a=(1,2,3,4,5,6)
# b=list(a)
# b.remove(max(b))
# secondlargest=max(b)
# a=tuple(b)
# print("secondlargest=",secondlargest)
    ## or
# a=(1,2,3,4,5,6)
# b=list(a)
# b.sort()
# secondlargest=b[-2]
# a=tuple(b)
# print("secondlargest=",secondlargest)
###Q4)
# a=(7,33,22,45,9,44,50,70,9)
# b=list(a)
# divisible=[]
# modulos=[]
# remaining=[]
# for num in b:
#     if num % 7==0:
#         divisible.append(num)
#     elif num % 2==0:
#         modulos.append(num)  
#     else:
#         remaining.append(num)
# a=tuple(b)        
# print("%=",divisible) 
# print("@=",modulos)             
# print("&=",remaining)
###       or
# a=[]
# # b=list(a)
# divisible=[]
# modulos=[]
# remaining=[]
# n=int(input("enter the elements"))
# for i in range(n):
#     userenter=int(input("enter the number"))
#     a.append(userenter)
#     print(a)
# b=list(a)
# for num in b:
#      if num % 7==0:
#          divisible.append(num)
#      elif num % 2==0:
#          modulos.append(num)  
#      else:
#         remaining.append(num)
# a=tuple(b)        
# print("%=",divisible) 
# print("@=",modulos)             
# print("&=",remaining)
     ###OR
# n=int(input("enter the number"))
# sum=0
# for i in range(n+1):
#  sum+=i
# print(sum)
#     ##OR
# word=str(input("enter the character"))
# reverse=""
# for x in word:
#     reverse=x+reverse;
# if word==reverse:
#     print("palandrome")
# else:
#     print("not palandrome")
#     ##OR
# str=input("enter the string")
# punctation=("!@#$$%%^&&**(())_+=-{}[]:;'<>/.,")
# chr=""
# for x in str:
#     if x not in punctation:
#         chr+=x
# print(chr)
# OR
import string
n=input("enter the string")
chr=""
for i in n:
    if i not in string.punctuation:
        chr+=i
print(chr)