# Ler o primeiro termo e a razão de uma P.A.
# Mostrar os 10 primeiros termos dessa progressão

primeiro_termo = int(input('Informe o primeiro termo da progressão aritmética: '))
razao = int(input('Informe a razão da P.A: '))

for c in range(primeiro_termo, razao):
    primeiro_numero = c
    print(primeiro_numero)
    segundo_numero = primeiro_numero + c
    print(segundo_numero)

    constante = primeiro_numero + segundo_numero
    print(constante)

#for i in range(segundo_numero, constante):
#    constante = segundo_numero+constante
#    print(constante)


    