salario = int(input('Coloque seu salário para empréstimo aqui: '))
prestação = int(input())

porc_salario = (20 / 100) * salario

if prestação > porc_salario:
    print('Empréstimo não concedido')
else:
    if prestação < porc_salario:
        print('Empréstimo concedido')



