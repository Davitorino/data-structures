

class SuperArray:

    def __init__(self, inicio, fim):
        inicio, fim = (fim, inicio) if inicio > fim else (inicio, fim)
        tamanho = fim - inicio + 1
        self.__lista = [None] * tamanho
        self.__inicio = inicio
        self.__fim = fim

    def obter(self, indice):
        self.__verificar_indice(indice)
        return self.__lista[indice - self.__inicio]

    def adicionar(self, indice, valor):
        self.__verificar_indice(indice)
        self.__lista[indice - self.__inicio] = valor

    def __verificar_indice(self, indice):
        if indice < self.__inicio or indice > self.__fim:
            raise Exception('SuperArray out of bounds')
