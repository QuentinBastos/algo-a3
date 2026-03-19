def hanoi(n, A, B, C, nom_A="A", nom_B="B", nom_C="C"):
    if n == 1:
        disque = A.pop()
        C.append(disque)
        print(f"Déplacer disque {disque} de {nom_A} vers {nom_C}")
    else:
        hanoi(n-1, A, C, B, nom_A, nom_C, nom_B)
        disque = A.pop()
        C.append(disque)
        print(f"Déplacer disque {disque} de {nom_A} vers {nom_C}")
        hanoi(n-1, B, A, C, nom_B, nom_A, nom_C)


def main():
    hanoi(6, [1, 2, 3, 4, 5, 6], [], [])

if __name__ == "__main__":
    main()