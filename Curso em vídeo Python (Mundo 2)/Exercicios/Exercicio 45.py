# Jokenpô
import random
escolha_do_usuario = input('Escolha Pedra, papel, ou tesoura') 
lista = ['Pedra', 'Papel', 'Tesoura']
escolha_do_computador = random.choice(lista)

if escolha_do_usuario == 'Pedra' and escolha_do_computador == 'tesoura':
    print('Você venceu!\nPedra quebra tesoura!')

elif escolha_do_usuario == 'Papel' and escolha_do_computador == 'Pedra':
    print('Você venceu!\nPapel embrulha pedra!')

elif escolha_do_usuario == 'Tesoura' and escolha_do_computador == 'Papel':
    print('Você venceu!\nTesoura corta papel!')

elif escolha_do_usuario == 'Tesoura' and escolha_do_computador == 'Pedra':
    print('Você perdeu!\nPedra quebra tesoura!')

elif escolha_do_usuario == 'Pedra' and escolha_do_computador == 'Papel':
    print('Você perdeu!\nPapel embrulha pedra!')

elif escolha_do_usuario == 'Papel' and escolha_do_computador == 'Tesoura':
    print('Você perdeu!\nTesoura corta papel!')
else:
    print(f'{escolha_do_usuario} e {escolha_do_computador}Empatou!\nTente denovo!')

print(f'Eu escolhi {escolha_do_computador}')


