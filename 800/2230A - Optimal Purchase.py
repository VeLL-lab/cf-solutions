t = int(input())
for i in range(t):
    arr = list(map(int, input().split()))
    n, a, b = arr[0], arr[1], arr[2]
    count = 0
    amount = 0
    while count != n:
        if (n*a) > (b):
            count += 3 
            amount += b
        