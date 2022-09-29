def sumD(n):
    summa=0
    while n!=0:
        summa+=n%10
        n=n//10
    return summa
print(sumD(int(input())))
