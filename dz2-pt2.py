d = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

def convert(r):
    a = 0
    for i in range(len(r)):
        if i > 0 and d[r[i]] > d[r[i-1]]:
            a += d[r[i]] - 2*d[r[i-1]]
        else:
            a += d[r[i]]
    return a

print(convert('XXXIX')) #39
print(convert('CCXLVI')) #246
print(convert('MLXVI')) #1066
print(convert('MDCCLXXVI')) #1776
print(convert('MCMLXXIV')) #1974
