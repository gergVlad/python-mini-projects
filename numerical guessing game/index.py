from random import *

print('Добро пожаловать в числовую угадайку')

# защитой от дурака.
def is_valid(text):
    return text.isdigit() and 1 <= int(text) <= 100

num = randint(1,100)
attempts = 0  # счётчик попыток

while True:
    user_input = input('Введите число от 1 до 100: ')

    if not is_valid(user_input):
        print('А может быть все-таки введем целое число от 1 до 100?')
        continue  # возвращаемся к началу цикла

    # если ввод корректный — преобразуем к числу
    user_num = int(user_input)
    attempts += 1

    if user_num < num:
        print('Ваше число меньше загаданного, попробуйте еще разок')
        continue
    elif user_num > num:
        print('Ваше число больше загаданного, попробуйте еще разок')
        continue
    elif user_num == num:
        print(f'Вы угадали число {num} за {attempts} попыток, поздравляем!')
        break

print('Спасибо, что играли в числовую угадайку. Еще увидимся...')