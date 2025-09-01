#Tabuada com for

numero = int(input('Digite um número para mostrar sua tabuada: '))
numero_para_operacao = int(input('Digite o número de valores da tabuada: ' ))


for c in range(numero, numero_para_operacao+1):
    for n in range(0, c+1):
        soma = n + numero_para_operacao
        print(f'|{n} + {numero_para_operacao} = {soma}   |')
    for n in range(0, c+1):
        multiplicacao = n * numero_para_operacao
        print(f'|{n} X {numero_para_operacao} = {multiplicacao}  |\t')

    for n in range(0, c+1):
        divisao = n / numero_para_operacao
        print(f'|{n} ÷ {numero_para_operacao} = {divisao}  |\t')

    for n in range(0, c+1):
        subtracao = n - numero_para_operacao
        print(f'|{n} - {numero_para_operacao} = {subtracao}    |\t')
print('===== FIM =====')
print(f'|{n} + {numero_para_operacao} = {soma}   |\t |{n} x {numero_para_operacao} = {multiplicacao} |')



