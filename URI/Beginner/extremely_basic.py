def extremely_basic(a, b):
    return a + b

def main():
    a = int(input())
    b = int(input())
    
    result = extremely_basic(a, b)

    print('X = {}'.format(result))

if __name__ == '__main__':
    main()