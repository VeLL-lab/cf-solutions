t = int(input())
for i in range(t):
    arr = list(map(int,input().split()))
    monsters = list(map(int, input().split()))
    n,c,k = arr[0], arr[1], arr[2]
    monsters.sort()
    for m in monsters:
        if m <= c:
            boost = min(k, c - m)
            c += m + boost
            k -= boost
    print(c)