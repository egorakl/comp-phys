fib = [1,1]
cube,sq = 0,0

while True:
  fib.append(fib[-1] + fib[-2])
  if fib[-1] >= (4e+6):
    break

for x in fib:
  if(x % 2 == 0):
    cube += x**3
    sq += x**2
    
print(cube/sq)
