m = 0
sum = 0.0
for i in range(1,7):
  n = float(input())
  if n>0:
    sum = sum+n
    m +=1
print("{} valores positivos".format(m))
print("%0.1f"%(sum/m)) 