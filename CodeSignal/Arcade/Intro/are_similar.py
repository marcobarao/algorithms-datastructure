def areSimilar(a, b):
    if a == b:
        return True
    if sorted(a) != sorted(b):
        return False
    swap = 0
    for i in range(len(a)-1):
        if b[i] != a[i]:
            swap += 1
    
    return (True if swap <= 4 else False)

print(areSimilar(list(map(int, input().split())), list(map(int, input().split()))))