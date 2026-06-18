t = int(input())
for i in range(t):
    arr = list(map(int, input().split()))
    classes = list(map(int,input()))
    n, k = arr[0], arr[1]
    count = 0
    j = 0
    forced = 0
    while j < n:
        if classes[j] == 1:
            j += 1
            forced = k
        elif classes[j] == 0 and forced > 0:
            forced -= 1
            j+= 1
        elif classes[j] == 0 and forced == 0:
            count += 1
            j += 1
    print(count)

    