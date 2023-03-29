one = int(input())
two = int(input())

if (one >= 1) and (one <= 10):
    if (two >= 1) and (two <= 10):
        print('Seu número secreto é: ', one * two)
    else:
        print('Segundo número incorreto!')
else:
    print('Primeiro número incorreto!')
