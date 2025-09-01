# INFORMAR SE O USÚARIO DEVE SE ALISTAR

idade_do_usuario = int(input('Digite sua idade: '))

if idade_do_usuario < 18:
    print(f'Você ainda vai se alistar!\nFaltam {18-idade_do_usuario} anos para você se alistar!')

elif idade_do_usuario > 18:
    print(f'Já passou do tempo de você se alistar!\nVocê já deveria ter se alistado há {idade_do_usuario - 18} anos!') 

else:
    print(f'Já é hora de se alistar!')