##Q1)
# movie=["a","b","c","d","e"]
# print(movie[0])
# print(movie[-1])
# movie[1]="f"
# print(movie)
##Q2)
# fruits=["a","b","c","d","e"]
# fruits.append("g")
# fruits.insert(2,"h")
# print(fruits)
##Q3)
# marks=["22","3","11","99","54"]
# marks[1]="33"
# marks.append("88")
# del marks[3]
# print(marks)
##Q4)for loop
# evenlist=[]
# oddlist=[]
# for i in range(1,31):
#     if i%2==0:
#         evenlist.append(i)
#     else:
#         oddlist.append(i)   
# print("evenlist=",evenlist)
# print('oddlist=',oddlist)     
###while loop    
evenlist=[]
oddlist=[]
i=0
while i<=30:
    if i%2==0:
         evenlist.append(i)
    else:
         oddlist.append(i)  
    i+=1          
print("evenlist=",evenlist)
print('oddlist=',oddlist)    