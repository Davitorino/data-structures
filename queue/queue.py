from pessoa import Pessoa


class Queue:

    def __init__(self):
        self.__inicio: Pessoa = None
        self.__fim: Pessoa = None
        self.__contador = 0

    def enqueue(self, irmao):
        self.__contador += 1
        if not self.__inicio:
            self.__inicio = irmao
            self.__fim = irmao
            return
        self.__fim.defineIrmao(irmao)
        self.__fim = irmao

    def dequeue(self):
        if self.__contador == 0:
            raise Exception('Fila vazia')
        self.__contador -= 1
        irmao = self.__inicio
        self.__inicio = irmao.getIrmao()
        return irmao

    def print_items(self):
        if self.__contador == 0:
            raise Exception('Fila vazia')
        irmao = self.__inicio
        print(irmao.getNome())
        while irmao.getIrmao():
            irmao = irmao.getIrmao()
            print(irmao.getNome())
