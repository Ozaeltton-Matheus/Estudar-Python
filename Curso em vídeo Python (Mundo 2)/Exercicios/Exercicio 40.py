# Calculo de média do aluno

nota1 = float(input('Digite qual foi a sua primeira nota: '))
nota2 = float(input('Digite qual foi a sua segunda nota: '))
media = (nota1 + nota2)/2
situacao = ''
if media < 5:
    situacao = 'REPROVADO'

elif media <= 6.9:
    situacao = 'EM RECUPERAÇÃO'

else:
    situacao = 'APROVADO'

print(f'A sua média final é {media}\nVocê está {situacao}!')