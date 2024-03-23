

class Stack:

    def __init__(self, tamanho):
        self.__tamanho = tamanho
        self.__stack = []
        self.__indice_atual = -1

    def push(self, valor):
        if self.is_cheia():
            raise Exception('Pilha cheia!')
        self.__indice_atual += 1
        self.__stack.append(valor)

    def pop(self):
        self.__validar_stack_vazia()
        self.__indice_atual -= 1
        return self.__stack.pop()

    def top(self):
        self.__validar_stack_vazia()
        return self.__stack[self.__indice_atual]

    def is_vazia(self):
        return not len(self.__stack)

    def is_cheia(self):
        return len(self.__stack) >= self.__tamanho

    def num_items(self):
        return len(self.__stack)

    def esvaziar(self):
        self.__stack = []
        self.__indice_atual = -1

    def __validar_stack_vazia(self):
        if self.is_vazia():
            raise Exception('Pilha vazia!')
