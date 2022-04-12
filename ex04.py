j = int(input('Digite o número do somas que você irá fazer: '))
def somar(i = int):
    soma = 0
    for i in range(j):
        num = float(input('Digite um número: '))
        soma += num
    return i, soma

valores = somar(j)
med = valores[0]
soma = valores[1]

print(f'A média das somas é: {soma/med}')