from ListeChainee import ListeChainee


def main():
    liste = ListeChainee([])
    liste.ajouter(4)
    liste.inserer(2, 1)
    liste.inserer(6, 3)
    liste.inserer(2, 3)
    liste.inserer(3, 3)
    liste.supprimer(2)
    if liste.rechercher(6): print("6 a été trouvé dans la liste")
    liste.obtenir(2)
    liste.afficher()


if __name__ == "__main__":
    main()
