import math
import cmath

print("""
Мій перший калькулятор!
Доступні операції:
 1 - додавання +
 2 - віднімання -
 3 - множення * 
 4 - ділення /
 5 - зведення в ступінь
 6 - квадратний корінь
 7 - кубічний корінь
 8 - синус числа
 9 - косинус числа
10 - тангес числа
""")
c = int(input("Оберіть номер операції: "))
if 1 <= c <= 5:
    a = int(input("Введіть перше число, a: "))
    b = int(input("Введіть друге число, b: "))
    print("-" * 20)
    match c:
        case 1:
            print(f'{a} + {b} = {a+b}')
        case 2:
            print(f'{a} - {b} = {a-b}')
        case 3:
            print(f'{a} * {b} = {a*b}')
        case 4:
            print(f'{a} / {b} = {a/b}')
        case 5:
            print(f'{a} у ступені {b} = {math.pow(a, b)}')
else:
    d = int(input("Введіть число: "))
    print("-" * 20)
    match c:
        case 6:
            if d < 0:
                print(f'Квадтратний корінь числа {d} через cmath = {cmath.sqrt(d)}')
            else:
                print(f'Квадтратний корінь числа {d} через math= {math.sqrt(d)}')
            print('Квадтратний корінь числа', d, 'через ступінь 0,5 =', d ** 0.5)
        case 7:
            print('Кубичний корінь числа', d, 'через ступінь 1/3 =', d ** 1/3)
        case 8:
            print(f'Синус числа {d} =', math.sin(d))
        case 9:
            print(f'Косинус числа {d} =', math.cos(d))
        case 10:
            print(f'Тангес числа {d} =', math.tan(d))
print("-" * 20)
print("Bay!")
