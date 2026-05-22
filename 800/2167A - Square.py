t = int(input())
for i in range(t):
    arr = list(map(int, input().split()))
    if arr[0] == arr[1] == arr[2] == arr[3]:
        print("YES")
    else:
        print("NO")
