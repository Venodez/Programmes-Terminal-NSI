class Pile:

    def __init__(self, *elements):
        self.valeur= []
        for element in elements:
            self.valeur.append(element)

    def empiler(self, valeur):
        self.valeur.insert(0, valeur)

    def depiler(self):
        valeur = self.valeur[-1]
        self.valeur.pop()
        return valeur

    def pile_est_vide(self):
        if len(self) == 0:
            return True
        else:
            return False

    def __repr__(self):
        return f'{self.valeur}'

    def __len__(self):
        return len(self.valeur)

