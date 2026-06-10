t = int(input())
for i in range(t):
    n = list(map(int, input().split()))
    if n[0] % 2 == 1 and n[1] % 2 == 1:
        print("NO")
    else:
        print("YES")