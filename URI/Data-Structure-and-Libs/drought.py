def trunc(num, digits):
   sp = str(num).split('.')
   return '.'.join([sp[0], sp[1][:digits]])

n = float('inf')
aux = 0
while True:
    n = int(input())
    if n == 0:
        break
    
    consumption_city = 0
    count_hab = 0
    consumption_hab = dict() 
    for _ in range(n):
        x, y = map(int, input().split())
        consumption_city += y
        count_hab += x
        a = y // x
        consumption_hab.setdefault(a, 0)
        consumption_hab[a] += x

    consumption_hab = sorted(consumption_hab.items(), key=lambda x:  x[0])

    for i in range(len(consumption_hab)):
        a = consumption_hab[i]
        consumption_hab[i] = "{}-{}".format(a[1], a[0])

    aux += 1
    print("Cidade# {}:".format(aux))
    print(*consumption_hab, sep=" ")
    print("Consumo medio: {} m3".format(trunc(consumption_city / count_hab, 2)))
