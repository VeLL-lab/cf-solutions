from math import ceil
t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    max_val = max(arr)
    min_val = min(arr)
    mid = ceil((max_val+min_val) // 2)
    answer = max((max_val - mid), (mid - min_val))
    print(answer)
            