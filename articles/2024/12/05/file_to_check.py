def cool(n):
    for i in range(n):
        print(i * '*')
    for i in range(n, 0, -1):
        print(i * '*')

    from json import load