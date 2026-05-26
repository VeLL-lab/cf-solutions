def sum_of_digits(num):
    s = 0
    while num > 0:
        s += num % 10
        num //= 10
    return s
    

t = int(input())
for i in range(t):
    n = int(input())
    count = 0 
    for y in range(n+1, n+200):
        if y - sum_of_digits(y) == n:
            count += 1
    print(count)
