nome = input('Qual é o seu nome? :')
if nome == 'Matheus':
    print('Que nome bonito!')
elif nome == 'Paulo' or nome == 'Pedro' or nome == 'Maria':
    print('Seu nome é bem popular no Brasil!')
elif nome in 'Cláudia Jessica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal!')
print(f'Tenha um bom dia, {nome}!')