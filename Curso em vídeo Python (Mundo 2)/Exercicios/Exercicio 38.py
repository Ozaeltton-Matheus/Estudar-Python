# Comparar entre dois números se um é maior doque o ouro ou os dois são iguais.

numero1 = int(input('Digite um 1º número: '))
numero2 = int(input('Digite um 2º número: '))

if numero1 > numero2:
    print(f'{numero1} é maior do que {numero2}')

elif numero2 > numero1:
    print(f'{numero2} é maior do que {numero1}')

else:
    print(f'Não há número maior, os números informados são iguais!')

