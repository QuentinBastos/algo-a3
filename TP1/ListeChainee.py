from Noeud import Noeud


class ListeChainee:
    def __init__(self):
        self.tete = None
        self.queue = None
        self.taille = 0


    def __repr__(self):
        morceaux = ""

        return "ListeChainee([{}])".format(morceaux)

    def afficher(self):
        print(self)