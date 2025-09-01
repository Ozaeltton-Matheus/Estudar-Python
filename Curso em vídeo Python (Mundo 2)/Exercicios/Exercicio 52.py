# Números primos

numero = int(input('Digite um número: '))

for i in range(numero):
    resultado = ''
    if numero % numero == 0:
        resultado = 'não é primo'

    else:
        resultado = 'é primo'


print(f'O número {numero} {resultado}')



