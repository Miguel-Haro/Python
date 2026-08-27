import random

letra_maiuscula = chr(random.randint(65, 90))
letra_minuscula = chr(random.randint(97, 122))
lista_numeros = []

for i in range(7):
    numeros = random.randrange(9)
    lista_numeros.append(numeros)

random.shuffle(lista_numeros)
lista_numeros = str(lista_numeros) [1:-1]
lista_numeros = lista_numeros.replace(',', '')
print(letra_maiuscula, letra_maiuscula, lista_numeros)