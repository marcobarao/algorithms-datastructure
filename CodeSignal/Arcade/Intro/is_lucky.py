def isLucky(n):
    n_str = str(n)
    size = len(n_str) // 2
    first_half = sum(map(int, n_str[:size]))
    second_half = sum(map(int, n_str[size:]))
    
    print(first_half, second_half)
    
    return first_half == second_half
