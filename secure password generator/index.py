from random import *

# Функция генерации одного пароля
def generate_password(length, chars):
    password = ''
    for _ in range(length):
        password += choice(chars)
    return password

# Строковые константы
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'

# Переменная для набора допустимых символов
chars = ''

# Запрос параметров у пользователя
count = int(input('Количество паролей для генерации: '))
length = int(input('Длина одного пароля: '))

include_digits = input('Включать ли цифры 0123456789? (да/нет): ').lower() == 'да'
include_uppercase = input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (да/нет): ').lower() == 'да'
include_lowercase = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (да/нет): ').lower() == 'да'
include_symbols = input('Включать ли символы !#$%&*+-=?@^_? (да/нет): ').lower() == 'да'
exclude_ambiguous = input('Исключать ли неоднозначные символы il1Lo0O? (да/нет): ').lower() == 'да'

# Формируем набор символов
if include_digits:
    chars += digits
if include_uppercase:
    chars += uppercase_letters
if include_lowercase:
    chars += lowercase_letters
if include_symbols:
    chars += punctuation

# Генерируем и выводим пароли
print('Ваши пароли:')
for _ in range(count):
    print(generate_password(length, chars))