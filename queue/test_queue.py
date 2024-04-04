from pessoa import Pessoa
from queue import Queue


p1 = Pessoa('Davi')
p2 = Pessoa('Rafael')
p3 = Pessoa('Joca')
p4 = Pessoa('Maria')

fila = Queue()
fila.enqueue(p1)
fila.enqueue(p2)
fila.enqueue(p4)
fila.enqueue(p3)

fila.print_items()
