num = int(input())

if num % 2 == 0 and num % 5 == 0:
    print('é divisivel por 2 e por 5')
else:
    if num % 2 != 0 and num % 5 != 0:
        print('não é divisivel por 2 e nem por 5')
    if num % 2 == 0:
         print('é divisivel por 2')
    if num % 5 == 0:
         print('é divisivel por 5')
