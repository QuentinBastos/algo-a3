def maxliste(liste):
    if len(liste) == 1:
        return liste[0]

    if len(liste) == 2:
        return liste[0] if liste[0] > liste[1] else liste[1]

    milieu = len(liste) // 2
    gauche = liste[:milieu]
    droite = liste[milieu:]

    max_gauche = maxliste(gauche)
    max_droite = maxliste(droite)

    return max_gauche if max_gauche > max_droite else max_droite

def main():
    liste = (input("Entrez une liste : ")).split()
    if len(liste) == 0:
        liste = [1, 2, 3, 4, 3, 4, 1]
    else:
        liste = [int(x) for x in liste]

    resultat = maxliste(liste)
    print("Le max est", resultat)



if __name__ == "__main__":
    main()