# Refazer o exercicio 35 que diz se as retas podem formar um triângulo, só que agora mostrando o tipo do triângulo formado.

reta1 = float(input('Digite o cumprimento da primeira reta: '))
reta2 = float(input('Digite o cumprimento da segunda reta: '))
reta3 = float(input('Digite o cumprimento da terceira reta: '))
situacao = ''
if reta1 == reta2 and reta2 == reta3 and reta3 == reta1:
    situacao = 'ESTAS RETAS FORMAM UM TRIÂNGULO EQUILÁTERO'

elif reta1 == reta2 and reta2 != reta3 or reta2 == reta3 and reta3 != reta1 or reta3 == reta1 and reta1 != reta2:
    situacao = 'ESTAS RETAS FORMAM UM TRIÂNGULO ISÓSCELES'

elif reta1 != reta2 and reta2 != reta3 and reta3 != reta1:
    situacao = 'ESTAS RETAS FORMAM UM TRIÂNGULO ESCALENO'

else:
    situacao = 'ESTAS RETAS NÃO PODEM FORMAR UM TRIÂNGULO'

print(situacao)
