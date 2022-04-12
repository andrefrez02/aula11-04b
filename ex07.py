soma = 0
qnt = 0

while True:
    num = int(input('Digite um número inteiro[Digite 0 para sair]: '))
    soma += num
    if num == 0:
        break
    qnt +=1

media = soma / qnt

print(f'A média dos números digitados é {media}')