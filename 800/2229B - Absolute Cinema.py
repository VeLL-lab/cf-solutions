def solve():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    total = sum(max(a[i], b[i]) for i in range(n))
    ans = 0
    for i in range(n):
        ans = max(ans, total + min(a[i], b[i]))
    print(ans)



t = int(input())
for i in range(t):
    solve()