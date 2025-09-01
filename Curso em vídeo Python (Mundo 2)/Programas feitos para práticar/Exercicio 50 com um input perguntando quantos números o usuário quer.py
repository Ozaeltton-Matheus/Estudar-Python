# Somar somente os números que forem pares

# Com um input perguntando quantos números o usuário quer

soma = 0
numero = int(input('Digite quantos números você quer :'))
for c in range(0, numero):
    numero = int(input('Digite um número: '))
    if numero %2 ==0:
        soma = soma + numero
print(f'A soma de todos os números pares é {soma}')

# Deu certo, internacional!
# Já pode ir para massaxuche