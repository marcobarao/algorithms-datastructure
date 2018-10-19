def bon_appetit(bill, k, b):
    del(bill[k])
    charged = b - (sum(bill) // 2)
    return ('Bon Appetit' if charged == 0 else charged)

if __name__ == "__main__":
    n, k = map(int, input().split())
    bill = list(map(int, input().split()))
    b = int(input())

    result = bon_appetit(bill, k, b)

    print(result)
