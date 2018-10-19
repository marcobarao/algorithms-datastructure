n = int(input())
print(n)

notas = [100, 50, 20, 10, 5, 2, 1]

for nota in notas:
    cedulas = n // nota
    n = n % nota
    print("{0} nota(s) de R$ {1},00".format(cedulas, nota))
