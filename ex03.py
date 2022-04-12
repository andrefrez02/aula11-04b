animais = ['cachorro', 'leao', 'gato', 'dragao', 'camelo']
for a in animais:
    if a == 'gato':
        continue
    if a == 'camelo':
        print(a, end = '. ')
    else:
        print(a, end = ', ')