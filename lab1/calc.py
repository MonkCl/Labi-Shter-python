
while True:
    print('Выберите логическое выражение:\n',
          'xor - ^\nand - &\nor - |\nnot - !\n',
          'Для завершения программы - exit')
    choice = input()
    if choice == '^':
        print('Введите две бинарные последовательности')
        a = '0b' + ''.join([i for i in input('1) ') if i in '01'])
        b = '0b' + ''.join([i for i in input('2) ') if i in '01'])
        print('1) ', a)
        print('2) ', b)
        print('=> ', bin(int(a, 2) ^ int(b, 2)))
    elif choice == '&':
        print('Введите две бинарные последовательности')
        a = '0b' + ''.join([i for i in input('1) ') if i in '01'])
        b = '0b' + ''.join([i for i in input('2) ') if i in '01'])
        print('1) ', a)
        print('2) ', b)
        print('=> ', bin(int(a, 2) & int(b, 2)))
        pass
    elif choice == '|':
        print('Введите две бинарные последовательности')
        a = '0b' + ''.join([i for i in input('1) ') if i in '01'])
        b = '0b' + ''.join([i for i in input('2) ') if i in '01'])
        print('1) ', a)
        print('2) ', b)
        print('=> ', bin(int(a, 2) | int(b, 2)))
        pass
    elif choice == '!':
        print('Введите бинарную последовательность')
        a = '0b' + ''.join([i for i in input('1) ') if i in '01'])
        print('1) ', a)
        print('=> ', bin(~int(a, 2)))
        pass
    elif choice == 'exit':
        break
    else:
        print('Некорректная команда.')
print('Завершение программы')
