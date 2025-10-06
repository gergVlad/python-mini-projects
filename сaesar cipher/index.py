def caesar_cipher(text, shift, lang, direction):
    # Определяем алфавит в зависимости от языка
    if lang == 'ru':
        alphabet_lower = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
        alphabet_upper = alphabet_lower.upper()
        n = 32
    elif lang == 'en':
        alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
        alphabet_upper = alphabet_lower.upper()
        n = 26
    else:
        return "Неверно указан язык!"

    # Для дешифрования — сдвиг влево
    if direction == 'дешифрование':
        shift = -shift

    result = ''
    for char in text:
        if char.isalpha():
            if char.islower():
                index = alphabet_lower.find(char)
                new_char = alphabet_lower[(index + shift) % n]
            else:
                index = alphabet_upper.find(char)
                new_char = alphabet_upper[(index + shift) % n]
            result += new_char
        else:
            result += char
    return result


# --- Основная программа ---

print('Привет! Это шифр Цезаря 🔐')

direction = input('Выберите направление (шифрование / дешифрование): ').strip().lower()
lang = input('Выберите язык (русский / английский): ').strip().lower()
shift = int(input('Введите шаг сдвига (целое число): '))
text = input('Введите текст для обработки: ')

# Определяем язык короткой меткой
if lang.startswith('р'):
    lang = 'ru'
elif lang.startswith('а') or lang.startswith('e'):
    lang = 'en'

# Вызываем функцию
result = caesar_cipher(text, shift, lang, direction)

print('Результат:')
print(result)