resp = 's'
i = 0
maior = 0

while resp in 'sS':
    num = int(input('Digite um número inteiro: '))
    if num >= 10:
        maior = maior + i
    resp = input('Digite "N" para sair[s/n]: ')

print(f'Foram digitados {maior} número maiores que 10.')