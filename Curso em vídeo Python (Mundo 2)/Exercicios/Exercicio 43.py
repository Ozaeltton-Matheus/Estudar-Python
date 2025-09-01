# Calcular o IMC

peso = float(input('Qual é o seu peso? em Quilogramas (Kg)'))
altura = float(input('Qual é a sua altura? em Metros (M)'))
imc = peso / altura**2
situacao = ''

if imc < 18.5:
    situacao = 'está ABAIXO DO PESO'

elif imc < 25:
    situacao = 'tem o PESO IDEAL'

elif imc <= 30:
    situacao = 'está com SOBREPESO'

elif imc <=40:
    situacao = 'está com OBESIDADE'

else:
    situacao = 'está com OBESIDADE MÓRBIDA'

print(f'O seu IMC é {imc:.3}!\nVocê {situacao}!')