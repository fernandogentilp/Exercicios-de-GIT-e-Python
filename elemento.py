seq = input().split()
elemento = int(input())

l = []
for i in range(len(seq)):
    num = int(seq[i])
    l.append(num)

s = []
for e in l:
    if elemento == e:
        print('Este elemento se encontra na sequência!')
if not elemento == e:
    print('Este elemento é inválido')

