i = 1

while i <= 10:
    nota1 = float(input('Digite a primeira nota: '))    
    nota2 = float(input('Digite a segunda nota: '))    
    media = (nota1 + nota2) / 2
    print(f'A média do {i}° aluno é {media}')
    i += 1