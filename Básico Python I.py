"""
#Exercicio 1
valor = input('Digite um valor: ')
print('O valor digitado foi: {}'.format(valor))

#Exercicio 2
valorf = float(input('Digite um valor real: ')
print('O valor digitado foi: {:.2f}'.format(valor))

#Exercicio 3
val1 = int(input('Digite o valor 1:'))
val2 = int(input('Digite o valor 2:'))
val3 = int(input('Digite o valor 3:'))
print('A soma de {0} + {1} + {2} é: {3}'.format(val1, val2, val3, val1+val2+val3))

#Exercicio 4
num = float(input('Digite um número real: '))
print('O quadrado de {0:.2f} é {1:.2f}'.format(num, num*num))

#Exercicio 5
num1 = float(input('Digite um valor: '))
print('A quinta parte é:{0:.5f}'.format(num1/5))

#Exercicio 6
tempC = float(input('Digite a temperatura em graus Celsius: '))
tempF = tempC*(9/5)+32
print('{0:.2f}°C = {1:.2f}°F'.format(tempC, tempF))

#Exercicio 7
tempF1 = float(input('Digite a temperatura em graus Fahrenheit: '))
tempC1 = 5*(tempF1-32)/9
print('{0:.2f}°F = {1:.2f}°C'.format(tempF1, tempC1))

#Exercicio 8
tempK = float(input('Digite a temperatura em graus Kelvin: '))
print('{0:.2f}°K = {1:.2f}°C'.format(tempK, tempK-273.15))

#Exercicio 9
tempC2 = float(input('Digite a temperatura em graus Celsius: '))
print('{0:.2f}°C = {1:.2f}°K'.format(tempC2, tempC2+273.15))

#Exercicio 10
Velkm = float(input('Digite a velocidade em Km/h: '))
print('A velocidade {0:.2f} Km/h equivale a {1:.2f} m/s'.format(Velkm, Velkm/3.6))

#Exercicio 11
Velms = float(input('Digite a velocidade em m/s: '))
print('A velocidade {0:.2f} m/s equivale a {1:.2f} Km/h'.format(Velms, Velms*3.6))

#Exercicio 12
Distmi = float(input('Digite a distancia em Milhas: '))
print('A distancia {0:.2f} Milhas equivale a {1:.2f} Km'.format(Distmi, Distmi*1.61))

#Exercicio 13
Distkm = float(input('Digite a distancia em Km: '))
print('A distancia {0:.2f} Km equivale a {1:.2f} Milhas'.format(Distkm, Distkm/1.61))

#Exercicio 14
pi = 3.14159265358979
Angdeg = float(input('Digite o ângulo em Graus: '))
print('{0:.4f}° = {1:.4f} Rad'.format(Angdeg, Angdeg*pi/180))

#Exercicio 15
pi = 3.14159265358979
Angrad = float(input('Digite o ângulo em Radianos: '))
print('{0:4f} Rad = {1:.4f}'.format(Angrad, Angrad*180/pi))

#Exercicio 16
comppol = float(input('Digite o valor em polegadas: '))
print('{0:.2f} inch = {1:.2f} cm'.format(comppol, comppol*2.54))

#Exercicio 17
CompCm = float(input('Digite o valor em Centimetros: '))
print('{0:.2f} cm = {1:.2f} inch'.format(CompCm, CompCm/2.54))

#Exercicio 18
VolM = float(input('Digite o valor do volume em m³: '))
print('{0:.2f} m³ = {1:.2f} Litros'.format(VolM, VolM*1000))

#Exercicio 19
VolL = float(input('Digite o valor do volume em Litros: '))
print('{0:.2f} Litros = {1:.2f} m³'.format(VolL, VolL/1000))

#Exercicio 20
MasK = float(input('Digite a massa em Kg: '))
print('{0:.2f} Kg = {1:.2f} lb'.format(MasK, MasK/.45))

#Exercicio 21
MasL = float(input('Digite a massa em lb: '))
print('{0:.2f} lb = {1:.2f} Kg'.format(MasL, MasL*0.45))

#Exercicio 22
DistJ = float(input('Digite a distancia em Jardas: '))
print('{0:.2f} Jardas = {1:.2f} Metros'.format(DistJ, DistJ*0.91))

#Exercicio 23
DistM = float(input('Digite a distancia em Metros: '))
print('{0:.2f} Metros = {1:.2f} Jardas'.format(DistM, DistM/0.91))

#Exercicio 24
AreaM = float(input('Digite a área em m²: '))
print('{0:.2f} m² = {1:.2f} Acres'.format(AreaM, AreaM*.000247))

#Exercicio 25
AreaA = float(input('Digite a área em acres: '))
print('{0:.2f} Acres = {1:.2f} m²'.format(AreaA, AreaM*4048.58))

#Exercicio 26
AreaMe = float(input('Digite a área em m²: '))
print('{0:.2f} m² = {1:.4f} Hectares'.format(AreaMe, AreaMe/10000))

#Exercicio 27
AreaH = float(input('Digite a área em hectares: '))
print('{0:.4f} Hectares = {1:.2f} m²'.format(AreaH, AreaH*10000))

#Exercicio 28
a = [0, 0, 0, 0]
for i in range(0, 3):
    a[i] = float(input('Digite um o valor {0:.0f}:'.format(i+1)))
    a[3] = a[3] + a[i]**2
print('A soma do quadrado dos 3 valores é: {0:.2f}'.format(a[3]))

#Exercicio 29
a = [0, 0, 0, 0, 0]
for i in range(0, 4):
    a[i] = float(input('Digite um a nota {0:.0f}:'.format(i+1)))
    a[4] = a[4] + a[i]
print('A média aritimetica é: {0:.2f}'.format(a[4]/4))

#Exercicio 29 Outra forma
lista = []
for i in range(1, 5):
    a = float(input('Digite a nota {}: '.format(i)))
    lista.append(a)
print('A média é: {0:.2f}'.format(sum(lista)/4))

#Exercicio 30
ValorRe = float(input('Digite o valor Real:'))
Cotacao = float(input('Digite a cotação do Dólar: '))
print('{0:.2f} BRL = {1:.2f} USD'.format(ValorRe, ValorRe/Cotacao))

#Exercicio 31
Number = int(input('Digite um número inteiro: '))
print('Antecessor: {0}\nNúmero: \t{1}\nSucessor: \t{2}'.format(Number-1, Number, Number+1))

#Exercicio 32
Number = int(input('Digite um número inteiro: '))
print('Antecessor:{0}\nSucessor:{1}\n{0} * 3 + {1} * 2 = {2}'.format(Number-1, Number+1, ((Number-1)*3+(Number+1)*2)))

#Exercicio 33
AreaQ = float(input('Digite o lado de um quadrado: '))
print('Area do Quadrado: {0:.2f}'.format(AreaQ * 2**.5))#Pode se substituir 2**.5 por pow(2, 1/2)

#Exercicio 34
Raio = float(input('Digite o valor do raio de um circulo: '))
print('A área do circuilo é: {0:.2f}'.format(pow(Raio, 2)*3.14159265358979))

#Exercicio 35
a = float(input('Digite o cateto a do triangulo: '))
b = float(input('Digite o cateto b do triangulo: '))
print('A hipotenusa é: {0:.2f}'.format(pow(pow(a, 2)+pow(b, 2), 1/2)))

#Exercicio 36
RaioC = float(input('Digite o raio do cilindro: '))
AltuC = float(input('Digite a altura do cilindro: '))
print('O volume do cilindro é: {0:.2f}'.format(pow(RaioC, 2)*AltuC*3.14159265358979))

#Exercicio 37
Preco = float(input('Digite o preço do produto R$ '))
print('O preço de R$ {0:.2f} com 12% de desconto é R$ {1:.2f}'.format(Preco, Preco*.88))

#Exercicio 38
Salario = float(input('Digite seu salário: '))
print('Seu salario {0:.2f} com 25% de aumento é: {1:.2f}'.format(Salario, Salario*1.25))

#Exercicio 39
premio = 780000
print('O premio de R$ 780.000,00 será dividido em 3 ganhadores\n1° Lugar receberá: {0:.2f}\n2° Lugar receberá: {1:.2f}\n3° Lugar receberá: {2:.2f}'.format(premio*.46, premio*.32, premio*.22))

#Exercicio 40
dias = int(input('Digite a quantidade de dias trabalhados: '))
salario = float(dias*30*.92)
print('Será pago R$ {0:.2f}'.format(salario))

#Exercicio 41
HorasR = float(input('Digite o valor da hora em R$ '))
HorasT = float(input('Digite o número de horas trabalhadas: '))
print('O salario a receber será R$ {0:.2f}'.format((HorasR*HorasT)*1.1))

#Exercicio 42
SalBase = float(input('Digite o salario base: '))
print('Seu salário será: {0:.2f}'.format(SalBase*.98))

#Exercicio 43
ValorB = float(input('Digite o valor do produto: '))
ValorD = ValorB * .90
print('O total a pagar com 10% de Desconto: {0:.2f}\nParcelamento em 3x sem juros: {1:.2f}'.format(ValorD, ValorB/3))
print('Comissão da venda a vista: {0:.2f}\nComissão da venda parcelada: {1:.2f}'.format(ValorD*.05, ValorB*.05))

#Exercicio 44
AltDeg = float(input('Digite a altura desejada de cada degrau em metros: '))
AltEsc = float(input('Digite a altura que a escada deverá ter em metros: '))
Degraus = AltEsc / AltDeg
print('A escada deverá ter degraus com altura de {0:.2f} metros e {1:.0f} degraus'.format(AltDeg, Degraus))

#Exercicio 45
letra = input('Digite uma letra maiuscula: ')
print(letra.lower())

#Exercicio 46
a = str(input('Digite um número de 3 Digitos: '))
print('Ordem inversa: {0}{1}{2}'.format(a[2], a[1], a[0]))

#Exercicio 47
a = input('Digite um número de 4 Digitos: ')
print('{0}\n{1}\n{2}\n{3}'.format(a[0], a[1], a[2], a[3]))

#Exercicio 48
a = int(input('Segundos inteiro:'))
hora = int(a/3600)
minuto = int((a - (3600*hora)) / 60)
segundo = int((a - (3600*hora) - (minuto*60)))
print('{}:{}:{}'.format(hora, minuto, segundo))

#Exercicio 49
hora1 = int(input('Digite a hora inicial: '))
minuto1 = int(input('Digite o minuto inicial: '))
segundo1 = int(input('Digite o segundo inicial: '))

a = int(input('Digite quantos segundos:'))
hora = int(a/3600)
minuto = int((a - (3600*hora)) / 60)
segundo = int((a - (3600*hora) - (minuto*60)))

horaf = hora1 + hora
minutof = minuto1 + minuto
segundof = segundo1 + segundo

if(segundof>59):
    segundof = segundof - 60
    minutof += 1
if(minutof>59):
    minutof = minutof - 60
    horaf += 1
if(horaf>23):
    horaf = 0
print('{}:{}:{}'.format(horaf, minutof, segundof))

#Exercicio 50
AnoN = int(input('Digite o ano de nascimento: '))
AnoA = int(input('Digite o ano atual: '))
print('Sua idade é: {} anos'.format(AnoA - AnoN))

#Exercicio 51
x = []
y = []
for i in range(0, 2):
    a = int(input('Digite a coordenada X{}: '.format(i)))
    x.append(a)
    a = int(input('Digite a coordenada Y{}: '.format(i)))
    y.append(a)
print('X {0}, Y {1}'.format(x, y))
x.append(x[1] - x[0])
y.append(y[1] - y[0])
r = pow(pow(x[2], 2) + pow(y[2], 2), 1/2)
print('O R² é: {0:.2f}'.format(r))

#Exercicio 52
a = []
t = 0
for i in range(0, 3):
    a.append(float(input('Digite o valor do investidor {0}:'.format(i+1))))
    t = t + a[i]
premio = float(input('Digite o valor do prêmio: '))
print('O investidor 1 receberá: {0:.2f}\nO investidor 2 receberá: {1:.2f}\nO investidor 3 receberá: {2:.2f}\n'.format(premio*(a[0]/t), premio*(a[1]/t), premio*(a[2]/t)))

#Exercicio 53
larg = float(input('Digite a largura do terreno em metros: '))
comp = float(input('Digite o comprimento do terreno em metros: '))
peri = (larg + comp) * 2
preco = float(input('Digite o preço da cerca por metro em R$:'))
print('O valor para cercar o terreno será R$ {0:.2f}'.format(peri*preco))
"""

"""
#Compilador online
https://www.programiz.com/python-programming/online-compiler/?ref=f0f2fd03
"""
