a = 0
b = 0
c = 0
d = 0
for i in range(1,6):
    n = float(input())
    if n%2==0:
      a +=1
    if n%2 !=0:
      b +=1
    if n>0:
      c +=1
    if 0>n:
      d +=1

print("{} valor(es) par(es)".format(a))
print("{} valor(es) impar(es)".format(b))
print("{} valor(es) positivo(s)".format(c))
print("{} valor(es) negativo(s)".format(d))