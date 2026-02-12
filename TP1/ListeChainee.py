from Noeud import Noeud


class ListeChainee:
    def __init__(self, liste):
        self.liste = liste
        self.tete = None
        self.queue = None
        self._taille = 0
        for valeur in self.liste:
            self.ajouter(valeur)

    def __repr__(self):
        valeurs = []
        courant = self.tete
        while courant is not None:
            valeurs.append(str(courant.valeur))
            courant = courant.suivant
        return " -> ".join(valeurs) if valeurs else "(vide)"

    def afficher(self):
        print(self)

    def ajouter(self, valeur):
        nouveau = Noeud(valeur)
        if self.estVide():
            self.tete = nouveau
            self.queue = nouveau
        else:
            self.queue.suivant = nouveau
            self.queue = nouveau
        self._taille += 1

    def inserer(self, valeur, position):
        if position < 1 or position > self._taille + 1:
            raise IndexError("Position invalide")
        if position == 1:
            self.tete = Noeud(valeur, self.tete)
            if self.queue is None:
                self.queue = self.tete
        elif position == self._taille + 1:
            self.queue.suivant = Noeud(valeur)
            self.queue = self.queue.suivant
        else:
            precedent = self.obtenir(position - 1)
            precedent.suivant = Noeud(valeur, precedent.suivant)
        self._taille += 1

    def supprimer(self, position):
        if position < 1 or position > self._taille:
            raise IndexError("Position invalide")
        if position == 1:
            self.tete = self.tete.suivant
            if self.tete is None:
                self.queue = None
        else:
            precedent = self.obtenir(position - 1)
            cible = precedent.suivant
            precedent.suivant = cible.suivant
            if position == self._taille:
                self.queue = precedent
        self._taille -= 1

    def rechercher(self, valeur):
        courant = self.tete
        while courant is not None:
            if courant.valeur == valeur:
                return True
            courant = courant.suivant
        return False

    def obtenir(self, position):
        """Renvoie le noeud a la position (1-based)."""
        if position < 1 or position > self._taille:
            raise IndexError("Position invalide")
        courant = self.tete
        for _ in range(1, position):
            if courant is None:
                raise IndexError("Position invalide")
            courant = courant.suivant
        return courant

    def taille(self):
        return self._taille

    def estVide(self):
        return self._taille == 0
