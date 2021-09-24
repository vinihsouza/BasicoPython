#5 - Sucessor e antecessor
a = int(input('Digite um número:'))
print('Seu sucessor é: {} \nSeu antecessor é: {}'.format(a+1,a-1))

#6 - Dobro, triplo e raiz
a = int(input('Digite um número:'))
b = a * 2
c = a * 3
d = float(a**(1/2))
print('O dobro é: {}\nO triplo é: {}\nA raiz é:{:.2f}'.format(b,c,d))

#7 - Média aluno
n1 = float(input('Digite a nota 1:'))
n2 = float(input('Digite a nota 2:'))
m = (n1+n2)/2
print('Sua média é:{:.2f}'.format(m))

#8 - Metros centimetros e milimetros
metros = float(input('Digite o valor de metros:'))
print('{:.2f} Metros = {:.0f} Centimetros = {:.0f} Milimetros'.format(metros,metros*100,metros*1000))

#9 - Tabuada
n = int(input('Digite um número:'))
a = 0
while a<11:
    print('{} * {} = {}'.format(n,a,n*a))
    a = a + 1

#10 - Dolar
d = float(input('Digite sua quantidade de dinheiro:'))
print('Você poderá comprar: {:.2f} USD'.format(d/4.96))

#11 - Problema
l = float(input('Digite a largura da parede:'))
a = float(input('Digite a altura da parede:'))
print('Area: {:.2f}m²\nQuantidade de tinta: {:.2f}L'.format(l*a,(l*a)/2))

#12 - 5% de desconto
preco = float(input('Digite o preço:'))
print('Preço com 5% de desconto: {:.2F} BRL'.format(preco-(preco*0.05)))

#13 - Novo salario
sal = float(input('Digite seu salario atual:'))
print('Seu novo salario com 15% de aumento é:{}'.format(sal*1.15))
