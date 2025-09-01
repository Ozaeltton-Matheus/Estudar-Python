# CONVERSÃO DE BASES NÚMERICAS

numero_para_converter = int(input('Digite um número: '))

convertido_para_binario = bin(numero_para_converter)
convertido_para_octal = oct(numero_para_converter)
convertido_para_exadecimal = hex(numero_para_converter)




opcao = int(input('Escolha uma opção:\nDIGITE\n(1) PARA CONVERTER PARA A BASE BINÁRIA\n(2) PARA CONVERTER PARA A BASE OCTAL\n(3) PARA CONVERTER PARA A BASE EXADECIMAL'))

if opcao == 1:
    print(f'{numero_para_converter} convertido para a base binária é {convertido_para_binario}')

elif opcao == 2:
    print(f'{numero_para_converter} convertido para a base octal é {convertido_para_octal}')

elif opcao == 3:
    print(f' {numero_para_converter} convertido para a base exadecimal é {convertido_para_exadecimal}')

else:
    print('Valor digitado inválido!\nPor favor digite um valor válido!')






 

