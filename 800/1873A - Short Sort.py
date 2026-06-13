t = int(input())
for i in range(t):
    arr = list(map(str, input()))
    if arr[0] != 'a':
        a_place = arr.index('a')
        arr[0], arr[a_place] = arr[a_place], arr[0]
    elif arr[1] != 'b':
        b_place = arr.index('b')
        arr[1], arr[b_place] = arr[b_place], arr[1]
    if arr[:] == ["a", "b", "c"]:
        print ("YES")
    else:
        print("NO")
