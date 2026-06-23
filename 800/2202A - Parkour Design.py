t = int(input())
for i in range(t):
    coor = list(map(int, input().split()))
    if (coor[0] + coor[1]) % 3 == 0 and (-coor[0]/4) <= coor[1] <= (coor[0]/2):
        print("YES")
    else:
        print("NO")

