result = 0

for _ in range(2):
    _id, qt, price = map(float, input().split())
    result += price * qt


print("VALOR A PAGAR: R$ {:.2f}".format(result))