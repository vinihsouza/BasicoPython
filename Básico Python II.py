"""
#Exercicio 1
val1 = float(input('Digite o valor 1: '))
val2 = float(input('Digite o valor 2: '))
if val1 > val2:
    print('Valor 1 maior')
elif val1 == val2:
    print('Valor 1 e 2 são iguais')
else:
    print('Valor 2 maior')

#Exercicio 2
val1 = float(input('Digite um valor: '))
if val1 < 0:
    print('Número negativo, Raiz Invalida')
else:
    print('Raiz: {0:.2f}'.format(pow(val1, 1/2)))

#Exercicio 3
val1 = float(input('Digite um valor: '))
if val1 < 0:
    print('Quadrado: {0:.2f}'.format(val1**2))
else:
    print('Raiz: {0:.2f}'.format(pow(val1, 1/2)))

#Exercicio 4
val = float(input('Digite um valor: '))
if val > 0:
    print('Quadrado: {0:.2f}'.format(val**2))
    print('Raiz: {0:.2f}'.format(pow(val, 1 / 2)))
else:
    print('Valor negativo')

#Exercicio 5
val = int(input('Digite um valor: '))
if val % 2 == 0:
    print('Valor Par')
else:
    print('Valor Impar')

#Exercicio 6
val1 = float(input('Digite o valor 1: '))
val2 = float(input('Digite o valor 2: '))
if val1 > val2:
    print('Valor 1 maior')
    dif = val1 - val2
elif val1 == val2:
    print('Valor 1 e 2 são iguais')
else:
    print('Valor 2 maior')
    dif = val1 - val2
print('Diferença de {0:.0f}'.format(dif))

#Exercicio 7
val1 = float(input('Digite o valor 1: '))
val2 = float(input('Digite o valor 2: '))
if val1 > val2:
    print('Valor 1 maior')
elif val1 == val2:
    print('Valor 1 e 2 são iguais')
else:
    print('Valor 2 maior')

#Exercicio 8
n1 = float(input('Digite a nota 1: '))
n2 = float(input('Digite a nota 2: '))
if n1 and n2 > 0 and n1 and n2 <= 10:
    print('Média: {0:.2f}'.format((n1+n2)/2))
else:
    print('Nota invalida')

#Exercicio 9
salario = float(input('Digite o salário: '))
emprest = float(input('Digite o valor do emprestimo: '))
if emprest/salario > 0.2:
    print('Emprestimo não concedido')
else:
    print('Emprestimo concedido')

#Exercicio 10
altura = float(input('Digite sua altura em metros: '))
sexo = str(input('Digite seu sexo: '))

if sexo.upper() == 'M' or sexo.upper() == 'MASCULINO':
    peso = altura * 72.7 - 58
else:
    peso = altura * 62.1 - 44.7

print('Seu peso ideal deve ser {0:.2f} Kilos'.format(peso))
"""

#Exercicio 11----------------------------------------------------------------Terminar

"""
#Exercicio 12
import math
val = float(input('Digite um valor: '))
if val > 0:
    print('O logaritmo de {0:.2f} é {1:.2f}'.format(val, math.log(val)))
else:
    print('Número invalido')

#Exercicio 13
a = []
for i in range(1, 4):
    a.append(float(input('Digite a média {0}: '.format(i))))
a.append(a[0] + a[1] + a[2]*2)
print('A média é {0:.2f}'.format(a[3] / 4))
if (a[3]/4) >= 60:
    print('Aprovado')
else:
    print('Reprovado')

#Exercicio 14
Trabalho = float(input('Digite a nota do trabalho: '))
Avaliação = float(input('Digite a nota da avaliação: '))
Exame = float(input('Digite a nota do exame: '))
Media = (Trabalho * 2 + Avaliação * 3 + Exame * 5) / 10
print('Média: {0:.2f}'.format(Media))
if Media <= 2.9 :
    print('Reprovado')
elif Media > 2.9 and Media <= 4.9:
    print('Recuperação')
else:
    print('Aprovado')

#Exercicio 15
x = int(input('Digite um valor de 1 a 7 correspondente a semana: '))
print({
        1: "Domingo",
        2: "Segunda",
        3: "Terça",
        4: "Quarta",
        5: "Quinta",
        6: "Sexta",
        7: "Sabado",
    }[x])

#Exercicio 16
x = int(input('Digite um valor de 1 a 12 correspondente ao mês: '))
print({
         1: "Janeiro",
         2: "Fevereiro",
         3: "Março",
         4: "Abril",
         5: "Maio",
         6: "Junho",
         7: "Julho",
         8: "Agosto",
         9: "Setembro",
        10: "Outubro",
        11: "Novembro",
        12: "Dezembro",
    }[x])

#Exercicio 17
BaseMenor = float(input('Digite a base menor: '))
BaseMaior = float(input('Digite a base maior: '))
Altura = float(input('Digite a altura do trapezio: '))
if BaseMenor == 0 or BaseMaior == 0 or Altura == 0:
    print('Valor(es) invalido(s)')
else:
    print('Área do trapezio = {0:.2f}'.format(((BaseMaior + BaseMenor) * Altura) / 2))

#Exercicio 18
oper = str(input('Escolha a operação desejada:\n+ Soma\n- Subtração\n* Multiplicação\n/ Divisão\n'))
n1 = float(input('Digite o valor 1: '))
n2 = float(input('Digite o valor 2: '))
if oper == '+':
    print('Resultado: {0:.2f}'.format(n1 + n2))
elif oper == '-':
    print('Resultado: {0:.2f}'.format(n1 - n2))
elif oper == '*':
    print('Resultado: {0:.2f}'.format(n1 * n2))
elif oper == '/':
     print('Resultado: {0:.2f}'.format(n1 / n2))
else:
    print('Operação invalida')

#Exercicio 19
numero = int(input('Digite um número: '))
if numero % 3 == 0:
    print('{0} é divisivel por 3'.format(numero))
if numero % 5 == 0:
    print('{0} é divisivel por 5'.format(numero))
else:
    print('Não são divisiveis')

#Exercicio 20
a = [0]
for i in range(1,4):
    a.append(int(input('Digite o lado {0}: '.format(i))))
if a[1] == a[2] and a[2] == a[3]:
    print('Triângulo Equilatero')
elif a[1] == a[2] or a[2] == a[3] or a[1] == a[3]:
    print('Triângulo Isósceles')
elif a[1] != a[2] and a[1] != a[3]:
    print('Triângulo Escaleano')
else:
    print('Valor não encontrado')
    
#Exercicio 21
opcao = int(input('Escolha uma opção abaixo:\n1 - Soma de 2 números\n2 - Diferença entre 2 números\n'
      '3 - Produto entre 2 números\n4 - Divisão entre 2 números\n'))
n1 = float(input('Digite o valor 1: '))
n2 = float(input('Digite o valor 2: '))
if opcao == 1:
    print('{0:.2f} + {1:.2f} = {2:.2f}'.format(n1, n2, n1+n2))
elif opcao == 2:
    print('Diferença entre {0:.2f} e {1:.2f} é {2:.2f}'.format(n1, n2, abs(n1 - n2)))
elif opcao == 3:
    print('{0:.2f} * {1:.2f} = {2:.2f}'.format(n1, n2, n1 * n2))
elif opcao == 4:
    if(n2 == 0):
        print('Divisão impossível!')
    else:
        print('{0:.2f} / {1:.2f} = {2:.2f}'.format(n1, n2, n1 / n2))
else:
    print('Opção invalida!')

#Exercicio 22
Idade = int(input('Digite sua idade: '))
TempoServico = int(input('Digite seu tempo de serviço: '))
if Idade >= 65:
    print('Pode se aposentar')
elif Idade >= 60 and TempoServico >= 25:
    print('Pode se aposentar')
elif TempoServico >= 30:
    print('Pode se aposentar')
else:
    print('Não pode se aposentar')

#Exercicio 23
ano = int(input('Digite um ano: '))
print(ano%4)
print(ano%100)
print(ano%400)
if ano % 4 == 0 and ano % 100 > 0:
    print('Ano bissexto')
elif ano % 400 == 0:
    print('Ano bissexto')
else:
    print('Ano não é bissexto')

#Exercicio 24
valor = float(input('Digite o valor: '))
estado = str(input('Digite o estado de destino (MG,SP,RJ,MS): '))
if estado == 'MG':
    print('O valor total será: {0:.2f}'.format(valor / 0.93)) #7%
elif estado == 'SP':
    print('O valor total será: {0:.2f}'.format(valor / 0.88)) #12%
elif estado == 'RJ':
    print('O valor total será: {0:.2f}'.format(valor / 0.85)) #15%
elif estado == 'MS':
    print('O valor total será: {0:.2f}'.format(valor / 0.92)) #8%
else:
    print('Estado invalido!')

#Exercicio 25
a = int(input('Digite o valor de ax²: '))
b = int(input('Digite o valor de bx: '))
c = int(input('Digite o valor de c: '))
d = pow(b, 2) - (4*a*c)
if d < 0:
    print('Não existe raiz')
elif d == 0:
    print('Existe uma raiz, é: {0:.2f}'.format(-b/(2*a)))
else:
    x1 = float((-b + pow(d, 1/2)) / (2*a))
    x2 = float((-b - pow(d, 1/2)) / (2*a))
    print('X1 = {0:.2f}\nX2 = {1:.2f}'.format(x1, x2))

#Exercicio 26
distancia = float(input('Digite a distancia em Km: '))
litros = float(input('Digite o consumo em litros: '))
if distancia/litros <= 8:
    print('Venda o carro!')
elif distancia/litros <= 12:
    print('Econômico!')
else:
    print('Super econômico!')

#Exercicio 27
idade = int(input('Digite a idade do nadador: '))
if idade >= 5 and idade <= 7:
    print('Infantil A')
elif idade >= 8 and idade <= 10:
    print('Infantil B')
elif idade >= 11 and idade <= 13:
    print('Juvenil A')
elif idade >= 14 and idade <= 17:
    print('Juvenil B')
elif idade >= 18:
    print('Senior')
else:
    print('Idade invalida!')

#Exercicio 28
print('Escolha uma opção abaixo e digite 3 números:')
a = str(input('(a)Geometrica\n(b)Ponderada\n(c)Harmonica\n(d)Aritmetica\n'))
x = float(input('Número X: '))
y = float(input('Número Y: '))
z = float(input('Número Z: '))
if a == 'a':
    print('{0:.2f}'.format(pow( x * y * z, 1/3)))
elif a == 'b':
    print('{0:.2f}'.format((x + 2*y + 3*z)/6))
elif a == 'c':
    print('{0:.2f}'.format((1/(1/x + 1/y + 1/z))))
elif a == 'd':
    print('{0:.2f}'.format((x+y+z)/3))
else:
    print('Operação invalida!')

#Exercicio 29
import random
c = 0
for _ in range(0, 5):
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    r = int(input('Qual a soma de {0} + {1} :'.format(a, b)))
    if(a + b == r):
        print('Resposta Correta')
        c = c + 2
    else:
        print('Resposta Errada, valor exato seria: {0}'.format(a+b))
print('Você acertou {0:.0f}\nNota final: {1}'.format(c/2, c))

#Exercicio 30
a = []
for _ in range(1, 4):
    a.append(int(input('Digite o número {0}:'.format(_))))
a.sort()
print(a)

#Exercicio 31
altura = float(input('Digite sua altura em metros: ')) 
peso = float(input('Digite seu peso em Kg: '))

if altura < 1.2:
    if peso < 60:
        print('A')
    elif peso <= 90: 
        print('D')
    else:
        print('G')
elif altura <= 1.7:
    if peso < 60:
        print('B')
    elif peso <= 90:
        print('E')
    else:
        print('H')
else:
    if peso < 60:
        print('C')
    elif peso <= 90:
        print('F')
    else:
        print('I')

#Exercicio 32
print('Bem vindo ao Vini lanches!\n')
print('Abaixo está o cardapio:\n')
print('100 = Cachorro quente = 1.20\n'
'101 = Bauru simples = 1.30\n'
'102 = Bauru com ovo = 1.50\n'
'103 = Hamburguer = 1.20\n'
'104 = Cheeseburguer = 1.70\n'
'105 = Suco = 2.20\n'
'106 = Refrigerente = 1.00\n'
'1 = Fechar pedido\n')
codigo = 0
lista = []
while codigo != 1:
    codigo = int(input('Digite o código do lanche: '))
    if codigo == 100:
        lista.append(1.2)
        print('\tCachorro quente: 1.20')
    elif codigo == 101:
        lista.append(1.3)
        print('\tBauru simples: 1.30')
    elif codigo == 102:
        lista.append(1.5)
        print('\tBauru com ovo: 1.50')
    elif codigo == 103:
        lista.append(1.2)
        print('\tHamburguer: 1.20')
    elif codigo == 104:
        lista.append(1.7)
        print('\tCheeseburguer: 1.70')
    elif codigo == 105:
        lista.append(2.2)
        print('\tSuco: 2.20')
    elif codigo == 106:
        lista.append(1)
        print('\tRefrigerante: 1.00')
    else:
        break
print('Total: {0:.2f}'.format(sum(lista)))

#Exercicio 33
preco = float(input('Digite o valor do produto: '))

if preco <= 50:
    preco = preco * 1.05
    print('Novo preço: {0:.2f} \nBarato'.format(preco))
elif preco <= 100:
    preco = preco * 1.1
    if preco < 80:
        print('Novo preço: {0:.2f} \nBarato'.format(preco))
    else:
        print('Novo preço: {0:.2f} \nNormal'.format(preco))
else:
    preco = preco * 1.15
    if preco > 200:
        print('Novo preço: {0:.2f} \nMuito caro'.format(preco))
    else:
        print('Novo preço: {0:.2f} \nCaro'.format(preco))

#Exercicio 34
a = ['A', 'B', 'C', 'D', 'E', 'E']
#     0    1    2    3    4    5
nota = float(input('Digite a nota: '))
faltas = int(input('Digite o número de faltas: '))

if nota >= 9:
    b = 0
elif nota >= 7.5:
    b = 1
elif nota >= 5:
    b = 2
elif nota >= 4:
    b = 3
else:
    b = 4

if faltas > 20:
    b += 1
else:
    b = b
print('Seu conceito é: {0}'.format(a[b]))

#Exercicio 35
dia = int(input('Digite o dia: '))
mes = int(input('Digite o mês: '))
ano = int(input('Digite o ano: '))
lista = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if ano % 4 == 0 and ano % 100 > 0 or ano % 400 == 0:
    lista[1] = 29
if mes > 12 or mes < 0:
    print('Data invalida!')
if dia > 31 or dia < 0:
    print('Data invalida!')
if dia <= lista[mes-1]:
    print('Data valida!')
else:
    print('Data invalida!')

#Exercicio 36
venda = float(input('Digite o total vendido no mês R$ '))
if venda >= 100000:
    venda = (venda*0.16) + 700
elif venda >= 80000:
    venda = (venda*0.14) + 650
elif venda >= 60000:
    venda = (venda*0.14) + 600
elif venda >= 40000:
    venda = (venda*0.14) + 550
elif venda >= 20000:
    venda = (venda*0.14) + 500
else:
    venda = (venda*0.14) + 400
print('O valor da comissão será R$ {}'.format(venda))

#Exercicio 37 #------------------------------------------------------------------------------------Revisar
horac = int(input('Digite o par de hora chegada: '))
minutoc = int(input('Digite o par de minuto chegada: '))
horas = int(input('Digite o par de hora saída: '))
minutos = int(input('Digite o par de minuto saída: '))

horad = horas - horac
minutod = minutos - minutoc
val = 0
if horad < 0:
    horad = 24 + horad
if minutod < 0:
    minutod = 60 + minutod
if horad == 0:
    val = 0
if minutod == 0:
    val = 0
if minutod > 0:
    horad += 1
if horad > 0:
    if horad <= 2:
        val = horad * 1
    elif horad <= 4:
        val = 2 + (horad - 2) * 1.4
    else:
        val = 2 + 2.8 + (horad - 4) * 2
print(val)

#Exercicio 38
dia = int(input('Digite o dia do nascimento: '))
mes = int(input('Digite o mês do nascimento: '))
ano = int(input('Digite o ano do nascimento: '))
lista = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if ano % 4 == 0 and ano % 100 > 0 or ano % 400 == 0:
    lista[1] = 29
if mes > 12 or mes < 0:
    print('Data invalida!')
if dia > 31 or dia < 0:
    print('Data invalida!')
if dia <= lista[mes-1]:
    print('Data valida!')
else:
    print('Data invalida!')

#Exercicio 39
salario = float(input('Digite seu salario: '))
tempo = int(input('Digite o tempo de serviço em anos: '))

if salario <= 500:
    salario = salario * 1.25
elif salario <= 1000:
    salario = salario * 1.2
elif salario <= 1500:
    salario = salario * 1.15
elif salario <= 2000:
    salario = salario * 1.1
else:
    salario = salario
if tempo > 10:
    salario = salario + 500
elif tempo >= 7:
    salario = salario + 300
elif tempo >= 4:
    salario = salario + 200
elif tempo >= 1:
    salario = salario + 100
else:
    salario = salario

print('Seu novo salario será R$ {0:.2f}'.format(salario))

#Exercicio 40
custo = float(input('Digite o custo do veiculo: '))

if custo > 25000:
    custo = custo / .65
elif custo > 12000:
    custo = custo / .75
else:
    custo = custo / .95

print('O custo com impostos será: {0:.2f}'.format(custo))

#Exercicio 41
altura = float(input('Digite sua altura em metros: '))
peso = float(input('Digite seu peso em Kilogramas: '))
imc = peso / (pow(altura, 2))
if imc >= 40:
    print('Obesidade Grau lll (morbida)')
elif imc >= 35:
    print('Obesidade Grau ll (severa)')
elif imc >= 30:
    print('Obesidade Grau l')
elif imc >= 25:
    print('Peso em excesso')
elif imc >= 18.6:
    print('Saudável')
else:
    print('Abaixo do peso')
print('IMC: {0:.2f}'.format(imc))
"""

#
# Complete the 'subarraySum' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


lista = [4,[5,[6]]]
print(sum(lista))
