def to_decimal(num_str, base):
    """Перевод числа num_str из системы base в 10-ю"""
    try:
        return int(num_str, base)
    except ValueError:
        return None


# ввод данных
num_str = input("Введите число: ").strip()
base = int(input("Введите систему счисления (2–36): "))

result = to_decimal(num_str, base)

if result is not None:
    print(f"Число {num_str} из системы {base} в десятичной = {result}")
else:
    print("Ошибка: некорректное число для указанной системы счисления.")