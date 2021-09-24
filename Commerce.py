Produtos = {'TV': 1299, 'PS4': 2299, 'XBOX': 1999, 'Nintendo': 2100, 'Controle': 199, }
Lista = {}
Var = ''
Count = 0
Valor = 0
while Var != 'SAIR':
    Var = str(input('Digite o produto: '))
    Var = Var.upper()
    if Var == 'SAIR':
        break
    if Var in Produtos:
        Valor = Produtos[Var]
    else:
        Cad = str(input('Produto não cadastrado!\nDeseja cadastra-lo?\n'))
        Cad = Cad.upper()
        if Cad == 'Y' or Cad == 'SIM' or Cad == 'YES' or Cad == 'S':
            Valor = int(input('Informe o valor: '))
            Produtos[Var] = Valor
        else:
            Valor = 0
    if Valor == 0:
        Qtde = 0
    else:
        Qtde = int(input('Digite a quantidade: '))
        print('{0} x {1:.2f} = {2:.2f}'.format(Qtde, Valor, Valor*Qtde))
        Lista.update({Var: Qtde*Valor})
        Count = Count + (Qtde*Valor)
print('\'Produtos\': \'Valor produtos\' = {0} Total = {1}'.format(Lista, Count))
