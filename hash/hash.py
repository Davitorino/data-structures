from linked_list.list import List


class Hash:

    def __init__(self, num_total: int, fator_carga: int):
        self.__tamanho = num_total // fator_carga
        self.__array = [List()] * self.__tamanho

    def incluir(self, valor: int):
        pos = valor % self.__tamanho
        self.__array[pos].insert_last(valor)

    def buscar(self, valor: int):
        pos = valor % self.__tamanho
        return self.__array[pos].get_by_value(valor)

    def excluir(self, valor: int):
        pos = valor % self.__tamanho
        self.__array[pos].remove_by_value(valor)
