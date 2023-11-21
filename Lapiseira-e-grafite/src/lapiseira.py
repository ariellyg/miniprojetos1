from src.grafite import Grafite


class Lapiseira:

    def __init__(self, calibre:float):
        self.calibre = calibre
        self.grafite = None
        self.FolhasEscritas = 0

    def inserir (self, grafite: Grafite):
        if self.grafite is None and grafite.getCalibre() == self.calibre:
            self.grafite = grafite
            self.FolhasEscritas = 0
            return True
        else:
            return False

    def remover(self):
        if self.grafite is not None:
            self.grafite = None
            return True
        else:
            return False

    def escrever(self, folhas: int):
        for f in range(folhas):
            if self.grafite is not None:
                self.FolhasEscritas += 1
                desgaste = self.grafite.desgastePorFolha()
                if self.grafite.getTamanho() >= desgaste:
                    self.grafite.setTamanho(self.grafite.getTamanho() - desgaste)
                    if self.grafite.getTamanho() <= 0:
                        self.grafite = None
                        print("Grafite acabou!")
                else:
                    print("Grafite insuficiente para escrever esta folha.")
                    return False
            else:
                print("Não há grafite para escrever.")
                return False
        return True

    def getGrafite(self):
        return self.grafite

    def getCalibre(self):
        return self.calibre

    def getFolhasEscritas(self):
        return self.FolhasEscritas