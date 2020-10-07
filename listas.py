"""
Função
# Contar quantas vezes aparece o elemento na lista
lista.count(4) -> Mostra quantas vezes aparece o número 4 na lista

# Adicionar elemento
lista.append(42) -> Adiciona ao final da lista o número 42 *adiciona um elemento por vez*
lista.append([4, 6, 8]) -> Adiciona uma lista dentro de uma lista como elemento único.
lista.extend([7, 8, 9]) -> adiciona os elementos dessa lista indidualmente.
lista.extend('Nome')-> adiciona cada letra separadamente
lista.extend(['Nome'])-> adiciona a string por inteiro
lista.insert(P, V) -> adiciona na posição P o valor V

# Remover elementos
lista.pop()  -> remove o último elemento de uma lista (também retorna o elemento removido)
lista.pop(P) -> 'P' indica a posição aser removida
lista.clear() -> Apaga a lista toda


# Odenando uma lista
lista.sort() -> ordena uma lista em ordem alfabetica
lista.reverse()  -> ordena em ordem reversa.
print(lista[::-1])

# Copiando uma lista
lista1 = lista.copy()

# Contando os elementos de uma lista
print(len(lista))

# Converter uma string em uma lista
lista = string.split()

# Convertendo uma lista em string
string = ' '.join(lista)
curso = '_'.join(lista)
print(curso)

# Enumerando itens
cores = ['verde', 'amarelo', 'azul', 'branco']
cores = list(enumerate(cores))
print(cores)

[(0, 'verde'), (1, 'amarelo'), (2, 'azul'), (3, 'branco')]

# Encontrar o índice de um elemento na lista
print(cores.index('azul')) -> mostra o número 2 (número do primeiro valor encontrado)
print(cores.index('azul', 1)) -> procura a partir do índice 1 (pulando o índice 0)
print(cores.index('azul', 1, 6)) -> procura a partir do índice 1 até o índice 6

## Revisão do Slicing
lista[ínicio:fim:passo]
range[ínicio:fim:passo]

# Soma
print(sum(lista))

# Máximo valor
print(max(lista))

# Mínimo valor
print(min(lista))

# Tamanho da lista
print(len(lista))

# Transformar uma lista em Tupla
tupla = tuple(lista)

# Desempacotamento de lista
lista = [1, 2, 3]
num1, num2, num3 = lista

# Copiando uma lista para outra ( Shallow Copy e Deep Copy)
utilizando a -- nova = lista.copy() -- cria uma lista totalmente independente -> Isso é (deep copy)

utilizando a -- nova = lista  --  As duas listas ficam ligadas, o que for alterado em uma a outra tbm será
isso é ( Shallow Copy )



"""
lista = [1, 2, 3]
print(lista)

nova = lista.copy()
print(nova)
nova.append(4)
print(lista)
print(nova)

