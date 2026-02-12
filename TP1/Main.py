from ListeChainee import ListeChainee
from TP1.Train import Train


def main():
    """ Partie Liste"""
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


    """Partie Train"""
    train = Train()
    Train.creer_train(train, 4)
    for _ in range(1, 16):
        train.monter(2)
    train.descendre(3)
    train.descendre(4)
    train.descendre(4)
    train.afficher_passagers()



if __name__ == "__main__":
    main()
