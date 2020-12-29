import random

chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwyzABCDEFGHIJKLNOPQRSTUVWYZ123456789'

number = int(input('Кол-во пароль: '))
lenght = int(input('Длина строка: '))

for x in range (number):
    password = ''

    for i in range(lenght):
        password += random.choice(chars)

    print(password)
    file = open('password.txt', 'a')
    file.write('\n' + password)
    file.close()