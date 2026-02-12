from TP1.Wagon import Wagon


class Train:
    def __init__(self):
        "Un train contient des wagons (n wagons) et les wagons contiennent 4 passagers maximum"
        self.train = []
        pass

    def creer_train(self, nombre_wagon):
        """Creer un train avec nombre_wagon wagons"""
        """Utiliser la fonction creer_wagon de la classe Wagon"""
        if nombre_wagon < 0:
            raise ValueError("nombre_wagon doit etre >= 0")
        self.train = []
        for i in range(nombre_wagon):
            wagon = Wagon()
            wagon.creer_wagon(0, i+1)
            self.train.append(wagon)

    def monter(self, position):
        # positions are 1-based from the outside
        self.chercher_une_place_apres_la_position(position)

    def descendre(self, position):
        index = position - 1
        if index < 0 or index >= self.taille_train():
            raise IndexError("Position invalide")
        self.train[index].descendre_un_passager()

    def chercher_une_place_apres_la_position(self, position):
        """Chercher une place dans le train dans tous les wagons derrieres position"""
        index = position - 1
        if index < 0:
            index = 0
        while index < self.taille_train():
            wagon = self.train[index]
            if wagon.taille_actuelle < wagon.taille_maximum:
                wagon.ajouter_un_passager()
                return index + 1
            index += 1
        self.cherche_une_place_avant_la_position(position)
        return None

    def cherche_une_place_avant_la_position(self, position):
        """Cherche une place avant la position dans les wagons"""
        index = position
        if index < 0:
            index = 0
        while index >= 0:
            wagon = self.train[index]
            if wagon.taille_actuelle < wagon.taille_maximum:
                wagon.ajouter_un_passager()
                return index + 1
            index -= 1
        print("Le train est plein, il n'y a pas de place pour monter")
        return None

    def afficher_passagers(self):
        for wagon in self.train:
            wagon.afficher_passagers()

    def taille_train(self):
        return len(self.train)
