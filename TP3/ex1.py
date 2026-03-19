def recursion_croissant(n, limite = 100):
    if n > limite:
        return None
    print(n)
    return recursion_croissant(n+1, limite)

def recursion_decroissant(n):
    print(n)
    if n == 0:
        return None
    return recursion_decroissant(n-1)

def main():
    i = int(input("Entrez un nombre : "))
    n = 0
    print('croissant')
    recursion_croissant(n, i)
    print('decroissant')
    n = i
    recursion_decroissant(n)


if __name__ == "__main__":
    main()