nome = input('Digite seu nome')
idade = int(input('Digite sua idade'))

if (nome == 'Izabel' and idade == 18) or nome == 'Izinha':
    print('Maravilhosa')
elif nome == 'Aquarela':
    print('Maravilhosa')
else: 
    print('Pessoa ridicula')

numero = 3

while numero < 5:
    print(numero)
    numero = numero + 1

lista = ['cubo magico','pagode japones', 'skate', 'manga com leite']

# for item in lista:
#     print(item)

for i in range(len(lista)):
    print(lista[i])