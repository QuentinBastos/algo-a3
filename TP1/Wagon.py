class Wagon:
    def __init__(self):
        self.numero_wagon = None;
        self.taille_maximum = 4
        self.taille_actuelle = 0
        "Un wagon peut avoir maxium 4 passager"
        pass

    def creer_wagon(self, nombre_passager, numero_wagon):
        """Creer un wagon avec nombre_passager passager"""
        self.taille_actuelle = nombre_passager
        self.numero_wagon = numero_wagon

    def afficher_passagers(self):
        print(f"Taille du wagon numéro {self.numero_wagon} :{self.taille_actuelle}")

    def ajouter_un_passager(self):
        self.taille_actuelle += 1

    def descendre_un_passager(self):
        self.taille_actuelle -= 1