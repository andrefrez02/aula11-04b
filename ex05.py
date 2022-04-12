def bin2Dec():
    binario = input('Digite um número binário: ')
    decimal = 0
    n = len(binario) - 1
    for d in binario:
        decimal = decimal + int(d)*2**n
        n -= 1
    return binario, decimal

def dec2Bin():
    num = int(input('Digite um número decimal: '))
    bin = ''
    while num != 0:
        r = num%2
        bin = str(r) + bin
        num = num//2
    return bin, num

def saidab2d():
    val = bin2Dec()
    bin = val[0]
    dec = val[1]
    print(f'O binário {bin} é igual a {dec} na base 10')

def saidad2b():
    val = dec2Bin()
    bin = val[0]
    dec = val[1]
    print(f'O decimal {dec} é igual a {bin} na base 2')

saidab2d()
saidad2b()