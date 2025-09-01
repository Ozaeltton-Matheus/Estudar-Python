idade = int(input('Digite a sua idade: '))
categoria = ''
if idade <= 9:
    categoria = 'MIRIM'

elif idade <= 14:
    categoria = 'INFANTIL'

elif idade <= 19:
    categoria = 'JUNIOR'

elif idade <= 20:
    categoria = 'SÊNIOR'

else:
    categoria = 'MESTRE'
print(f'Você está na categoria {categoria}')