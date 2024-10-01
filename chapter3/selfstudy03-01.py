i, k = 0, 0

for i in range(0, 9):
    if i < 5:
        for k in range(0, i):
            print(' ', end='')
        for k in range(0, 9 - (2 * i)):
            print("*", end='')
    else:
        for k in range(0, 8 - i):
            print(' ', end='')
        for k in range(0, 3 + 2 * (i - 5)):
            print("*", end='')

    print("")