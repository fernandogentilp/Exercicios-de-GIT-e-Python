peso = input().split()

l = []
for i in range(len(peso)):
    num = int(peso[i])
    l.append(num)
normal, anemico, obeso = 0, 0, 0
for quilo in l:
    if 50 <= quilo <= 70:
        normal = quilo
        print(f'você pesa {normal}, está normal!')
    else:
        if num > 70:
            obeso = quilo
            print(f'você pesa {obeso}, está obeso.')
        if num < 50:
            anemico = quilo
            print(f'você pesa {anemico}, está anemico.')        
