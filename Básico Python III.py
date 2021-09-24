"""
#Exercicio 1
for _ in range(1, 6):
    print('3 * {0:.0f} = {1:.0f}'.format(_, _*3))

#Exercicio 2
for i in range(0, 101):
    print(i)
i = 0
while i <= 100:
    print(i)
    i += 1

#Exercicio 3
i = 10
print('Contagem regressiva:')
while i > 0:
    print(i)
    j = 0
    while j < 10000000:#Laço para delay
        j += 1
    i -= 1
print('Fim')

#Exercicio 4
i = 0
while i <= 100000:
    print(i)
    i = i + 1000

#Exercicio 5
valores = []
for _ in range(1, 11):
    valores.append(int(input('Digite o valor {0:.0f}:'.format(_))))
print('A soma é: {0:.0f}'.format(sum(valores)))

#Exercicio 6
valores = []
for _ in range(1, 11):
    valores.append(float(input('Digite o valor {0:.0f}:'.format(_))))
print('A média é: {0:.2f}'.format((sum(valores))/10))

#Exercicio 7
valores = []
cont = 0
for i in range(1, 11):
    valores.append(float(input('Digite o valor {0:.0f}:'.format(i))))
    if valores[i-1] < 0:
        valores[i-1] = 0
        cont = cont + 1
print('A média é: {0:.2f}'.format((sum(valores))/(10-cont)))

#Exercicio 8
valores = []
maior = -10000000
menor = 100000000
for i in range(1, 11):
    valores.append(float(input('Digite o valor {0:.0f}:'.format(i))))
    if valores[i-1] > maior:
        maior = valores[i-1]
    if valores[i-1] < menor:
        menor = valores[i-1]
print('O maior valor é {0:.0f}\nO menor valor é {1:.0f}'.format(maior, menor))

#Exercicio 9
n = int(input('Digite um número inteiro natural: '))
print(n)
for i in range(0, n):
    if n % 2 == 0:
        n += 1
    else:
        n += 2
    print(n)

#Exercicio 10
soma = 0
soma1 = 0
for i in range(1, 99):
    if i % 2 == 0:
        soma = soma + i
    else:
        soma1 = soma1 + i
print('Soma dos 50 primeiros números pares:',soma)

#Exercicio 11
n = int(input('Digite um número inteiro: '))
for i in range(0, n+1):
    print(i)

#Exercicio 12
n = int(input('Digite um número inteiro: '))
for i in range(n, -1, -1):
    print(i)

#Exercicio 13
n = int(input('Digite um número inteiro natural: '))
if n % 2 != 0:
    print('Número digitado não é par!')
    n = -1
for i in range(0, n+1):
    if i % 2 == 0:
        print(i)

#Exercicio 14
n = int(input('Digite um número inteiro natural: '))
if n % 2 != 0:
    print('Número digitado não é par!')
    n = -2
for i in range(n+1, -1, -1):
    if i % 2 == 0:
        print(i)

#Exercicio 15
n = int(input('Digite um número inteiro natural: '))
if n % 2 == 0:
    print('Número digitado não é impar!')
    n = -1
for i in range(0, n+1):
    if i % 2 != 0:
        print(i)

#Exercicio 16
n = int(input('Digite um número inteiro natural: '))
if n % 2 == 0:
    print('Número digitado não é impar!')
    n = -2
for i in range(n+1, 0, -1):
    if i % 2 != 0:
        print(i)

#Exercicio 17
n = int(input('Digite um número inteiro natural: '))
soma = 0
if n % 2 != 0:
    print('Número digitado não é par!')
    n = -1
for i in range(0, n+1):
    if i % 2 == 0:
        soma = soma + i
print('A soma é {0:.0f}'.format(soma))

#Exercicio 18
n = int(input('Digite uma quantidade de numeros a digitar: '))
maior = 0
val = 0
cont = 0
for i in range(0, n):
    val = int(input('Digite o valor {0}: '.format(i+1)))
    if val > maior:
        maior = val
        cont = 1
    elif val == maior:
        cont += 1
print('Maior valor: {0:.0f}\nContado: {1:.0f}'.format(maior, cont))

#Exercicio 19
b = int(input('Digite um número entre 100 a 999: '))
if b>=100 and b<=999:
    c = int(b/10)
    c = int(c/10)
    print(c)
    c = c * 100
    d = int(b - c)
    e = int(d/10)
    print(e)
    print(d-e*10)
else:
    print('Número não corresponde ao solicitado!')
#print(int(c/100),e,d-e*10)

#Exercicio 20
n = 0
cont =0
p = 0
while n != 1000:
    n = int(input('Digite um valor: '))
    if n == 1000:
        break
    p += 1
    if n % 2 == 0:
        print('É número par!')
        cont += 1
    else:
        print('Não é número par')
print('{0:.0f} Números lidos\n{1:.0f} Números pares'.format(p, cont))

#Exercicio 21
a = int(input('Digite n1: '))
b = int(input('Digite n2: '))
c = 0

for i in range(0, a):
    if i % 2 == 0:
        c = c + i
print('A soma dos números pares: {0:.2f}'.format(c))
i = 0
c = 1
for i in range(0, b):
    if i % 2 != 0:
        c = c * i
print('A multiplicação dos números impares: {0:.2f}'.format(c))

#Exercicio 22
nota = 11
media = []
cont = 0
while nota != 0:
    nota = float(input('Digite a nota: '))
    if nota < 10 or nota > 20:
        nota = 0
        break
    media.append(nota)
    cont += 1
if cont == 0:
    cont = 1
print('A média é: {0:.2f}'.format(sum(media)/cont))

#Exercicio 23
divisores = []
dividendo = int(input('Digite um dividendo: '))
for i in range(1, dividendo+1):
    if dividendo % i == 0:
        divisores.append(i)
print(divisores)

#Exercicio 24
divisores = []
dividendo = int(input('Digite um dividendo: '))
for i in range(1, dividendo):
    if dividendo % i == 0:
        divisores.append(i)
print('A soma de {0} é: {1}'.format(divisores, sum(divisores)))

#Exercicio 25
liste = []
for i in range(1, 1000):
    if i % 3 == 0 or i % 5 == 0:
        liste.append(i)
print('A soma de {0} é: {1}'.format(liste, sum(liste)))

#Exercicio 26
a = int(input('Digite um valor: '))
for a in range(a, a*100):
    if a % 11 == 0 or a % 13 == 0 or a % 17 == 0:
        if a % 11 == 0:
            b = 11
        elif a % 13 == 0:
            b = 13
        else:
            b = 17
        break
print('Valor mais próximo: {0}\nDivisor: {1}'.format(a, b))

#Exercicio 27
n = int(input('Digite o valor n: '))
H = float(1)
for i in range(1, n+1):
    H = H + (1/i)
print('O valor Harmonico é: {0:.2f}'.format(H))

#Exercicio 28
h = int(input('Digite o valor desejado: '))
t = 1
for i in range(1, h+1):
    f = i
    for j in range(i-1, 1, -1):
        f = f * j
    j = 0
    t = t + 1/f
print(t)

#Exercicio 29
s = 0
for i in range(1, 6):
    e = 1
    j = 0
    for j in range(i*2, 1, -1):
        e = e * j
    print(e)
    s = s + i/e
print(s)

#Exercicio 30
n = int(input('Digite um valor n: '))
s = 0
s1 = 0
s2 = 0
for i in range(0, n):
    s = s + i
for j in range(0, n):
    s1 = -2*j + 1 + s1
for k in range(0, n):
    s2 = 2*k - 1 + s2
print(s, s1, s2)

#Exercicio 31
i = 1
j = 1
s = 0
while i < 51:
    s = s + (j/i)
    i += 1
    j += 2
print(s)

#Exercicio 32
import random
n = int(input('Digite quantidade n: '))
for i in range(1, n+1):
    d1 = random.randrange(1, 7)
    d2 = random.randrange(1, 7)
    print('Lançamento {0}: d1={1}, d2={2}'.format(i, d1, d2))
    if(d1>d2):
        print('d1 maior que d2, diferença: {0}\n'.format(d1-d2))
    elif(d1==d2):
        print('d1 é igual a d2, diferença: 0\n')
    else:
        print('d2 maior que d1, diferença: {0}\n'.format(d2-d1))

#Exercicio 33
n = int(input('Digite a quantidade de n: '))
i = int(input('Digite o valor de i: '))
j = int(input('Digite o valor de j: '))
s = set()
for _ in range(0, n):
    s.add(i*_)
    if n == len(s):
        break
    s.add(j*_)
print(s)

#Exercicio 34
#i = 232792560
cont = 0
for i in range(230000000, 240000000):
    cont = 0
    for _ in range(1, 21):
        if i % _ == 0:
            cont += 1
        else:
            cont = 0
        if cont == 20:
            break
    if cont == 20:
        break
print(cont, i)


#Exercicio 35
n0 = int(input('Digite o vaor inicial: '))
nf = int(input('Digite o valor final: '))
sum = 0
for i in range(nf, n0-1, -1):
    if i % 2 != 0:
        sum = sum + i
if n0 > nf:
    print('Intervalo Invalido!')
else:
    print(sum)

#Exercicio 36
soma = list(range(1, 101))
sqrt = []
for i in range(0, 101):
    sqrt.append(i**2)
print('Soma do quadrado: {0}\nO quadrado da soma: {1}'.format(sum(sqrt), sum(soma)**2))

#Exercicio 37

#Exercicio 38
a = int(input('Digite o valor a: '))
b = int(input('Digite o valor b: '))
c = a**2 + b**2
print('\t   o valor c: {0:.0f}'.format(pow(c, 1/2)))

#Exercicio 39
base = int(input('Digite a base: '))
alt = int(input('Digite a altura: '))

if(base<=0 or alt <=0):
    print('Dados invalidos!')
else:
    print('Área do triângulo: {0:.2f}'.format((base*alt)/2))

#Exercicio 40
print('Digite um valor, para sair digite um valor negativo!\n')
i = 5
maior = 0
menor = 10000
while i >= 0:
    if i > maior:
        maior = i
    if i < menor:
        menor = i
    i = int(input('Digite um valor: '))
print('Maior: {0}\nMenor: {1}'.format(maior, menor))

#Exercicio 41
i = 1
r1 = 0
r2 = 0
req = 0.00
while i != 0:
    r1 = int(input('Informe R1: '))
    r2 = int(input('Informe R2: '))
    if r1 == 0 or r2 == 0:
        break
    print('Resistencia equivalente: {0:.2f}'.format((r1*r2)/(r1+r2)))
print('Obrigado por utilizar o associador de resistor!')

#Exercicio 42
i = 1
while i >= 0:
    i = int(input('Digite um valor: '))
    if i <= 0:
        break
    print('Quadrado: {0}\nCubo: {1}\nRaiz: {2:.2f}'.format(i**2, i**3, pow(i, 1/2)))
print('Obrigado por usar o exponenciador')

#Exercicio 43
i = 1
cont = 0
idade = 0
while i != 0:
    i = int(input('Digite a idade: '))
    if i == 0:
        break
    cont += 1
    idade += i
print('A media é: {0:.2f}'.format(idade/cont))

#Exercicio 44
lista = [0, 1]
i = 0
val = int(input('Digite um valor: '))
while True:
    i += 1
    print(lista[i], lista[i-1], i)
    if val < lista[i]:
        break
    else:
        lista.append(lista[i-1]+lista[i])
print(lista)

#Exercicio 45
escolha = 0
velocidade = 0
while escolha != 3:
    escolha = int(input('1 - Converter Km/h -> M/s\n2 - Converter M/s -> Km/h\n3 - Sair\n'))
    if escolha == 3:
        break
    elif escolha == 2:
        velocidade = float(input('Digite a velocidade em M/s: '))
        print('Velocidade {0:.2f} M/s = {1:.2f} Km/h'.format(velocidade, velocidade*3.6))
    elif escolha == 1:
        velocidade = float(input('Digite a velocidade em Km/h: '))
        print('Velocidade {0:.2f} Km/h = {1:.2f} M/s'.format(velocidade, velocidade/3.6))
    else:
        print('Escolha invalida!')
print('Obrigado por usar o velocidade calculator')

#Exercicio 46
from random import randint
rand = randint(1, 1001)
print(rand)
i = 1
cont = 0
while i != 0:
    i = int(input('Digite um valor: '))
    cont += 1
    if i == rand:
        print('Acertou!')
        break
    elif i > rand:
        print('Número digitado deve ser menor')
    elif i < rand:
        print('Número digitado deve ser maior')
print('Quantidades de tentativas: {0}'.format(cont))

#Exercicio 47
opcao = 0
while opcao != 5:
    opcao = int(input('Escolha uma opção abaixo:\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n5 - Saída\n'))
    if opcao == 5:
        print('Obrigado por utilizar o calculator')
        break
    elif opcao == 1:
        res = num1 + num2
    elif opcao == 2:
        res = num1 - num2
    elif opcao == 3:
        res = num1 * num2
    elif opcao == 4:
        res = num1 / num2
    else:
        print('Opção invalida!')
        break
    num1 = float(input('Digite o valor 1:'))
    num2 = float(input('Digite o valor 2:'))
    print('O resultado é: {0:.2f}\n'.format(res))

#Exercicio 48
fibo = [0, 1]
soma = 0
i = 0
while i < 400000:
    fibo.append(fibo[-1]+fibo[-2])
    if fibo[-1] % 2 == 0:
        soma = soma + fibo[-1]
    if soma > 4000000:
        break
    i += 1
print(f'Fibo: {fibo}\nSoma:{soma}')

#Exercicio 49
Carlos = float(input('Digite o salario de Carlos: '))
Joao = Carlos/3
i = 0
while Carlos > Joao:
    Carlos = Carlos + (Carlos*0.02)
    Joao = Joao + (Joao*0.05)
    i += 1
    if Joao > Carlos:
        break
print('Valor Carlos: {0:.2f}\nValor João: {1:.2f}\nTempo: {2} Meses'.format(Carlos, Joao, i))

#Exercicio 50
Chico = 1.5
Ze = 1.1
i = 0
while Chico > Ze:
    Chico = Chico + 0.02
    Ze = Ze + 0.03
    i += 1
    if Ze > Chico:
        break
print('Em {0} anos, Ze terá {1:.2f} e Chico terá {2:.2f}'.format(i, Ze, Chico))

#Exercicio 51
sal = 2030
i = 1997
taxa = 0.03
while i < 2020:
    sal = sal + (sal * taxa)
    taxa *= 2
    i += 1
print(sal)

#Exercicio 52
saque = int(input('Digite o valor para saque: '))
cem = 0
cinq = 0
vin = 0
dez = 0
cinc = 0
doi = 0
um = 0
while saque != 0:
    if saque / 100 >= 1:
        cem = int(saque / 100)
        saque = saque - cem * 100
    elif saque / 50 >= 1:
        cinq = int(saque / 50)
        saque = saque - cinq * 50
    elif saque / 20 >= 1:
        vin = int(saque / 20)
        saque = saque - vin * 20
    elif saque / 10 >= 1:
        dez = int(saque / 10)
        saque = saque - dez * 10
    elif saque / 5 >= 1:
        cinc = int(saque / 5)
        saque = saque - cinc * 5
    elif saque / 2 >= 1:
        doi = int(saque / 2)
        saque = saque - doi * 2
    elif saque / 1 >= 1:
        um = int(saque / 1)
        saque = 0
print('Cem: {0}\nCinquenta: {1}\nVinte: {2}\nDez: {3}\nCinco: {4}\nDois: {5}\nUm: {6}'.format(cem, cinq, vin, dez, cinc, doi, um))

#Exercicio 53
a = []
n = int(input('Digite o valor de n: '))
for i in range(1, n+1):
    a.append(i)
    print(a)

#Exercicio 54
num = int(input('Digite um número: '))
cont = 0
for i in range(1, num+1):
    if num % i == 0:
        cont += 1
if cont == 1 or cont == 2:
    print('Número Primo!')
else:
    print('Não é número primo!')

#Exercicio 55
n = int(input('Digite um número: '))
a = []
for i in range(1, n+1):
    cont = 0
    for j in range(1, i+1):
        if i % j == 0:
            cont += 1
    if cont == 1 or cont == 2:
        a.append(i)
print('Sequência: {0} = soma({1})'.format(a, sum(a)))

#Exercicio 56
a = []
for i in range(1, 200):
    cont = 0
    for j in range(1, i+1):
        if i % j == 0:
            cont += 1
    if cont == 1 or cont == 2:
        a.append(i)
print('Soma = {0}'.format(sum(a)))

#Exercicio 57
b = int(input('Digite o valor a: '))
c = int(input('Digite o valor b: '))
a = []
for i in range(b, c+1):
    cont = 0
    for j in range(1, i+1):
        if i % j == 0:
            cont += 1
    if cont == 1 or cont == 2:
        a.append(i)
print('Sequencia: {0}\nQuantidade = {1}'.format(a, len(a)))

#Exercicio 58
b = int(input('Digite o valor a: '))
c = int(input('Digite o valor b: '))
a = []
for i in range(b, c+1):
    cont = 0
    for j in range(1, i+1):
        if i % j == 0:
            cont += 1
    if cont == 1 or cont == 2:
        a.append(i)
print('Sequencia: {0}\n Soma = {1}'.format(a, sum(a)))

#Exercicio 59
populacao = int(input('Digite a população: '))
print('codigo do do consumidor:\n1 - Residencial\n2 - Comercial\n3 - Industrial')
lista1 = []
lista2 = []
resi = 0
come = 0
indu = 0
for i in range(1, populacao+1):
    lista1.append(int(input('Digite o consumo {0} em KWh: '.format(i))))
    lista2.append(int(input('Digite o código {0}: '.format(i))))
    if lista2[-1] == 1:
        resi += lista1[-1]
    elif lista2[-1] == 2:
        come += lista1[-1]
    elif lista2[-1] == 3:
        indu += lista1[-1]
    else:
        print('Código invalido! Dados apagados')
        lista1.pop()
        lista2.pop()
maior = max(lista1, key=int)
menor = min(lista1, key=int)
print('Maior Consumo: {0}\nMenor Consumo: {1}'.format(maior, menor))
print('Média de Consumo: {0:.2f}'.format(sum(lista1)/len(lista1)))
print(f'Consumo Residencial: {resi}')
print(f'Consumo Comercial: {come}')
print(f'Consumo Industrial: {indu}')

#Exercicio 60
a = []
while True:
    a.append(int(input('Digite um numero natural: ')))
    if a[-1] == 0:
        a.pop()
        break
print(f'Soma: {sum(a)}')
print(f'Elementos: {len(a)}')
print('Média: {0:.2f}'.format(sum(a)/len(a)))
print(f'Maior: {max(a, key=int)}')
print(f'Menor: {min(a, key=int)}')
pares = filter(lambda valor: valor % 2 == 0, a)
print('Soma de pares: {0}'.format(sum(list(pares))))


#Bonus---------------------------------------------------------------------------------------------------Números primos
p = int(input('Digite um número: '))
cont = 0
for _ in range(1, p+1):
    if p % _ == 0:
        cont = cont + 1
if cont == 2 or cont == 1:
    print('É um número primo')
else:
    print('Não é um número primo')
"""
"""--------------------------------------------------------Base para um sistema de vendas com cadastramento de produtos
produtos = {'TV': 800, 'PS4': 950, 'DVD': 150}
lista = {}
var = ''
cont = 0
val = 0
while var != 'SAIR':
    var = str(input('Digite o produto: '))
    var = var.upper()
    if var == 'SAIR':
        break
    if var in produtos:
        val = produtos[var]
    else:
        cad = str(input('Produto não cadastrado!\nDeseja cadastra-lo?\n'))
        cad = cad.upper()
        if cad == 'Y' or cad == 'SIM' or cad == 'YES' or cad == 'S':
            val = int(input('Informe o valor: '))
            produtos[var] = val
        else:
            val = 0
    if val == 0:
        qtde = 0
    else:
        qtde = int(input('Digite a quantidade: '))
        print('{0} x {1:.2f} = {2:.2f}'.format(qtde, val, val*qtde))
        lista.update({var: qtde*val})
        cont = cont + (qtde*val)
print('\'Produtos\': \'Valor produtos\' = {0} Total = {1}'.format(lista, cont))
"""

lista = [0, 28, 15, 32, 44, 19, 28.3, 40, 3, 4.8]
print(list(map(lambda r: 9/5 * r + 32, lista)))
