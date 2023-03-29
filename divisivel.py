numero = int(input())

div3 = numero % 3
div5 = numero % 5

if div3 == 0:
    print('É divisivel por 3')
else:
    if div3 == 1:
        print('Não é divisivel por 3')
if div5 == 0:
    print('É divisivel por 5')
else:
    if div5 == 1:
        print('Não é divisivel por 5')
        
