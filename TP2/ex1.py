# Programme 1
def programme1(n):
    test = 0
    for i in range(n):
        test = test + 1

    for j in range(n):
        test = test - 1


# Programme 2
def programme2(n):
    test = 0
    for i in range(n):
        for j in range(n):
            test = test + i * j


# Programme 3
def programme3(n):
    a = 5
    b = 6
    c = 10
    for i in range(n):
        for j in range(n):
            x = i * i
            y = j * j
            z = i * j
            for k in range(n):
                w = a * k + 45
                v = b * b
                d = 33


# Programme 4
def programme4(n):
    i = n
    while i > 0:
        k = 2 + 2
        i = i // 2


# Programme 5
def programme5(n):
    sum_val = 0
    for i in range(1, n * n + 1):
        for j in range(1, i + 1):
            for k in range(1, 7):
                sum_val = sum_val + 1

