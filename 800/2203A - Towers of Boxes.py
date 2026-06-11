from math import ceil
t = int(input())
for i in range(t):
    arr = list(map(int, input().split()))
    n = arr[0]
    m = arr[1]
    d = arr[2]
    count = 0 
    max_height = (d//m) + 1
    towers = (n + max_height - 1) // max_height

    print(towers)
