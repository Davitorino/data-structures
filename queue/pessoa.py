

class Pessoa:

    def __init__(self, nome):
        self.__nome = nome
        self.__irmao = None

    def getNome(self):
        return self.__nome

    def defineIrmao(self, irmao):
        self.__irmao = irmao

    def getIrmao(self):
        return self.__irmao
