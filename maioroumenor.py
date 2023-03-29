n1 = int(input())
n2 = int(input())
n3 = int(input())

maior, menor, meio = 0, 0, 0

if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = n2
else:
    maior = n3
if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n1 and n2 < n3:
    menor = n2
else:
    menor = n3
if n1 > menor and n1 < maior:
    meio = n1
elif n2 > menor and n2 < maior:
    meio = n2
else:
    meio = n3

print(menor)
print(meio)
print(maior)
