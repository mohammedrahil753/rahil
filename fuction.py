# def a():
#     print("rahil")
# a()
#     or
# def a():
#     return("rahil")
# print(a())
# #     or
# def farenheat(celcius):
#     return (celcius-32)*5/9
# print(farenheat(100))  
# print(farenheat(50))
# print(farenheat(0))
#     ##OR 
# def a(name):
#     print("hi",name)
# a("rahil")
# or
# def a(name):
#     return("hi"+""+name)
# print(a("rahil"))
# def name(fname,lname):
#     print(fname+lname)
# name("mohammed"," rahil")
# def my_function(animal,name):
#     print("I Have A",animal)
#     print("my",animal+"'s name is ",name)
# my_function(animal="dog",name="tom")
# def my_function(fruits):
#     for fruits in fruits:
#         print(fruits)
# my_fruits=["apple","banana","cherry"]
# my_function(my_fruits)
# def my_function(person):
#     print("Name :",person["name"])
#     print("Age :",person["age"])
# my_person={"name":"Rahil","age":"22"}
# my_function(my_person)
# def my_function(x,y):
#     return(x+y)
# result=my_function(5,3)
# print(result)
# def my_function(x):
#     if x%2==0:
#         return("even")
#     else:
#         return("odd")
# result=int(input("enter the number"))
# print(my_function(result))
# def my_function(x):
#     return(x*x)
# z=int(input("enter the number"))
# print(my_function(z))
# def my_function(greeting,*names):
#     for name in names:
#         print(greeting,name)
# my_function("hello","emil","tobis","refnesnes")
# def my_function(*numbers):
#     total=0
#     for num in numbers:
#         total+=num
#     return total
# print("total:",my_function(1,2,3))
# print("total:",my_function(20,3,50,7))
# print("total:",my_function(5))
# def my_function(*numbers):
#     if len(numbers)==0:
#         return(None)
#     max_num=numbers[0]
#     for num in numbers:
#         if num>max_num:
#          max_num=num
#     return max_num
# print(my_function(3,4,6,2,7,3,7,3,))
# def my_function(title,*args,**kwargs):
#     print("title:",title)
#     print("position arguments:",args)
#     print("keyword arguments:",kwargs)
# my_function("user info:","emil","tobis",Age=25,city="osmo")
# def factorial(n):
#     if n==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(5))
# try:
#     a=int(input("enter the number"))
#     b=int(input("enter the number"))
#     c=a/b
# except ZeroDivisionError:
#     print("cannot divide by zero")
# except ValueError:
#     print("invalid input")
# else:
#     print("result:",c)
# finally:
#     print("execution completed")
# try:
#     NO=[10,20,30]
#     index=int(input("enter the index"))
#     print("value at index",index,"is",NO[index])
# except IndexError:
#     print("index out of range")
# except ValueError:
#     print("invalid input")
# except Exception as e:
#     print("an error occurred:",str(e))
# except KeyboardInterrupt:
#     print("program interrupted by user")
# finally:
#     print("execution completed")
# import datetime
# x=datetime.datetime.now()
# print(x)
a="rahil"
reversedtext=a[::-1]
print(reversedtext)