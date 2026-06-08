t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    
    m = a[n // 2]          # optimal meeting point = median
    l = sum(1 for x in a if x < m)
    r = sum(1 for x in a if x > m)
    print(max(l, r))