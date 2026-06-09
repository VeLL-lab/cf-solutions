
t = int(input())
for i in range(t):
    first = list(map(int, input().split()))
    second = list(map(int, input().split()))
    n = first[0]
    h = first[1]
    l = first[2]
    if h > l:
        h, l = l, h
    r = 0
    c = 0
    for j in range(n):
        if second[j] <= h:
            r += 1
        if second[j] <= l:
            c += 1
    print(min(r, c// 2))
