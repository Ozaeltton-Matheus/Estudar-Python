# Calcular a soma entre todos os números impares multiplos de três e que se encontram no intercalo de 1 até 500

soma = 0

for c in range(1, 501, 3):
    numero = c
    if c % 3:
        print(numero)
        soma += numero
print(f'A soma de todos os números foi igual a {soma}')

# Acho que algo está errado mas, tudo bem

