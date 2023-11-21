from src.item import Item
from src.moeda import Moeda

class Cofre:

    def __init__(self, volumeMaximo: int):
        self._volumemax = volumeMaximo
        self.volume = 0
        self.volumeRest = self._volumemax - self.volume
        self.quebrado = False
        self.itens = []
        self.moedas = []

    def getVolume(self):
        return self.volume

    def getVolumeMaximo(self):
        return self._volumemax

    def getVolumeRestante(self):
        return self.volumeRest

    def add(self, item: Item):
        if not self.quebrado and item.getVolume() <= self.volumeRest:
            self.volume += item.getVolume()
            self.volumeRest -= item.getVolume()
            self.itens.append(item)
            return True
        return False

    def addm(self, moeda: Moeda):
        if not self.quebrado and moeda.getVolume() <= self.volumeRest:
            self.volume += moeda.getVolume()
            self.volumeRest -= moeda.getVolume()
            self.moedas.append(moeda)
            return True
        return False

    def obterItens(self):
        if self.quebrado:
            if self.itens:
                DescricaoItens = ', '.join(item.getDesricao() for item in self.itens)
                self.itens = []
                self.volume = 0
                self.volumeRest = self._volumemax
                return DescricaoItens
            return 'vazio'
        return None


    def obterMoedas(self):
        if self.quebrado:
            if self.moedas:
                SomaMoedas = sum(moeda.value[0] for moeda in self.moedas)
                self.moedas = []
                self.volume = 0
                self.volumeRest = self._volumemax
                return SomaMoedas
            return 0
        return -1

    def taInteiro(self):
        return not self.quebrado

    def quebrar(self):
        if not self.quebrado:
            self.quebrado = True
            return True
        return False
