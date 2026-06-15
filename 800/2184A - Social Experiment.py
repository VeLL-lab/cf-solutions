t = int(input())
for i in range(t):
    n = int(input())
    if n == 2:
        print(2)
    elif n % 2 == 1 and n > 2:
        print(1)
    else:
        print(0)