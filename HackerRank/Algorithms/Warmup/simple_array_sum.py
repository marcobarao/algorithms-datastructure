def simple_array_sum(arr):
    return sum(arr)

def main():
    _ = input()
    arr = list(map(int, input().split()))
    
    result = simple_array_sum(arr)
    
    print(result)

if __name__ == '__main__':
    main()