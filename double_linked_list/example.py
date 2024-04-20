from list import List

lista_compras = List(20)
lista_compras.inserir_como_ultimo('cenoura')
lista_compras.inserir_como_ultimo('maçã')
lista_compras.inserir_como_primeiro('pão')
lista_compras.inserir_na_posicao(4, 'beterraba')

lista_compras.buscar('beterraba')
lista_compras.inserir_antes_atual('alface')

print('Elemento atual:', lista_compras.acessar_atual())
print('Posição da maçã:', lista_compras.posicao_de('maçã'))
print('Quantidade de elementos:', lista_compras.tamanho())

lista_compras.buscar('cenoura')
lista_compras.excluir_atual()

print('Posição da cenoura:', lista_compras.posicao_de('cenoura'))
print('Quantidade de elementos:', lista_compras.tamanho())
print('Lista está vazia?', lista_compras.vazia())
print('Lista está cheia?', lista_compras.cheia())
