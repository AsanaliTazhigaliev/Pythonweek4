n = int(input())
o = oct(n)[2:]
print('0'*(10-len(o)), o, sep='')