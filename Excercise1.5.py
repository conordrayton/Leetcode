
k = 2
x = 2
while k < 21 :
    while x < k :
        if k % x == 0:
            print(k, 'is', x, '*', k / x, 'so it is not a prime number')
            k += 1
            x = 2
            break
        x += 1

    else:
        print(k, 'is a prime number')
        k += 1
        x = 2

