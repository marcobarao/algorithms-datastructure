from itertools import product

def get_money_spent(keyboards, drives, b):
    _max = -1
    for tup in product(keyboards, drives):
            if  sum(tup) > _max and sum(tup) <= b:
                _max = sum(tup)
    
    return _max

if __name__ == "__main__":
    b = int(input().split()[0])
    keyboards = list(map(int, input().split()))
    drives = list(map(int, input().split()))

    result = get_money_spent(keyboards, drives, b)

    print(result)