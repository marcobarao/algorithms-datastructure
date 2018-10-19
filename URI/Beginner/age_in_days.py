n = int(input())

print("{} ano(s)".format(n // 365))
n = n % 365
print("{} mes(es)".format(n // 30))
n = n % 30
print("{} dia(s)".format(n))
