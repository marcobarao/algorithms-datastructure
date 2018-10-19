import string
letters = list(string.ascii_uppercase + '_.')

while True:
    try:
        n, s = input().split()
        s = list(s)
        n = int(n)
        for i in range(len(s)):
            index = letters.index(s[i])+n
            if index >= len(letters):
                index = index - len(letters)
            s[i] = letters[index]
        print(''.join(reversed(s)))
    except:
        break