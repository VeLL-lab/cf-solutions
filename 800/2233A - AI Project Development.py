t = int(input())
for i in range(t):
    arr = list(map(int, input().split()))
    n,x,y,z = arr[0], arr[1], arr[2], arr[3]
    hour = 0
    count = 0
    while n > count:

        if count + x + y >= n:
            hour += 1
            break
        elif count + x + y < n:
            count += x + y 
            hour += 1
        
    count2 = z * x
    hour2 = z
    if n > count2:
        while n > count2:
            count2 += x + (y * 10)
            hour2 += 1
    
    print(min(hour,hour2))