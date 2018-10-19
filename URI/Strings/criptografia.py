n = int(input())

for _ in range(n):
    m = input()
    step1 = ''
    for i in range(len(m)):
        if m[i].isalpha():
            step1 += chr(ord(m[i]) + 3)
        else:
            step1 += m[i]

    step2 = step1[::-1]

    step3 = step2[:len(step2) // 2]

    for i in range(len(step2) // 2, len(step2)):
        step3 += chr(ord(step2[i]) - 1)

    print(step3)