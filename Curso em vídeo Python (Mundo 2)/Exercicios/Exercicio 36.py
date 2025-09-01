# APROVAR O EMPRÉSTIMO PARA A COMPRA DE UMA CASA
# EU TINHA ERRADO A CONTA DA PRESTAÇÃO E DO MINIMO DE SALÁRIO NECESSÁRIO PARA PAGAR O EMPRÉSTIMO (O CÁLCULO DA PORCENTAGEM)
# AÍ EU FIZ A CORREÇÃO COM O GUANABARA
#P.S DEVO PRATICAR A UTILIZAÇÃO DE PORCENTAGEM E A REALIZAÇÃO DE CÁLCULOS PARA MELHORA-LOS

valor_da_casa = float(input('Qual é o valor da casa que você deseja comprar? R$'))
salario_do_comprador = float(input('Qual é o valor do seu salário?'))
em_quantos_anos_deseja_pagar = int(input('Em quatos anos você deseja pagar o empréstimo?'))

# CALCULANDO O VALOR DA PRESTAÇÃO MENSAL

# Valor da prestação é o valor da casa / (anos * 12) anos * 12 é a quantidade de meses do empréstimo.
valor_da_prestacao_mensal = valor_da_casa/(em_quantos_anos_deseja_pagar * 12) #anos * 12 diz a quantidade de meses que o empréstimo vai ser pago

minimo_do_salario = salario_do_comprador * 30 / 100

print(f'Para pagar uma casa de RS{valor_da_casa} em {em_quantos_anos_deseja_pagar} anos a prestação será de R${valor_da_prestacao_mensal }')

if valor_da_prestacao_mensal <= minimo_do_salario:
    print('EMPRÉSTIMO APROVADO!')

else:
    print('EMPRÉSTIMO NEGADO!')

