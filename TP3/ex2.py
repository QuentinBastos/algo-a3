import time
def fibonacci1(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci1(n-1) + fibonacci1(n-2)

### O(n) au lieu de O(2^n) pour la version sans mémoïsation
def fibonacci2(n, memo):
    if memo[n] is None:
        if n == 1 or n == 2:
            memo[n] = 1
        else:
            memo[n] = fibonacci2(n-1, memo) + fibonacci2(n-2, memo)
    return memo[n]

### O(n) au lieu de O(2^n) pour la version sans mémoïsation
def fibonacci3(n, a=1, b=1):
    if n == 1 or n == 2:
        return 1
    if n == 3:
        return a + b
    return fibonacci3(n - 1, b, a + b)

def main():
    i = int(input("Entrez un nombre : "))

    t = time.time()
    fibonacci3(i)
    print(time.time() - t)

    t = time.time()
    memo = [None] * (i + 1)
    fibonacci2(i, memo)
    print(time.time() - t)

    t = time.time()
    fibonacci1(i)
    print(time.time() - t)




if __name__ == "__main__":
    main()