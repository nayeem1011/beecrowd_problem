N = int(input())

years = N // 365
mounths = (N % 365) // 30
day = (N % 365) % 30
print("{:d} ano(s)".format(years))
print("{:d} mes(es)".format(mounths))
print("{:d} dia(s)".format(day))