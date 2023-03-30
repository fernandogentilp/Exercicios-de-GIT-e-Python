#Essa função retorna o valor do dobro de uma variável
def dobro(x):
    num = x
    dobro = num * 2
    return dobro
#Esse escopo de código, está fazendo a raíz quadrada da variavel num2, usando a função dobro e fazendo a exponenciação de 1/2, que é basicamente a raiz quadrada
num2 = dobro(5) ** (1/2)
print(num2)

