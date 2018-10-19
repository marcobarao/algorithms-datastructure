n = float(input())
print(n)

notas = [100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.1, 0.05, 0.01]
type = 'nota'

for nota in notas:
    if nota == 100:
        print("NOTAS:")
    elif nota == 1:
        print("MOEDAS:")
        type = 'moeda'
    cedulas = int(n // nota)
    n = n % nota
    print("{0} {2}(s) de R$ {1:.2f}".format(cedulas, nota, type))
