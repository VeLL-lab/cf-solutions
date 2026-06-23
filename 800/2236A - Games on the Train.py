t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    answer = (max(arr) + 1) - min(arr)
    print(answer) 