num = int(input('Digite um número decimal: '))
bin = ''

while num != 0:
    r = num%2
    bin = str(r) + bin
    num = num//2

print(f'O binário é {bin}')