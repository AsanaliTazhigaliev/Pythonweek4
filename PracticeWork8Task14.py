import math
a=str(input("Write a text: "))
b=0
list(a)
for i in range(math.ceil(len(a)/2)):
    if a[i]=="n":
        a.replace("n","*")
        b+=1
print(str(b),"amount of removed")
