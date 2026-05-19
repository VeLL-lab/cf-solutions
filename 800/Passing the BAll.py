
t = int(input())
for i in range(1, t+1):
    n = int(input())
    s = input()
    for j in range(0, n):
        if s[j] == 'L':
            print(j+1) 
            break