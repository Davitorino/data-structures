from list_item import ListItem
import math


class List:

    def __init__(self, limite: int = math.inf):
        self.__prim: ListItem | None = None
        self.__ult: ListItem | None = None
        self.__cursor: ListItem | None = None
        self.__qtd = 0
        self.__limite = limite

    def acessar_atual(self):
        return self.__cursor.value

    def inserir_antes_atual(self, valor):
        self.__verificar_lista_vazia()
        self.__verificar_lista_cheia()
        item = ListItem(valor)
        anterior = self.__cursor.prev
        self.__cursor.prev = item
        item.next = self.__cursor
        if anterior is not None:
            anterior.next = item
            item.prev = anterior
        else:
            self.__prim = item
        self.__qtd += 1

    def inserir_apos_atual(self, valor):
        self.__verificar_lista_vazia()
        self.__verificar_lista_cheia()
        item = ListItem(valor)
        posterior = self.__cursor.next
        self.__cursor.next = item
        item.prev = self.__cursor
        if posterior is not None:
            posterior.prev = item
            item.next = posterior
        else:
            self.__ult = item
        self.__qtd += 1

    def inserir_como_ultimo(self, valor):
        item = ListItem(valor)
        if self.__ult is not None:
            self.__ult.next = item
            item.prev = self.__ult
        else:
            self.__prim = item
            self.__cursor = item
        self.__ult = item
        self.__qtd += 1

    def inserir_como_primeiro(self, valor):
        item = ListItem(valor)
        if self.__prim is not None:
            self.__prim.prev = item
            item.next = self.__prim
        else:
            self.__ult = item
            self.__cursor = item
        self.__prim = item
        self.__qtd += 1

    def inserir_na_posicao(self, k: int, valor):
        self.__ir_para_primeiro()
        self.__avancar_k_posicoes(k - 1)
        self.inserir_antes_atual(valor)

    def excluir_atual(self):
        self.__verificar_lista_vazia()
        anterior = self.__cursor.prev
        posterior = self.__cursor.next
        if anterior is not None:
            anterior.next = posterior
        else:
            self.__prim = posterior
        if posterior is not None:
            posterior.prev = anterior
        else:
            self.__ult = anterior
        self.__cursor = self.__prim
        self.__qtd -= 1

    def excluir_primeiro(self):
        self.__verificar_lista_vazia()
        self.__prim = self.__prim.next
        self.__prim.prev = None
        self.__qtd -= 1

    def excluir_ultimo(self):
        self.__verificar_lista_vazia()
        self.__ult = self.__ult.prev
        self.__ult.next = None
        self.__qtd -= 1

    def excluir_elem(self, valor):
        if self.buscar(valor):
            self.excluir_atual()

    def excluir_da_posicao(self, k: int):
        self.__ir_para_primeiro()
        self.__avancar_k_posicoes(k - 1)
        self.excluir_atual()

    def buscar(self, valor) -> bool:
        self.__ir_para_primeiro()
        while True:
            if self.__cursor.value == valor:
                return True
            if self.__cursor.next is None:
                return False
            self.__cursor = self.__cursor.next

    def vazia(self) -> bool:
        return self.__qtd == 0

    def cheia(self) -> bool:
        return self.__qtd == self.__limite

    def tamanho(self) -> int:
        return self.__qtd

    def posicao_de(self, valor) -> int:
        self.__verificar_lista_vazia()
        atual = self.__prim
        for pos in range(self.__qtd):
            if atual.value == valor:
                return pos + 1
            atual = atual.next
        return -1

    def __avancar_k_posicoes(self, k: int):
        self.__verificar_lista_vazia()
        self.__verificar_posicao(k)
        for i in range(k):
            if self.__cursor.next is None:
                return
            self.__cursor = self.__cursor.next

    def __retroceder_k_posicoes(self, k: int):
        self.__verificar_lista_vazia()
        self.__verificar_posicao(k)
        for i in range(k):
            if self.__cursor.prev is None:
                return
            self.__cursor = self.__cursor.prev

    def __ir_para_primeiro(self):
        self.__verificar_lista_vazia()
        self.__cursor = self.__prim

    def __ir_para_ultimo(self):
        self.__verificar_lista_vazia()
        self.__cursor = self.__ult

    def __verificar_lista_vazia(self):
        if self.vazia():
            raise Exception('Lista vazia')

    def __verificar_lista_cheia(self):
        if self.cheia():
            raise Exception('Lista cheia')

    def __verificar_posicao(self, k: int):
        if k < 0 or k > self.__qtd:
            raise Exception('Posição inválida/fora dos limites')
