class Item:


    def __init__(self, descricao: str, volume: int):
        self._volume = volume
        self._descricao = descricao

    def getDesricao(self):
        return self._descricao

    def getVolume(self):
        return self._volume
