primeiro_numero = int(input('Qual será o primeiro número? '))
segundo_numero = int(input('Digite qual será o segundo número? '))
razao = int(input('Digite qual a razão da P.A'))

for c in range(primeiro_numero, segundo_numero, razao):
    print(c)
numero_atual = c
numero = c+1
razao = primeiro_numero + segundo_numero

