n=int(input('n= '))
if n>0:
    for i in range (1,n+1):
        a,j=[],i
        while j:
            a.append(j%10);j//=10
            if 0 not in a:
                yes=True
                for b in a:
                    if i%b:yes=False;
                    break
                if yes:
                    print(i,';',sep='')