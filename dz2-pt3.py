d = {1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}
k = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

def convert(a):
  r = ''
  ar = a
  while ar != 0:
    for i in range (len(k)):
      if ar >= k[i]:
        r += (d[k[i]])
        ar -= k[i]
        break
  return r

print(convert(14)) #XIV
print(convert(737)) #DCCXXXVII
print(convert(1287)) #MCCLXXXVII
print(convert(1910)) #MCMX
print(convert(1974)) #MCMLXXIV
print(convert(1999)) #MCMXCIX
print(convert(2014)) #MMXIV
