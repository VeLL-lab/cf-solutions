t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n-2, -1, -1):
        if arr[i+1] > 0:
            arr[i] += arr[i+1]
    print(sum(1 for x in arr if x > 0))