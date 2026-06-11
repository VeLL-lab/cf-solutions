t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    pos = {v: i for i, v in enumerate(arr)}
    cur = 0
    for v in range(n, 0, -1):
        i = pos[v]
        if i != cur:        
            arr[cur:i+1] = arr[cur:i+1][::-1]
            break
        cur += 1
    print(*arr)