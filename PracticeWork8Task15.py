a=str(input("Write a text: "))
n=str(input("Given word: "))
b=0
a=a.split(" ")
for i in range(len(a)):
    if a[i]==n:
        b+=1
print(str(b),"amount of repeatings")
