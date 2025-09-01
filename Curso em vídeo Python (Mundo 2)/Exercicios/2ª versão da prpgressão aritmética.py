primeiro_numero = int(input('Qual é o primeiro número da progressão?'))
segundo_numero = int(input('Digite qual é'))
razao = segundo_numero - primeiro_numero
for c in range(primeiro_numero, 10+1, razao):
    primeiro_numero = c
    proximo_numero = c+1
    print(primeiro_numero)
    print(segundo_numero)
    p_a = primeiro_numero + razao

    


    